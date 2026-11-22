---
name: recon-briefs
description: "Use when writing sub-agent recon goals: STEP 0 line, per-child question, write paths, stop conditions, return shape."
---

# Menulis brief recon

Anak tidak tahu apa pun soal percakapan. Semua konteks harus ada di goal + folder target.

## Bentuk goal (urutan wajib)

```
STEP 0 (mandatory): baca ~/audit/<target>/SKILLS_<lane>.md dan <skill terkait> sebelum alat apa pun.
Kamu anak recon <n>/5 untuk <target>. Baca <folder>/BRIEF_<n>.md dan kerjakan sampai habis.
Tulis <folder>/RECON/R<n>-<topik>.md. Kembalikan hanya: wrote / answers / gaps / leads.
```

- Baris pertama selalu STEP 0. Label "skill: x" saja diabaikan.
- Brief lengkap ada di file, bukan di goal — goal cukup menunjuk.
- Sebut jumlah anak (n/5) supaya anak tahu ia bukan satu-satunya.

## Isi brief

1. Pertanyaan bernomor, tiap pertanyaan punya keputusan yang mengikutinya.
2. Path tulis yang diizinkan + larangan (jangan sentuh file anak lain, jangan edit ARCHITECTURE).
3. Kondisi berhenti: pertanyaan terjawab atau gap tercatat.
4. Bentuk output: baris pertama `# Rn`, lalu `as-of`, `egress-ip`, label `observed`/`unverified`.

## Lima peran (jangan digabung)

| n | peran | output |
|---|---|---|
| 1 | aset + ingress | RECON/R1-assets.md |
| 2 | dupe + prior art | RECON/R2-dupe.md + DUPE_GATE.md |
| 3 | auth/sesi/transport | RECON/R3-auth.md |
| 4 | sisi dalam VM (probe) | RECON/R4-cell.md |
| 5 | sink/connector/approval | RECON/R5-sinks.md |

## Setelah batch

- Baca kelima output. Jalankan ulang perintah penentu tiap klaim yang akan dipakai.
- Patch ARCHITECTURE bila anak mematahkan premis — sebelum panggilan investigasi.
- Isi COVERAGE; permukaan tanpa lane = lubang, bukan selesai.
- Anak yang tidak menghasilkan file: ulangi anak itu saja dengan goal diperbaiki.

## Jebakan

- Goal panjang berisi semua konteks → anak kehabisan ruang sebelum bekerja. Pindahkan ke brief.
- Anak diberi izin menulis bebas → dua anak menimpa file yang sama.
- Ringkasan anak dipercaya apa adanya → kirim laporan dengan klaim yang tidak pernah jalan.
