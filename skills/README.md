# skills/ — skill untuk Veda

Format: satu folder per skill, berisi `SKILL.md` dengan frontmatter `name` + `description`, lalu isi
prosedur. Ini format Muse Code; validasi sebelum dipakai:

```
muse skills validate ./bounty-cycle
muse skills install ./bounty-cycle --scope user
muse skills list --source user
```

Tanpa CLI: simpan di `~/skills/<id>/SKILL.md`, panggil dengan path eksplisit ("baca ~/skills/…").

Aturan penulisan (dipakai juga oleh `skill-authoring`):
- `description` satu kalimat, diawali "Use when …" — itu yang dibaca saat katalog, jadi harus bisa
  dicocokkan ke situasi tanpa membuka isi.
- Isi = urutan langkah + jebakan, bukan esai. Satu aturan per baris.
- Angka konkret lebih baik daripada "secukupnya". Kalau ada batas, tulis batasnya.
- Skill yang menyentuh produk Muse harus menyebut jalur nyata (file, menu, perintah), bukan kiasan.

| skill | dipakai saat |
|---|---|
| `bounty-cycle` | target bounty baru / melanjutkan target |
| `recon-briefs` | menulis goal sub-agent recon |
| `evidence-hygiene` | mengumpulkan dan merapikan bukti |
| `report-writer` | menulis laporan temuan |
| `triage-gate` | memutuskan kandidat layak kirim atau tidak |
| `daily-ops` | rutinitas harian non-bounty |
| `memory-hygiene` | Memory mulai panjang/basi |
| `skill-authoring` | menulis atau memperbaiki skill |

Skill ini **tidak** menimpa Soul. Kalau bertabrakan, Soul menang dan skill-nya diperbaiki.
