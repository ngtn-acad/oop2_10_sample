const credit_summary_chart = document.getElementById('credit_summary_chart');

    fetch('/api/month_total_by_product')//後で聞いて直す
      .then(res => res.json())
      .then(data => {
        console.log(data)

        new Chart(credit_summary_chart, {
          type: 'bar',
          data: {
            labels: data.labels,
            datasets: [{
              axis: 'y',
              label: '売り上げ(円)',
              data: data.data,
              fill: false,
              backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(201, 203, 207, 0.2)'
              ],
              borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)'
              ],
              borderWidth: 1

            }]
          },
          options: {
            responsive: true,
            indexAxis: 'y',
            scales: {
              x: {
                beginAtZero: true
              }
            }
          }
        })
      })


    const credit_ranking_chart = document.getElementById('credit_ranking_chart');

    fetch('/api/user_ranking')//後で聞いて直す
      .then(res => res.json())
      .then(data => {
        console.log(data)

        new Chart(credit_ranking_chart, {
          type: 'doughnut',
          data: {
            labels: data.labels,
            datasets: [{
              data: data.data,
              borderWidth: 1

            }]
          },
          options: {
            responsive: true,
             plugins: {
                legend: {
                  position: 'right'
                }
             }
          }
        })
      })