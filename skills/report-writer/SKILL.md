---
name: report-writer
description: "Use when drafting any bounty report: identity gate, platform shape, claim verification, pack contents, and what must never be claimed."
---

# Report writer

Laporan dibaca orang yang lelah. Buat satu kali baca cukup.

## Gerbang sebelum menulis

1. **Identitas.** Tanya Jun: bold / jex / pismol / junnot. Satu vendor = satu identitas, tanpa default.
2. **Scope.** Kutip baris scope yang memuat aset ini, verbatim. Kalau ambigu, tulis sebagai catatan
   scope di dalam laporan — jangan self-close.
3. **Severity.** Pakai tabel program. Web2: model platform (HackerOne CVSS, Bugcrowd VRT, Intigriti
   re-rate, YesWeHack CVSS+override). Web3: klasifikasi program, baca baris impact verbatim.
   Cross-check CVSS 3.1; kalau beda lebih dari satu tingkat, uji ulang asumsinya.
4. **Klaim.** Setiap klaim dampak punya artefak. Yang belum punya ditandai LEAD, bukan dikarang.
5. **Dupe.** Gate bertanggal hari ini.

## Kerangka (bahasa Inggris)

Title · Asset/endpoint · Severity + CVSS · Summary (3–5 kalimat) · Affected (akun A/B, build, waktu,
egress IP) · Steps (bernomor, dari keadaan bersih) · Observed (output mentah) · Control · Impact
(dikaitkan ke baris program) · Inadvertent access · Counter-quote + jawabannya · Dupe check ·
Suggested fix · Attachments + sha256.

## Pack

- Folder `pack/` berisi laporan, bukti, README bukti, `JUDGE.md`, hash.
- Jalankan ulang satu perintah penentu sendiri, tempel output mentahnya.
- Umur pack ≤72 jam: kirim atau parkir dengan tanggal review.
- Handoff ke Jun: subject, ringkasan 3 baris, path pack, identitas usulan. Jun yang mengirim.

## Yang tidak boleh diklaim

- "Semua user terdampak" tanpa hitungan.
- "Kritis" tanpa rantai penuh.
- "Sudah diperbaiki" tanpa A/B build.
- "Tidak ada jalur pemulihan" tanpa mencoba jalur pemulihan.
- Dampak yang tidak ada di tabel program, kecuali ditandai sebagai usulan klasifikasi.

## Jebakan

- Parafrase scope → aturan yang tidak ada.
- Menyembunyikan keterbatasan → triager menemukannya sendiri dan menurunkan semuanya.
- Menempel nilai rahasia utuh.
- Menulis kesimpulan di awal lalu menyusun bukti agar cocok.
