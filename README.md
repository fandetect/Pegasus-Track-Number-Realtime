# 🛰️ Pegasus Track Number Realtime

Script Python untuk melacak **lokasi nomor HP secara realtime**, aman dari modifikasi, dan hanya bisa dijalankan dengan **kata aktivasi** tertentu. Fokus utama untuk nomor-nomor di **Indonesia** 🇮🇩.

---

## 🧩 Apa Yang Dilakukan?
- 🟢 Minta input nomor telepon di awal
- 🛡️ Verifikasi kata aktivasi (`sobri`)
- 🌍 Lacak:
  - Negara
  - Operator telekomunikasi
  - Latitude & Longitude
  - Zona waktu
  - Mata uang
  - Bendera negara
  - Link ke peta (OpenStreetMap)
- ❌ Script langsung **error jika dimodifikasi**

---

## 🔐 Fitur Keamanan
- Anti-modifikasi: File ini dilindungi, jika kamu ubah, langsung error
- Aktivasi wajib: Kata sandi `sobri` diperlukan sebelum jalan
- Validasi input: Hanya format nomor telepon yang sah diterima

---

## 📥 Contoh Input
```bash
$ python3 pegasus-track-number-realtime.py
Masukkan kata aktivasi: sobri
Masukkan nomor telepon: +628123456789
```

## 📤 Contoh Output
```bash
Country Name => Indonesia
-------------------------

Telecom Company Name => Telkomsel
-------------------------------

Latitude: -6.200000
Longitude: 106.816666
Currency: Indonesian Rupiah (Rp)
Timezone: Asia/Jakarta
Flag: 🇮🇩
Map: https://www.openstreetmap.org/?lat=-6.2&lon=106.816666
```

## ⚙️ Teknologi yang Digunakan
- Python 3
- OpenCage API
- OpenStreetMap
- Modul pelindung anti-modifikasi dan validasi input

## 🚀 Cara Pakai

### Persiapan
Ada dua cara untuk melakukan setup:

1. **Setup Otomatis** (Direkomendasikan):
   ```bash
   # Windows
   python setup-env.py
   
   # Linux/macOS
   python3 setup-env.py
   ```
   Script ini akan memeriksa dan menginstal semua dependensi yang dibutuhkan, serta membantu konfigurasi API key.

2. **Setup Manual**:
   ```bash
   # Windows
   pip install -r requirements.txt
   
   # Linux/macOS
   pip3 install -r requirements.txt
   ```

### Menjalankan Aplikasi
```bash
# Windows
python pegasus-track-number-realtime.py

# Linux/macOS
python3 pegasus-track-number-realtime.py
```

### Untuk Pengembang (Jika Menggunakan VS Code)
Jika melihat error Pylance tentang "Import could not be resolved", gunakan salah satu solusi berikut:

1. Restart VS Code setelah menginstal paket
2. File `pyrightconfig.json` sudah disediakan untuk menonaktifkan peringatan impor

## 👤 Author
- Letda Kes dr. Sobri, S.Kom
- 📧 Email: muhammadsobrimaulana31@gmail.com
- 🌐 GitHub: https://github.com/sobri3195

## ❤️ Dukung Proyek Ini
Kamu bisa support pengembangan tools ini di:
- 🔗 https://lynk.id/muhsobrimaulana

## ⚠️ Peringatan Penting
- 🚫 Jangan ubah file ini, script akan error otomatis
- ✅ Gunakan hanya untuk tujuan edukasi & keamanan pribadi
- 🔒 Dilarang keras menyebarkan ulang tanpa izin

## 📜 Lisensi
Hak Cipta © 2025 Letda Kes dr. Sobri, S.Kom
Lisensi Khusus – Tidak untuk distribusi publik tanpa izin resmi. 