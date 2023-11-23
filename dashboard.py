import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk membaca data
def read_data():
    customers_df = pd.read_csv('customers_dataset.csv', delimiter=',')
    geolocation_df = pd.read_csv('geolocation_dataset.csv', delimiter=';')
    order_items_df = pd.read_csv('order_items_dataset.csv', delimiter=',')
    order_payments_df = pd.read_csv('order_payments_dataset.csv', delimiter=',')
    order_reviews_df = pd.read_csv('order_reviews_dataset.csv', delimiter=',')

    # Perubahan disini: Ubah format kolom tanggal
    orders_df = pd.read_csv('orders_dataset.csv', delimiter=',', 
                            parse_dates=['order_purchase_timestamp', 'order_approved_at', 
                                         'order_delivered_carrier_date', 'order_delivered_customer_date', 
                                         'order_estimated_delivery_date'])

    # Perubahan disini: Set kolom 'order_purchase_timestamp' sebagai indeks
    orders_df.set_index('order_purchase_timestamp', inplace=True)

    product_category_df = pd.read_csv('product_category_name_translation.csv', delimiter=',')
    products_df = pd.read_csv('products_dataset.csv', delimiter=',')
    sellers_df = pd.read_csv('sellers_dataset.csv', delimiter=',')

    return {
        'customers': customers_df,
        'geolocation': geolocation_df,
        'order_items': order_items_df,
        'order_payments': order_payments_df,
        'order_reviews': order_reviews_df,
        'orders': orders_df,
        'product_category': product_category_df,
        'products': products_df,
        'sellers': sellers_df
    }

def show_graph_by_month_and_year(orders_df, selected_month, selected_year):
    # Filter data berdasarkan rentang waktu yang lebih luas
    start_date = f"{selected_year}-{selected_month:02d}-01"
    end_date = f"{selected_year}-{selected_month + 1:02d}-01" if selected_month < 12 else f"{selected_year + 1}-01-01"
    
    filtered_data = orders_df[(orders_df.index >= start_date) & (orders_df.index < end_date)]

    # Sort filtered data berdasarkan tanggal
    filtered_data = filtered_data.sort_index()

    # Check if the filtered data is not empty
    if not filtered_data.empty:
        # Buat plot/grafik (contoh: jumlah pesanan per hari)
        fig, ax = plt.subplots(figsize=(15, 8))
        sns.countplot(x=filtered_data.index.day, palette='viridis', ax=ax, label='Order Purchase')

        ax.set_title(f'Orders Timeline in {selected_month}/{selected_year}')
        ax.set_xlabel('Day of Month')
        ax.set_ylabel('Number of Orders')
        ax.legend()
        st.pyplot(fig)

        # Pemecah untuk membantu pemantauan
        st.write("Selected Month:", selected_month)
        st.write("Selected Year:", selected_year)
        st.write("Filtered Data (Sorted by Date):")
        st.write(filtered_data)
    else:
        st.warning(f"No orders found for {selected_month}/{selected_year}")

# Fungsi untuk menampilkan jumlah pengguna aktif berdasarkan state
def show_active_users_by_state(customers_df, selected_state):
    # Filter data berdasarkan state yang dipilih
    filtered_data = customers_df[customers_df['customer_state'] == selected_state]

    # Hitung jumlah pengguna aktif
    active_users_count = len(filtered_data)

    # Menampilkan jumlah pengguna aktif dalam sebuah kotak
    st.info(f"**Active Users in {selected_state}:** {active_users_count} 👥")

# Fungsi untuk menampilkan jumlah penjual per state
def show_sellers_per_state(sellers_df, selected_state):
    # Filter data penjual berdasarkan state yang dipilih
    filtered_data = sellers_df[sellers_df['seller_state'] == selected_state]

    # Hitung jumlah penjual per state
    sellers_count = len(filtered_data)

    # Menampilkan jumlah penjual per state dalam sebuah kotak
    st.info(f"**Number of Sellers in {selected_state}:** {sellers_count} 👥")


# Fungsi utama
def run():
    st.set_page_config(
        page_title="E-commerce Dashboard",
        page_icon="🛍️",
    )

    st.write("# Welcome to E-commerce Dashboard! 🛍️")

    # Membaca semua file CSV
    data = read_data()

    # Sidebar untuk pemilihan bulan dan tahun
    st.sidebar.header("Filter by Month and Year")
    selected_month = st.sidebar.slider("Select Month", 1, 12, 1)
    selected_year = st.sidebar.slider("Select Year", int(data['orders'].index.year.min()),
                                      int(data['orders'].index.year.max()), 2023)

    # Menampilkan grafik sesuai dengan bulan dan tahun yang dipilih
    show_graph_by_month_and_year(data['orders'], selected_month, selected_year)

    # Sidebar untuk pemilihan state pelanggan
    st.sidebar.header("Filter by Customer State")
    
    # Gabungkan customers_df dan geolocation_df berdasarkan customer_zip_code_prefix dan geolocation_zip_code_prefix
    merged_customers_geolocation = pd.merge(data['customers'], data['geolocation'],
                                            left_on='customer_zip_code_prefix', right_on='geolocation_zip_code_prefix')
    
    # Ambil data unik geolocation_state untuk dropdown
    unique_customer_states = merged_customers_geolocation['geolocation_state'].unique()
    
    # Dropdown untuk memilih geolocation_state pelanggan
    selected_customer_state = st.sidebar.selectbox("Select Customer State", unique_customer_states)

    # Menampilkan jumlah pengguna aktif berdasarkan state yang dipilih
    show_active_users_by_state(merged_customers_geolocation, selected_customer_state)

    # Sidebar untuk pemilihan state penjual
    st.sidebar.header("Filter by Seller State")
    
    # Gabungkan sellers_df dan geolocation_df berdasarkan seller_zip_code_prefix dan geolocation_zip_code_prefix
    merged_sellers_geolocation = pd.merge(data['sellers'], data['geolocation'],
                                           left_on='seller_zip_code_prefix', right_on='geolocation_zip_code_prefix')
    
    # Ambil data unik geolocation_state untuk dropdown penjual
    unique_seller_states = merged_sellers_geolocation['geolocation_state'].unique()
    
    # Dropdown untuk memilih geolocation_state penjual
    selected_seller_state = st.sidebar.selectbox("Select Seller State", unique_seller_states)

    # Menampilkan jumlah penjual per state
    show_sellers_per_state(merged_sellers_geolocation, selected_seller_state)


if __name__ == "__main__":
    run()
