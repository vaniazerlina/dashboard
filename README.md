# E-commerce Dashboard 🛍️

Dashboard ini dibuat untuk menganalisis dan menampilkan data dari E-commerce menggunakan Streamlit.

## Fitur
- Menampilkan berbagai visualisasi data yang interaktif.
- Analisis yang mudah diakses dan digunakan oleh pengguna.
- Dashboard responsif yang menyesuaikan dengan ukuran layar perangkat.

## Persyaratan
- Python 3.9
- Anaconda (opsional untuk pengaturan environment)
- Streamlit

## Setup Environment - Anaconda (Opsional)

1. Buat environment baru dan aktifkan:
    ```bash
    conda create --name main-ds python=3.9
    conda activate main-ds
    ```

2. Instal semua dependensi yang dibutuhkan:
    ```bash
    pip install -r requirements.txt
    ```

## Setup Environment - Shell/Terminal

1. Buat direktori proyek:
    ```bash
    mkdir dashboard
    cd dashboard
    ```

2. Instal dan aktifkan pipenv:
    ```bash
    pipenv install
    pipenv shell
    ```

3. Instal semua dependensi yang dibutuhkan:
    ```bash
    pip install -r requirements.txt
    ```

## Menjalankan Aplikasi Streamlit

Setelah semua dependensi terpasang, jalankan aplikasi Streamlit dengan perintah berikut:

```bash
streamlit run dashboard.py
