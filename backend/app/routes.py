from flask import Blueprint, request, jsonify
import pandas as pd
import io
from app.utils.categorizer import categorize_description
from app.utils.tips_generator import generate_saving_tips
from app.utils.predictor import predict_next_month

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "MyBudgetAI backend is running!"

@main.route('/analyze', methods=['POST'])
def analyze():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    try:
        df = pd.read_csv(io.StringIO(file.stream.read().decode("utf-8")))

        # Clean and preprocess
        df = df[df['Type'].str.lower() == 'debit']
        df['Date'] = pd.to_datetime(df['Date'])
        df['Amount'] = df['Amount'].astype(float)
        df['Description'] = df['Description'].astype(str)

        # Categorize each transaction
        categorized_transactions = []
        for _, tx in df.iterrows():
            category = categorize_description(tx['Description'])
            categorized_transactions.append({
                'date': tx['Date'].strftime('%Y-%m-%d'),
                'description': tx['Description'],
                'amount': tx['Amount'],
                'type': tx['Type'],
                'category': category
            })

        # Predict next month’s expense
        df['Month'] = df['Date'].dt.to_period('M')
        monthly_expense = df.groupby('Month')['Amount'].sum().reset_index()
        prediction = predict_next_month(monthly_expense)

        # Generate tips
        categorized_df = pd.DataFrame(categorized_transactions)
        tips = generate_saving_tips(categorized_df)

        return jsonify({
            'message': 'Analysis complete!',
            'categorized': categorized_transactions,
            'next_month_prediction': float(prediction),
            'tips': tips
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
