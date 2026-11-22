---
name: evidence-hygiene
description: "Use when collecting proof for a candidate: folder layout, timestamps, controls, secret masking, foreign-data cleanup."
---

# Evidence hygiene

Bukti yang tidak bisa dibaca ulang bukan bukti.

## Struktur

`~/audit/<target>/evidence/<lane>/` :
- `README.md` dari template: apa, kapan (UTC), egress IP, akun, build, perintah, harapan vs hasil,
  kontrol, **apa yang belum dibuktikan**, file + sha256.
- `raw/` output mentah (`curl -D`, dump, transcript).
- `shots/` screenshot berurutan, nama berisi nomor langkah.

## Aturan

- Timestamp UTC di setiap artefak; jam lokal hanya sebagai catatan tambahan.
- Setiap positif punya kontrol yang hanya berbeda di variabel uji. Tanpa kontrol, positif belum jadi.
- Rahasia: prefix + panjang + sha256 12 karakter pertama. Nilai utuh hanya kalau memang perlu dibaca
  triager, dan itu ditandai.
- Nama file tanpa spasi, tanpa karakter aneh.
- `sha256sum` untuk semua lampiran sebelum pack; daftar hash masuk README.
- Hapus bukti yang tidak dipakai; folder pack hanya berisi yang mendukung klaim.

## Data pihak lain (program yang mensyaratkan)

1. Ambil sampel terbatas (≤20 objek), catat id + ringkasan isi.
2. Hentikan akses begitu cukup.
3. Hapus salinan dari mesin kita, sisakan hash + screenshot teredaksi.
4. Tulis bagian "inadvertent access" di README dan di laporan: akun/id, jendela waktu, "salinan dihapus
   <tanggal>".

## Jebakan

- Screenshot tanpa URL bar → tidak menunjukkan capability mana yang berlaku.
- Dump badan respons tanpa header → status dan auth tidak terbukti.
- Kontrol dijalankan belakangan setelah state berubah → kontrol tidak lagi sebanding.
- Menempel token utuh di README → satu file bocor, semua bocor.
