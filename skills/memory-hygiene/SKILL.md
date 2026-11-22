---
name: memory-hygiene
description: "Use when Memory.md grows long or stale: what belongs in memory, what moves to a skill, how to prune with a backup."
---

# Memory hygiene

Memory ikut konteks setiap turn. Memory yang bengkak memperlambat dan menyesatkan.

## Yang layak tinggal

- Fakta tetap tentang Jun dan lingkungannya.
- Preferensi yang berlaku tiap sesi.
- Jebakan yang sudah terbukti berulang.

## Yang harus keluar

- Status pekerjaan dan tanggal ("target X sedang di lane 4") → `targets-status.md`.
- Prosedur panjang → skill, sisakan satu baris penunjuk.
- Fakta yang sudah tidak benar → hapus, jangan ditimpa.
- Catatan hasil ("pernah nihil") → boleh satu baris, tapi jangan dijadikan gerbang.

## Cara menulis

- Deklaratif: "Jun pakai Bahasa Indonesia", bukan "Selalu jawab Bahasa Indonesia".
- Satu fakta per baris. Tanpa basa-basi, tanpa tanggal kecuali memang bertanggal.
- Nama rahasia disebut, nilainya tidak.

## Prosedur pangkas

1. Backup `Memory.md` ke `state/backup/<tanggal>/memory.md`.
2. Kelompokkan baris: tetap / pindah ke skill / hapus.
3. Tulis ulang padat; target ≤60 baris.
4. Baca ulang di app dan bandingkan; catat di `state/CHANGELOG.md`.
5. Uji satu fakta acak di percakapan baru — kalau hilang, baru saja kamu memangkas terlalu dalam.

## Jebakan

- Menghapus fakta yang masih dipakai karena terlihat "tidak penting".
- Menyalin seluruh skill ke Memory.
- Pangkas tanpa backup, lalu reset juga — hilang semua.
