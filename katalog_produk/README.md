# 🛒 TokoKita – Website Katalog Produk Sederhana
**Tugas Praktikum Pemrograman Web | Framework Django**

---

## 📋 Deskripsi Proyek

Website katalog produk sederhana yang dibangun menggunakan framework **Django (Python)**.
Website ini menampilkan daftar produk, detail produk, dan halaman kontak.
Data produk disimpan secara **hardcoded** di `views.py` (tidak menggunakan database).

---

## 📁 Struktur Folder Proyek

```
katalog_produk/
│
├── manage.py                        # File manajemen Django
│
├── katalog_produk/                  # Folder konfigurasi proyek
│   ├── __init__.py
│   ├── settings.py                  # Pengaturan Django
│   ├── urls.py                      # URL utama proyek
│   └── wsgi.py
│
└── katalog/                         # Folder aplikasi katalog
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py                     # Logic tampilan & data produk
    ├── urls.py                      # URL routing app katalog
    └── templates/
        └── katalog/
            ├── base.html            # Template dasar (navbar, footer, CSS)
            ├── homepage.html        # Halaman Beranda (/)
            ├── daftar_produk.html   # Halaman Daftar Produk (/produk/)
            ├── detail_produk.html   # Halaman Detail Produk (/produk/<id>/)
            ├── kontak.html          # Halaman Kontak (/kontak/)
            └── produk_tidak_ditemukan.html
```

---

## 🗺️ Daftar URL (Routing)

| URL | Nama View | Keterangan |
|-----|-----------|------------|
| `/` | `homepage` | Halaman Beranda |
| `/produk/` | `daftar_produk` | Daftar semua produk |
| `/produk/<id>/` | `detail_produk` | Detail produk berdasarkan ID |
| `/kontak/` | `kontak` | Halaman informasi kontak |

---

## 🚀 Cara Menjalankan Proyek

### Langkah 1 – Pastikan Python sudah terinstall
```bash
python --version
# Harus Python 3.8 ke atas
```

### Langkah 2 – Buat Virtual Environment
```bash
python -m venv venv
```

### Langkah 3 – Aktifkan Virtual Environment

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Mac / Linux:**
```bash
source venv/bin/activate
```

### Langkah 4 – Install Django
```bash
pip install django
```

### Langkah 5 – Masuk ke folder proyek
```bash
cd katalog_produk
```

### Langkah 6 – Jalankan migrasi database (wajib meski tidak pakai DB)
```bash
python manage.py migrate
```

### Langkah 7 – Jalankan Development Server
```bash
python manage.py runserver
```

### Langkah 8 – Buka di Browser
Buka browser dan akses: **http://127.0.0.1:8000/**

---

## 📸 Halaman yang Perlu Di-screenshot untuk Laporan

| No | Halaman | URL | Keterangan |
|----|---------|-----|------------|
| 1 | Beranda (Homepage) | `http://127.0.0.1:8000/` | Halaman selamat datang |
| 2 | Daftar Produk | `http://127.0.0.1:8000/produk/` | Grid semua produk |
| 3 | Detail Produk 1 | `http://127.0.0.1:8000/produk/1/` | Detail Laptop ASUS |
| 4 | Detail Produk 2 | `http://127.0.0.1:8000/produk/2/` | Detail Samsung Galaxy |
| 5 | Detail Produk 3 | `http://127.0.0.1:8000/produk/3/` | Detail Tas Eiger |
| 6 | Halaman Kontak | `http://127.0.0.1:8000/kontak/` | Informasi kontak |

---

## 💡 Teknologi yang Digunakan

- **Python 3.x** – Bahasa pemrograman
- **Django 4.x / 5.x** – Web framework
- **HTML5 + CSS3** – Tampilan antarmuka
- **SQLite** – Database bawaan Django (hanya untuk sesi, tidak digunakan aktif)

---

## 👤 Informasi Pengembang

- **Nama**: [Isi Nama Anda]
- **NIM**: [Isi NIM Anda]
- **Mata Kuliah**: Pemrograman Web
- **Dosen**: [Isi Nama Dosen]
- **Tahun**: 2024
