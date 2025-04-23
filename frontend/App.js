import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [categorizedData, setCategorizedData] = useState([]);
  const [prediction, setPrediction] = useState(null);
  const [tips, setTips] = useState([]);
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(false); // NEW

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleAnalyze = async () => {
    if (!selectedFile) {
      alert('Please select a file first.');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      setLoading(true); // NEW

      const uploadRes = await axios.post('/analyze', formData);
      setCategorizedData(uploadRes.data.categorized);
      setPrediction(uploadRes.data.next_month_prediction);
      setTips(uploadRes.data.tips || []);
      setMessage(uploadRes.data.message || 'Analysis complete.');

    } catch (error) {
      console.error('Error:', error);
      setMessage('An error occurred during processing.');
    } finally {
      setLoading(false); // NEW
    }
  };

  return (
    <div className="App">
      <h1>📊 MyBudgetAI</h1>

      <input type="file" accept=".csv" onChange={handleFileChange} />
      <button onClick={handleAnalyze}>Analyze</button>

      {loading && <div className="spinner"></div>} {/* NEW */}

      {message && !loading && <p><strong>{message}</strong></p>}

      {!loading && prediction && (
        <div className="card">
          <h2>📈 Predicted Spending Next Month</h2>
          <p>₹ {prediction}</p>
        </div>
      )}

      {!loading && tips.length > 0 && (
        <div className="card">
          <h2>💡 Smart Saving Tips</h2>
          <ul>
            {tips.map((tip, index) => (
              <li key={index}>{tip}</li>
            ))}
          </ul>
        </div>
      )}

      {!loading && categorizedData.length > 0 && (
        <div className="card">
          <h2>🧾 Categorized Transactions</h2>
          <table>
            <thead>
              <tr>
                <th>Date</th>
                <th>Description</th>
                <th>Amount</th>
                <th>Type</th>
                <th>Category</th>
              </tr>
            </thead>
            <tbody>
              {categorizedData.map((tx, index) => (
                <tr key={index}>
                  <td>{tx.date}</td>
                  <td>{tx.description}</td>
                  <td>{tx.amount}</td>
                  <td>{tx.type}</td>
                  <td>{tx.category}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default App;
