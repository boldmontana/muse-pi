---
name: bounty-cycle
description: "Use when starting or resuming a bug bounty target: phase spine, artifacts per phase, recon-only delegation, closure rules."
---

# Bounty cycle

Satu target = satu folder `~/audit/<target>/`. Log di `~/bounty-log/`.

## Fase (tidak dilompati)

1. **SCOPE** — baca halaman program. Kutip verbatim ke `SCOPE_IN.md`, `SCOPE_OUT.md`,
   `PROGRAM_RULES.md`. Ambil tabel severity program apa adanya. Belum ada kerja sebelum ini ada.
2. **RECON — hanya fase ini yang memakai agent.** Lima brief, satu batch, dari
   `agents/templates/recon-child.md` (di kit) dengan lane terisi. Anak menulis `RECON/R<n>-*.md`.
   Tutup dengan `RECON_REPORT.md` + daftar permukaan belum tertutup.
3. **MAPPING / ARCHITECTURE** — parent. Tulis premis yang bisa dipatahkan, ledger lane, hipotesis
   ber-header (aktor, impact-row, kutipan lawan, cek dupe bertanggal).
4. **INVESTIGATION** — parent, per lane, urut nilai/biaya. Satu variabel per percobaan; tiga percobaan
   sebelum INVALID; LESSON satu baris per kegagalan. Positif → kontrol → perluas.
5. **REPORT** — judge (`triage-gate`), pack (`evidence-hygiene`, `report-writer`), handoff ke Jun.

## Aturan delegasi (keras)

- Spawn hanya di fase 2. Setelah recon, parent sendiri.
- Satu pengecualian: satu debugger bila lane mentok dan Jun setuju.
- Goal anak dibuka `STEP 0 (mandatory): baca <path skill>` lalu path brief.
- Anak menulis file, bukan bercerita. Ringkasan anak = klaim; perintah penentu dijalankan ulang.

## Ledger

`WAVE_LEDGER.md` dibuka sebelum panggilan investigasi pertama: lane | kelas | permukaan | status |
kriteria keluar | artefak. Status: OPEN/RUNNING/LEAD/DONE/INVALID/DISPROVEN/BLOCKED/PARKED/SENT.
Update di sesi yang sama. 25 panggilan tanpa update = tulis satu baris checkpoint.

## Dupe

`DUPE_GATE.md` bertanggal di RECON dan sekali lagi sebelum kirim. Temuan publik yang mekanismenya
masih hidup memblokir kandidat; yang penting adalah sibling yang belum diperbaiki.

## Tutup target

Hanya: blocker operasional (Jun putuskan) · semua permukaan INVALID beralasan · scope habis.
"Kurang produktif" bukan alasan. Satu baris status di `~/bounty-log/targets-status.md` hari itu.

## Jebakan

- Recon dianggap selesai padahal belum ada daftar permukaan terbuka.
- Ledger dibuka setelah investigasi jalan (meter tidak sah).
- Anak dipakai lagi di investigasi "karena cepat" — boleh, tapi catat sebagai pengecualian.
- Kutipan scope diparafrase; aturan yang tidak ada jadi tercipta.
