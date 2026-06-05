const TOPSIS = {
  kriteria: ["Harga (USD/mo)", "RAM (GB)", "Storage (GB)", "Slot Pemain", "Uptime (%)", "vCPU"],
  jenis: ["cost", "benefit", "benefit", "benefit", "benefit", "benefit"],
  bobot: [0.20, 0.20, 0.10, 0.10, 0.25, 0.15],

  run: function (data) {
    const n = data.length;
    const m = this.kriteria.length;
    const X = data.map(row => this.kriteria.map(k => parseFloat(row[k])));

    const norm = Array(m).fill(0);
    for (let j = 0; j < m; j++) {
      let sumSq = 0;
      for (let i = 0; i < n; i++) sumSq += X[i][j] * X[i][j];
      norm[j] = Math.sqrt(sumSq);
    }

    const R = X.map(row => row.map((v, j) => v / norm[j]));

    const W = this.bobot;
    const Y = R.map(row => row.map((v, j) => v * W[j]));

    const A_pos = [];
    const A_neg = [];
    for (let j = 0; j < m; j++) {
      const col = Y.map(row => row[j]);
      if (this.jenis[j] === "benefit") {
        A_pos.push(Math.max(...col));
        A_neg.push(Math.min(...col));
      } else {
        A_pos.push(Math.min(...col));
        A_neg.push(Math.max(...col));
      }
    }

    const D_pos = Y.map(row =>
      Math.sqrt(row.reduce((sum, v, j) => sum + (v - A_pos[j]) ** 2, 0))
    );
    const D_neg = Y.map(row =>
      Math.sqrt(row.reduce((sum, v, j) => sum + (v - A_neg[j]) ** 2, 0))
    );

    const V = D_neg.map((d, i) => d / (D_pos[i] + d));

    const ranked = data.map((row, i) => ({
      ...row,
      _R: R[i],
      _Y: Y[i],
      _D_pos: D_pos[i],
      _D_neg: D_neg[i],
      _V: V[i]
    }));
    ranked.sort((a, b) => b._V - a._V);
    ranked.forEach((r, i) => r._rank = i + 1);

    return {
      X, R, Y, A_pos, A_neg, D_pos, D_neg, V, norm,
      ranked
    };
  }
};
