---
name: daily-ops
description: "Use when running the normal day: morning brief, decision queue, closing line, scheduled jobs, approval discipline."
---

# Daily ops

Hari normal bukan hari bounty. Tetap punya bentuk.

## Pagi (≤5 baris)

1. Kalender hari ini — hanya yang butuh persiapan.
2. Keputusan yang menunggu dari Jun (maksimal 3, yang paling tua di atas).
3. Satu prioritas hari ini, dengan alasan satu baris.

Bukan ceramah, bukan daftar semua hal.

## Siang

- Kerjakan prioritas. Kalau mentok: catat blocker, lanjut yang lain, kumpulkan pertanyaan.
- Tugas yang butuh approval: siapkan lengkap (isi, penerima, biaya), minta approval sekali, jangan
  menunggu sambil menganggur.
- Baca boleh tanpa approval; tulis ke layanan nyata tidak.

## Sore

- Satu baris apa yang berubah.
- Satu baris apa yang menunggu besok.
- Satu baris apa yang Jun perlu putuskan.

## Jadwal

- Rutin yang sudah dua kali dikerjakan manual → jadwal di `agents/cron/`.
- Jadwal yang tidak pernah menghasilkan sesuatu dalam dua minggu → hapus, jangan dibiarkan.
- Job terjadwal melapor hanya kalau ada yang baru; "tidak ada perubahan" cukup satu baris.

## Approval: jujur soal status

- "Draf siap" ≠ "terkirim". Setelah approval, cek Activity log sebelum bilang terkirim.
- Kalau approval ditolak, jangan ulangi otomatis; sebut alasan yang terlihat.
- Biaya: sebut estimasi sebelum, dan konfirmasi setelah.

## Jebakan

- Brief pagi jadi laporan panjang → tidak dibaca.
- Mengumpulkan pertanyaan tapi lupa menyampaikannya.
- Menyelesaikan tugas dengan menulis ke layanan orang lain tanpa approval.
