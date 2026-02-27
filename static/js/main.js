// ===== Table search filter =====
function filterTable() {
  const input = document.getElementById('searchInput');
  if (!input) return;

  const filter = input.value.toLowerCase();
  const table  = document.getElementById('usersTable');
  if (!table) return;

  const rows = table.getElementsByTagName('tr');
  let visibleCount = 0;

  // Start from index 1 to skip the header row
  for (let i = 1; i < rows.length; i++) {
    const row = rows[i];
    const text = row.textContent.toLowerCase();
    if (text.indexOf(filter) > -1) {
      row.style.display = '';
      visibleCount++;
    } else {
      row.style.display = 'none';
    }
  }

  // Update count if element exists
  const footer = document.querySelector('.table-footer strong');
  if (footer) footer.textContent = visibleCount;
}

// ===== Bar chart renderer =====
function renderBarChart() {
  const container = document.getElementById('barChart');
  if (!container) return;

  const months  = JSON.parse(container.dataset.months  || '[]');
  const signups = JSON.parse(container.dataset.signups || '[]');
  const logins  = JSON.parse(container.dataset.logins  || '[]');

  if (!months.length) return;

  const maxVal = Math.max(...logins, ...signups);
  const chartHeight = 160; // px — matches CSS .chart-bars height

  container.innerHTML = '';

  months.forEach(function(month, i) {
    const loginH  = Math.round((logins[i]  / maxVal) * chartHeight);
    const signupH = Math.round((signups[i] / maxVal) * chartHeight);

    const group = document.createElement('div');
    group.className = 'chart-group';

    group.innerHTML =
      '<div class="chart-bars">' +
        '<div class="chart-bar chart-bar--blue"  style="height:' + loginH  + 'px" title="Logins: '  + logins[i]  + '"></div>' +
        '<div class="chart-bar chart-bar--green" style="height:' + signupH + 'px" title="Signups: ' + signups[i] + '"></div>' +
      '</div>' +
      '<span class="chart-label">' + month + '</span>';

    container.appendChild(group);
  });
}

// ===== Init =====
document.addEventListener('DOMContentLoaded', function () {
  renderBarChart();
});
