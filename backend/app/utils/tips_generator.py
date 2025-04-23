def generate_saving_tips(df):
    tips = []
    category_totals = df.groupby('category')['amount'].sum()

    if category_totals.get('OTT Subscription', 0) > 500:
        tips.append("Review your OTT subscriptions. You might be paying for multiple platforms.")
    if category_totals.get('Food', 0) > 2000:
        tips.append("You're spending quite a lot on food. Try home-cooked meals to save.")
    if category_totals.get('Transport', 0) > 1500:
        tips.append("Consider carpooling or public transport to cut transport costs.")
    if category_totals.get('Shopping', 0) > 3000:
        tips.append("Shopping expenses are high. Consider tracking non-essential purchases.")
    if category_totals.get('Others', 0) > 2000:
        tips.append("Review your 'Others' category to find avoidable expenses.")

    if not tips:
        tips.append("You're doing great with your spending! Keep it up.")

    return tips
