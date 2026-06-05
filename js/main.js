// Navbar mobile toggle
document.addEventListener("DOMContentLoaded", function () {
  const toggle = document.getElementById("menuToggle");
  const navLinks = document.getElementById("navLinks");
  if (toggle && navLinks) {
    toggle.addEventListener("click", function () {
      navLinks.classList.toggle("open");
    });
  }

  // Highlight active page
  const page = document.body.dataset.page;
  if (page) {
    document.querySelectorAll(".nav-links a").forEach(function (a) {
      if (a.dataset.page === page) a.classList.add("active");
    });
  }

  // Step accordion
  document.querySelectorAll(".step-header").forEach(function (header) {
    header.addEventListener("click", function () {
      const step = this.parentElement;
      step.classList.toggle("open");
    });
  });

  // Table search + sort
  initTable();
});

function initTable() {
  const wrapper = document.getElementById("tableWrapper");
  if (!wrapper) return;

  const searchInput = document.getElementById("searchInput");
  const tableBody = document.getElementById("tableBody");

  let currentData = [];
  let sortCol = -1;
  let sortAsc = true;

  function renderTable() {
    const query = (searchInput ? searchInput.value.toLowerCase() : "");

    let filtered = HOSTING_DATA.filter(function (row) {
      return !query ||
        row.Platform.toLowerCase().includes(query) ||
        row.Tier.toLowerCase().includes(query);
    });

    if (sortCol >= 0) {
      filtered.sort(function (a, b) {
        const keys = ["Platform", "Tier", "Harga (USD/mo)", "RAM (GB)", "Storage (GB)", "Slot Pemain", "Uptime (%)", "vCPU"];
        const key = keys[sortCol];
        let va = a[key];
        let vb = b[key];
        if (typeof va === "string") {
          va = va.toLowerCase();
          vb = vb.toLowerCase();
        }
        if (va < vb) return sortAsc ? -1 : 1;
        if (va > vb) return sortAsc ? 1 : -1;
        return 0;
      });
    }

    currentData = filtered;
    renderTableBody();
    updateResultCount();
  }

  function renderTableBody() {
    if (!tableBody) return;
    tableBody.innerHTML = "";
    currentData.forEach(function (row) {
      const tr = document.createElement("tr");
      tr.innerHTML =
        "<td>" + escHtml(row.Platform) + "</td>" +
        "<td>" + escHtml(row.Tier) + "</td>" +
        "<td>$" + row["Harga (USD/mo)"].toFixed(2) + "</td>" +
        "<td>" + row["RAM (GB)"] + " GB</td>" +
        "<td>" + row["Storage (GB)"] + " GB</td>" +
        "<td>" + row["Slot Pemain"] + "</td>" +
        "<td>" + row["Uptime (%)"] + "%</td>" +
        "<td>" + row["vCPU"] + "</td>" +
        "<td><a href='" + escHtml(row.url) + "' target='_blank' rel='noopener' class='btn-visit'>Kunjungi</a></td>";
      tableBody.appendChild(tr);
    });
  }

  function updateResultCount() {
    const el = document.getElementById("resultCount");
    if (el) el.textContent = "Menampilkan " + currentData.length + " dari " + HOSTING_DATA.length + " hosting";
  }

  // Sort on header click
  document.querySelectorAll("#tableWrapper th[data-col]").forEach(function (th) {
    th.addEventListener("click", function () {
      const col = parseInt(this.dataset.col);
      if (sortCol === col) sortAsc = !sortAsc;
      else { sortCol = col; sortAsc = true; }
      document.querySelectorAll("#tableWrapper th").forEach(function (h) { h.classList.remove("sorted"); });
      this.classList.add("sorted");
      renderTable();
    });
  });

  if (searchInput) searchInput.addEventListener("input", renderTable);

  renderTable();
}

function escHtml(str) {
  var div = document.createElement("div");
  div.appendChild(document.createTextNode(str));
  return div.innerHTML;
}

// TOPSIS result runner for metode page
function runTopsisForMetode() {
  const result = TOPSIS.run(HOSTING_DATA);
  return result;
}
