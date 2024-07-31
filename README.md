# Program API autentikasi

Program api autentikasi dengan webapp sederhana untuk login,register dan get resource

## Tools

- Flask
- SQLAlchemy
- Flask-Bcrypt
- Flask-JWT-Extended
- Bootstrap
- MySQL

## Penggunaaan
- Pastikan seluruh library pada "requirements.txt" sudah terpasang
- Pastikan sudah install mysql
- Buat database baru dan user menggunakan "buatdb.sql"
- Jalankan program "app.py"
- Buka link yang tertera, jika error pastikan tambahkan /login dibelakang link
- Login jika sudah memiliki username dan password, jika tidak klik registrasi
- Registrasi username,email dan password baru. Data baru harus valid (tidak sama dengan yang ada di database atau email tidak sesuai format)
- Login menggunakan data yang teregistrasi, jika berhasil maka dapat terlihat kode akses
- Submit kode akses, jika berhasil maka terdapat gambar kucing.
