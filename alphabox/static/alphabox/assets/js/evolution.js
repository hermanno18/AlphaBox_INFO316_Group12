/* globals Chart:false, feather:false */

(function () {
  'use strict'

  //feather.replace()
var datas =  [
  15,
  21,
  8,
  24,
  23,
  24,
  34,
]
var labelsFromJson = [
  'Sunday',
  'Monday',
  'Tuesday',
  'Wednesday',
  'Thursday',
  'Friday',
  'Saturday'
]
  // Graphs
  var ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: labelsFromJson,
      datasets: [{
        label : 'Moyenne de mots appris',
        data: datas,
        lineTension: 0.5,
        backgroundColor: 'rgba(9, 218, 54, 0.150)',
        borderColor: 'rgba(9, 218, 54, 0.950)',
        borderWidth: 2,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      tooltips: {
          mode: 'nearest'
      },
      legend: {
        display : false
      },
      title: {
        display: true,
        text: 'Courbe de votre évolution ce mois',
        position: 'left',
        fontSize: 16,
        padding: 20
    },
    }
  })
})()
