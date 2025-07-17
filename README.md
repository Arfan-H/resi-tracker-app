# resi-tracker-app\
Berikut adalah contoh isi `README.md` untuk repositori GitHub berdasarkan file `main.py` yang kamu unggah:

---

# 📦 Informasi Barang - Sistem Pelacakan & Pengiriman Paket

Aplikasi desktop berbasis Python (Tkinter) untuk **melacak, mengelola, dan memantau pengiriman paket** antar cabang (Jakarta & Surabaya) dengan fitur login, sorting, dan pencarian resi menggunakan algoritma BFS.

## 🚀 Fitur Utama

* 🔎 **Pelacakan Resi**
  Cari dan tampilkan informasi paket dari database CSV menggunakan pencarian BFS.

* 🗃️ **Pengelolaan Pengiriman**
  Input data pengiriman baru, termasuk pengirim, penerima, alamat, jenis, dan berat paket. Nomor resi akan digenerate otomatis.

* 📤📥 **Pemindahan Data Paket**
  Kirim data paket ke cabang tujuan, dengan konfirmasi pengguna.

* 🔐 **Autentikasi Login**
  Akses halaman admin/pengiriman dengan login berdasarkan file CSV pengguna.

* 📊 **Sorting Data**
  Urutkan paket berdasarkan prioritas (`Prioritas`, `Reguler`, `Retur`) dan nomor resi menggunakan algoritma **Shell Sort**.

* 🌐 **Antarmuka Grafis**
  Menggunakan `tkinter` dengan layout dan ikon kustom (berkas gambar disimpan di folder `images/`).

## 🗂️ Struktur Data & Algoritma

* `LinkedList`
  Digunakan untuk menyimpan dan mengecek duplikasi nomor resi.

* `Shell Sort`
  Untuk mengurutkan daftar pengiriman berdasarkan prioritas dan nomor resi.

* `BFS (Breadth First Search)`
  Untuk pencarian data berdasarkan nomor resi secara efisien.

## 📁 Dataset & File

* Folder `database/` berisi:

  * `Jakarta/package_in.csv`
  * `Jakarta/package_out.csv`
  * `Surabaya/package_in.csv`
  * `Surabaya/package_out.csv`
  * `User_Auth.csv`

* Folder `images/` berisi elemen visual antarmuka aplikasi (UI).

## 💻 Cara Menjalankan

```bash
python main.py
```

> Pastikan semua file CSV dan folder gambar berada di jalur yang benar sesuai di kode.

## 📚 Sumber & Referensi

* Visual antarmuka dirancang menggunakan `tkinter` & `Pillow`
* Data dibaca menggunakan pustaka `csv` Python
* Inspirasi dan data dummy dapat diisi sendiri atau dari hasil scraping/simulasi layanan ekspedisi

---

