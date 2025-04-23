import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

def predict_next_month(monthly_expense_df):
    data = monthly_expense_df['Amount'].values.reshape(-1, 1)
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data)

    X = []
    y = []
    for i in range(1, len(data_scaled)):
        X.append(data_scaled[i-1])
        y.append(data_scaled[i])
    X, y = np.array(X), np.array(y)
    X = X.reshape((X.shape[0], 1, 1))

    model = Sequential()
    model.add(LSTM(units=50, return_sequences=False, input_shape=(1, 1)))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X, y, epochs=100, verbose=0)

    last_value = data_scaled[-1].reshape(1, 1, 1)
    next_month_scaled = model.predict(last_value, verbose=0)
    next_month = scaler.inverse_transform(next_month_scaled)

    return next_month[0][0]
