---
name: triage-gate
description: "Use when deciding whether a candidate is worth packing: three Phase-0 quotes, four questions, one verdict file."
---

# Triage gate

Kandidat yang lolos belum tentu temuan. Verdict ditulis sebagai file di folder pack (`JUDGE.md`),
bukan kalimat di chat.

## Phase 0 — tiga kutipan verbatim

1. **Konsekuensi** — baris tabel program yang dibayar oleh kandidat ini.
2. **Kepemilikan** — baris scope yang menyatakan aset ini milik vendor.
3. **Niat** — teks vendor (docs, UI, blog) yang menyatakan perilaku ini diinginkan atau tidak.

Plus satu **kutipan lawan**: kalimat vendor yang paling bisa mematikan kandidat. Kalau kutipan lawan
mematikan dan tidak ada jawaban, kandidat mati di situ — itu gunanya.

## Empat pertanyaan

1. Kontrolnya benar-benar pecah, atau perilakunya terdokumentasi?
2. Kelas interaksi victim jujur? (0 / 0.5 / 1 / 2 / >2 klik; "paste ini ke chat" = paling jauh 1 klik)
3. Rantai lolos klausul "realistically exploitable"?
4. Sudah publik? (gate dupe bertanggal hari ini; kalau ya, sebut referensinya dan delta-nya)

## Verdict

`HOLD` (satu artefak kurang, sebutkan perintahnya) · `KILL` (sebut apa yang bisa menghidupkan) ·
`RAISE` (naikkan kelas dan sebut bukti tambahan yang harus ada sebelum pack).

## Kalibrasi

- Turunkan kalau dampaknya terbatas, victim menyakiti diri sendiri, precondition tidak masuk akal, atau
  mitigasi efektif.
- Jangan turunkan karena "tidak ada dana berpindah" — authz dan kebocoran dinilai dari yang terbuka.
- Impact-row yang tidak ada di tabel = LEAD + eskalasi ke Jun, jangan bikin PoC dulu.

## Jebakan

- Verdict ditulis dari estimasi sendiri tanpa kutipan → opini.
- "Downgrade lalu kirim" tanpa memutuskan HOLD/KILL/RAISE.
- Gate dupe internal (antar kandidat kita) dianggap gate program.
