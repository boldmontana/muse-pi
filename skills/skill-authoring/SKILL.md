---
name: skill-authoring
description: "Use when writing or fixing a skill: format, description rules, validation, test on one real task, changelog."
---

# Skill authoring

Skill adalah prosedur yang dipakai ulang. Kalau isinya cuma pengetahuan umum, bukan skill.

## Sebelum menulis

1. Apakah ini sudah dua kali dikerjakan manual dan bentuknya sama? Kalau belum, tunda.
2. Apakah ada skill lain yang menutupi? Kalau ada, perluas yang lama — jangan bikin kembar.
3. Apakah langkahnya bisa diperiksa (keluaran, exit, file)? Kalau tidak, tulis lebih konkret.

## Format

```
skills/<id>/SKILL.md
---
name: <id>
description: "Use when <situasi>. <satu kalimat perilaku>."
---
# Judul
## Kapan
## Urutan langkah
## Jebakan
```

- `id`: huruf kecil, tanda hubung, ≤40 karakter.
- `description` ≤160 karakter, diawali "Use when". Itu yang dibaca katalog.
- Langkah bernomor, satu aksi per langkah, perintah konkret di blok kode.
- Jebakan ditulis dari kegagalan nyata, bukan dugaan.
- Tanpa paragraf motivasi; tanpa angka keramat yang tidak bisa dijelaskan.

## Uji

1. `muse skills validate ./<id>` (atau baca ulang bila tanpa CLI).
2. Jalankan satu tugas nyata yang kecil dengan skill itu dipanggil via path.
3. Kalau ada langkah yang harus ditafsirkan, perbaiki sekarang.
4. Baru dipakai rutin.

## Ubah skill yang sudah dipakai

- Satu perubahan per commit/patch, dan jelaskan blast-radius-nya ke Jun kalau skill itu dipakai
  bersama.
- Jangan mengubah skill di tengah pekerjaan supaya cocok dengan kandidat — catat dulu, selesaikan
  pekerjaan, baru ubah.
- Skill yang tidak pernah dipakai dua bulan: gabungkan atau hapus.

## Jebakan

- Skill raksasa 400 baris → tidak ada yang memuat penuh.
- Description generik ("membantu pekerjaan") → tidak pernah cocok.
- Menyimpan rahasia di dalam skill.
