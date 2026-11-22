---
name: report-delivery
description: "Use when a report is ready to leave: MD + PDF pair, Gmail send to the vendor address, approval, and the sent-marker. Send is the last step, never the first."
---

# Report delivery (MD + PDF, kirim via Gmail)

Laporan hanya keluar kalau Jun sudah memilih identitas dan memberi GO. Kamu yang menyiapkan, kamu yang
mengirim setelah approval; kalau gagal, katakan gagal — jangan bilang terkirim.

## Bentuk kiriman (wajib dua file)

- Satu laporan = satu slug. Selalu dua file dengan basename sama:
  `<slug>.md` (sumber kebenaran) dan `<slug>.pdf` (turunan, jangan diedit tangan).
- Bahasa Inggris. Nama file ASCII: `lowercase-with-dash.md/.pdf`, tanpa spasi.
- Folder: `~/bounty/evidence/<target>/<YYYY-MM-DD>-<slug>/`. Isi juga `README.md` bukti + `JUDGE.md`.
- PDF dibuat dari MD, bukan dikarang terpisah. Isi PDF harus sama dengan MD.

## Membuat PDF (tool yang ada di VM)

```
python3 ~/skills/report-delivery/md2html.py <slug>.md <slug>.html
soffice --headless --convert-to pdf --outdir . <slug>.html
```

Verifikasi sebelum lanjut:
- `file <slug>.pdf` → PDF, ukuran > 3 KB, dan `head -c 5 <slug>.pdf` = `%PDF-`.
- Buka ulang MD: setiap section report-writer ada; tidak ada placeholder `TBD`.
- sha256 kedua file dicatat di README bukti.

## Penerima dan subjek

- Penerima: alamat security vendor yang tertulis di `PROGRAM_RULES.md`. Jangan menebak, jangan pakai
  alamat dari ingatan. Kalau program pakai form, kiriman Gmail tetap dibuat sebagai arsip.
- Subjek: `[<program>] <Severity>: <title> — <asset>`. Tanpa emoji, tanpa "URGENT" kecuali Critical.
- Body: 5–8 baris — satu kalimat temuan, satu kalimat dampak, daftar 2 lampiran, catatan bahwa detail
  ada di lampiran, tanda tangan identitas yang dipilih Jun. Jangan menempel PoC di body kalau ada lampiran.

## Urutan kirim (jangan dibalik)

1. Identitas sudah dipilih Jun untuk vendor ini, dan GO tertulis.
2. `JUDGE.md` ada dan verdict-nya bukan KILL.
3. Dupe gate bertanggal hari ini ada di folder.
4. Redaksi: tidak ada private key, mnemonic, token, cookie sesi, atau data user nyata.
5. Dua lampiran ada dan non-zero; PDF lolos cek di atas.
6. Susun email, pasang dua lampiran, baca ulang subjek + penerima + nama lampiran.
7. Kirim lewat connector Gmail. Kalau Sentinel memunculkan approval, tunggu; jangan kirim dobel.
8. Setelah terkirim: catat `SENT_<YYYY-MM-DD>_<message-id>.md` di folder (message-id dari Gmail),
   tambahkan `ack-watch: <date +3 hari>` di `~/bounty-log/submission-queue.md` kalau ada.
9. Satu vendor satu email per 24 jam; dua temuan ke vendor yang sama = kirim terpisah, bukan satu bundle.

## Yang membatalkan kiriman

- Identitas belum dipilih, atau vendor sudah pernah dikirimi dengan identitas lain.
- Angka/hadiah di body tidak cocok dengan tabel program.
- Lampiran cuma MD (tanpa PDF), atau PDF kosong/rusak.
- Ada klaim tanpa bukti di dalam laporan.
- Penerima hasil karangan.

## Setelah kirim

Laporkan ke Jun satu baris: penerima, subjek, message-id, dua path lampiran. Klaim "terkirim" hanya
sah kalau ada message-id.
