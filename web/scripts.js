document.addEventListener('DOMContentLoaded', () => {
    const API_BASE_URL = 'http://localhost:5000/api';
  
    const transactionList = document.getElementById('transaction-list');
  
    // Fetch and display transactions
    const fetchTransactions = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/transactions`);
        const transactions = await response.json();
        transactionList.innerHTML = transactions.map(transaction => `
          <li>${transaction.name}</li>
        `).join('');
      } catch (error) {
        console.error('Error fetching transactions:', error);
      }
    };
  
    // Initial fetch
    fetchTransactions();
  });
  