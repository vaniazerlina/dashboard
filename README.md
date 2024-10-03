E-commerce Dashboard 🛍️
Dashboard untuk menganalisis dan menampilkan data dari E-Commerce menggunakan Streamlit.

## Fitur
- Menampilkan data visualisasi berdasarkan koleksi Dicoding.
- Analisis interaktif menggunakan berbagai visualisasi.
- Dashboard responsif yang mudah digunakan.

## Persyaratan
- Python 3.9
- Anaconda (untuk pengaturan environment opsional)
- Streamlit

## Setup Environment - Anaconda

1. Buat environment baru dan aktifkan:
    ```bash
    conda create --name main-ds python=3.9
    conda activate main-ds
    ```

2. Instal semua dependensi dari file `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Setup Environment - Shell/Terminal (Opsional tanpa Anaconda)

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

3. Instal semua dependensi dari file `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

## Menjalankan Aplikasi Streamlit

Setelah semua dependensi terpasang, jalankan aplikasi Streamlit dengan perintah berikut:

```bash
streamlit run dashboard.py
