function redraw_chart(before, after) {
  fetch(`/chart-data?before=${before}&after=${after}`)
 : .then(response => response.json())
  .then(data => {
      var ctx = document.getElementById('myChart').getContext('2d');
      var myChart = new Chart(ctx, {
          type: 'bar',
          data: {
              labels: data.hours,
              datasets: [{
                  label: 'Number of Events',
                  data: data.event_counts,
                  backgroundColor: 'rgba(255, 99, 132, 0.2)',
                  borderColor: 'rgba(255, 99, 132, 1)',
                  borderWidth: 1
              }]
          },
          options: {
              scales: {
                  yAxes: [{
                      ticks: {
                          beginAtZero: true
                      }
                  }]
              }
          }
      });
  });
}
const before_input = document.querySelector('input[name="before"]');
const after_input = document.querySelector('input[name="after"]');
var before_val = before_input.value;
var after_val = after_input.value;
redraw_chart(before_val, after_val);
const redraw_button = document.querySelector('button[name="redraw"]');
redraw_button.addEventListener('click', () => {
  let chartStatus = Chart.getChart("myChart"); // <canvas> id
  if (chartStatus != undefined) {
    chartStatus.destroy();
  }
  before_val = before_input.value;
  after_val = after_input.value;
  console.log(`before ${before_val} after ${after_val}`);
  redraw_chart(before_val, after_val);
  console.log('redraw time');
});


const opts = {
  format: 'dd.mm.yyyy'
};
const datepicker_before = new Datepicker(before_input, opts);
const datepicker_after = new Datepicker(after_input, opts);

