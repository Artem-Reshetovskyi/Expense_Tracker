document.addEventListener("DOMContentLoaded", function () {
    // Витрати
    const expenseCtx = document.getElementById('expenseChart').getContext('2d');
    new Chart(expenseCtx, {
      type: 'pie',
      data: {
        labels: window.categoryLabels,
        datasets: [{
          label: 'Expenses by Category',
          data: window.categoryData,
          backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#8E44AD', '#2ECC71']
        }]
      }
    });
  
    // Доходи
    const incomeCtx = document.getElementById('incomeChart').getContext('2d');
    new Chart(incomeCtx, {
      type: 'pie',
      data: {
        labels: window.incomeLabels,
        datasets: [{
          label: 'Income by Description',
          data: window.incomeData,
          backgroundColor: ['#3498DB', '#E67E22', '#1ABC9C', '#F1C40F', '#E74C3C', '#9B59B6']
        }]
      }
    });
  });
  