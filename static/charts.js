
const css = v => getComputedStyle(document.documentElement).getPropertyValue(v).trim();
const money = n => n >= 1e6 ? '$' + (n / 1e6).toFixed(2) + 'M' : n >= 1e3 ? '$' + (n / 1e3).toFixed(1) + 'K' : '$' + n.toFixed(0);

function barChart(id, labels, data, fmt) {
  new Chart(document.getElementById(id), {
    type: 'bar',
    data: { labels, datasets: [{ data, backgroundColor: css('--accent'), borderRadius: 3 }] },
    options: {
      indexAxis: 'y', maintainAspectRatio: false,
      plugins: { legend: { display: false }, tooltip: { callbacks: { label: x => fmt(x.raw) } } },
      scales: { x: { grid: { color: css('--line') }, ticks: { color: css('--muted') } },
                y: { grid: { display: false }, ticks: { color: css('--text') } } }
    }
  });
}

function lineChart(id, labels, series) {
  new Chart(document.getElementById(id), {
    type: 'line',
    data: { labels, datasets: series.map(s => ({ label: s.label, data: s.data, borderColor: css(s.color),
                                                 backgroundColor: css(s.color), tension: .25 })) },
    options: {
      maintainAspectRatio: false,
      plugins: { legend: { labels: { color: css('--text') } }, tooltip: { callbacks: { label: x => x.dataset.label + ': ' + money(x.raw) } } },
      scales: { x: { grid: { display: false }, ticks: { color: css('--muted') } },
                y: { grid: { color: css('--line') }, ticks: { color: css('--muted'), callback: money } } }
    }
  });
}
