# Tugas Kelompok PBP

## Kelompok PBP E11:

- Mohammad Ferry Husnil Arif (2106709112)
- Muhammad Naufal Zaky Alsar (2106752041)
- Vander Gerald Sukandi
- Muhammad Rayhan Denel (2106752161)
- Bimo Priyohutomo (2106708444)
- Aushaaf Fadhilah Azzah (2106630063)

## Tautan : https://saku-in.herokuapp.com/

## Cerita Aplikasi:

Website ini dirancang untuk membantu orang untuk mengelola keuangan. Website ini memiliki beberapa fitur yaitu Dompet (untuk informasi keuangan terkini), Forum pengeluaran/pemasukan, Untuk mengkonversi satu mata uang ke uang mata lainnya (yang menentukan nilai kurs adalah admin), Berita Finansial Berita finansial yang diberikan oleh admin ada kategori juga untuk berita, Donasi Pengguna bisa mendonasikan sejumlah uangnya dan terintegrasi ke dompet kita (kalau uangnya kurang bakal dikasih warning)

## Module:

- Dompet

Modul yang menampilkan keuangan pengguna saat ini. Pengeluaran/pemasukan Input nominal pengeluaran dan pemasukan dalam dompet berdasarkan tempat penyimpanan uang.

- Forum

Forum diskusi antara user dan dapat mereply forum

- Berita Finansial

Berita finansial yang diberikan oleh admin ada kategori juga untuk berita

- Kurs

Untuk mengkonversi satu mata uang ke uang mata lainnya

- Donasi

Pengguna bisa mendonasikan sejumlah uangnya dan terintegrasi ke dompet kita (kalau uangnya kurang bakal dikasih warning). Yang buka donasi user dan ada deskripsi.

## Role:

- Guest (User yang belum log in akses yang dipunya adalah kurs dan membaca berita)
- User (Pengguna yang sudah terautentifikasi bisa mengakses hampir semua fitur kecuali membuat berita dan menghapus donasi user lain, menghapus forum dan komen user lain, dan membuat berita dan menghapus berita)
- Admin (Pengguna yang mempunyai akses ke semua fitur seperti : dapat menghapus dan menambah berita, menghapus forum dan komen, menghapus donasi)
