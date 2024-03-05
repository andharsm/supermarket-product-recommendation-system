# -*- coding: utf-8 -*-
"""Product Recomendation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ceIfR5rrFIP46nFtQUl---rl9W498R8e

# Sisten Rekomendasi Produk

# Import Library
"""

import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

"""# Load Data

Load data dari kaggle: [Supermarket dataset for predictive marketing 2023](https://www.kaggle.com/datasets/hunter0007/ecommerce-dataset-for-predictive-marketing-2023/data)
"""

# Define your Kaggle API credentials
kaggle_credentials = {
    "username": "andharsm",
    "key": "aa01adb9e93691614d246ac084458990"
}

# Save the credentials to a file named kaggle.json
with open('/content/kaggle.json', 'w') as file:
    json.dump(kaggle_credentials, file)

!mkdir -p ~/.kaggle
!cp '/content/kaggle.json' ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d hunter0007/ecommerce-dataset-for-predictive-marketing-2023

# unzip
!mkdir loan-dataset
!unzip -qq ecommerce-dataset-for-predictive-marketing-2023.zip -d ecommerce-dataset
!ls ecommerce-dataset

"""Terdapat satu data yaitu 'ECommerce_consumer behaviour.csv'

# Data Exploratotion

Menampilkan dataset dalam dataframe dan melihat 5 dataset pertama
"""

df= pd.read_csv('/content/ecommerce-dataset/ECommerce_consumer behaviour.csv')

df.head(60)

"""Value key dataset:

* order_id: Kunci unik yang mengidentifikasi setiap pesanan.
* user_id: Atribut yang memberikan informasi tentang pengguna yang melakukan * pesanan.
* order_number: Atribut yang mencatat nomor pesanan.
* order_dow: Atribut yang mencatat hari dalam seminggu pesanan dibuat.
* order_hour_of_day: Atribut yang mencatat waktu pesanan dibuat.
* days_since_prior_order: Atribut yang mencatat sejarah pesanan, yaitu berapa hari sejak pesanan sebelumnya dibuat.
* product_id: Kunci unik untuk mengidentifikasi produk dalam pesanan.
* add_to_cart_order: Atribut yang mencatat jumlah item yang ditambahkan ke keranjang.
* reordered: Atribut yang menunjukkan pemesanan ulang terjadi.
* department_id: Kunci unik yang mengidentifikasi departemen produk.
* department: Nama departemen produk.
* product_name: Nama produk.

Menampilkan dimensi dataset
"""

df.shape

"""Terdapat 2019501 baris data dan 12 kolom

Menampilkan informasi dataset
"""

df.info()

"""Terdapat 12 kolom dataset, 2 data objek, 9 data integer dan 1 data float

Menampilkan ringkasan statistik dari kolom data numerik
"""

df.describe()

"""informasi yang dapat diambil dari deskripsi statistik data yang diberikan:

* Jumlah Pesanan:

Terdapat sekitar lebih dari 2 juta pesanan.

* Distribusi Waktu Pemesanan:

Rata-rata order_hour_of_day adalah sekitar jam 13, dengan standar deviasi sekitar 4 jam. Ini dapat memberikan wawasan tentang pola waktu saat pengguna cenderung melakukan pembelian.

* Kebiasaan Pemesanan Ulang:

Dari kolom reordered, dapat dilihat bahwa rerata persentase pemesanan ulang adalah sekitar 59%, dengan standar deviasi sekitar 49%. Ini bisa menunjukkan sejauh mana pengguna cenderung memesan kembali produk yang pernah mereka beli sebelumnya.

* Frekuensi Pemesanan:

Rata-rata days_since_prior_order adalah sekitar 11 hari, dengan standar deviasi sekitar 9 hari. Ini dapat memberikan pemahaman tentang seberapa sering pengguna melakukan pemesanan ulang.

* Keranjang Belanja:

Rata-rata add_to_cart_order adalah sekitar 71, dengan standar deviasi sekitar 38. Hal ini menunjukkan sejauh mana pengguna cenderung menambahkan produk ke keranjang belanja mereka.

* Pola Pembelian Berdasarkan Hari dalam Seminggu:

Rata-rata order_dow (hari dalam seminggu) adalah sekitar 2.73, dengan standar deviasi sekitar 2.09. Ini dapat memberikan wawasan tentang pola pembelian pengguna dalam seminggu.

Dari detail statistika deskripsi diatas, didapatkan insight yang dapat membantu pembuatan sistem rekomendasi.

* Menyesuaikan rekomendasi produk berdasarkan waktu pembelian pengguna.
* Menyesuaikan rekomendasi produk berdasarkan kategori produk
* Menyesuaikan rekomendasi produk berdasarkan kondisi add to cart

Menampilkan ringkasan statistik dari kolom data kategorikal
"""

df.describe(include='O')

"""* Department:

Count: Jumlah total baris atau entri dalam kolom 'department' adalah 2,019,501.

Unique: Ada 21 nilai unik dalam kolom 'department', yang berarti terdapat 21 departemen berbeda dalam dataset.

Top: Nilai yang paling sering muncul (modus) dalam kolom 'department' adalah 'produce'.

Freq: Frekuensi atau jumlah kemunculan departemen 'produce' adalah 588,996 kali.

* Product Name:

Count: Jumlah total baris atau entri dalam kolom 'product_name' adalah 2,019,501.

Unique: Ada 134 nilai unik dalam kolom 'product_name', yang berarti terdapat 134 jenis produk berbeda dalam dataset.

Top: Produk yang paling sering muncul (modus) dalam kolom 'product_name' adalah 'fresh fruits'.

Freq: Frekuensi atau jumlah kemunculan produk 'fresh fruits' adalah 226,039 kali.

Menampilkan nilai unik setiap kolom
"""

df.nunique()

"""Menampilkan missing value pada dataset"""

df.isnull().sum()

"""Terdapat beberapa data null pada beberapa kolom

Menampilkan data duplikasi
"""

df.duplicated().sum()

"""Tidak ada data duplikasi

# Data Visualiztion

## Distribusi Order Hour of Day
"""

# Menghitung distribusi order_hour_of_day
hour_distribution = df['order_hour_of_day'].value_counts().sort_index()

# Membuat line chart
plt.figure(figsize=(10, 6))
plt.plot(hour_distribution.index, hour_distribution.values, marker='o', linestyle='-', color='b')

# Menambahkan judul dan label
plt.title('Distribusi Order Hour of Day')
plt.xlabel('Jam Pembelian')
plt.ylabel('Jumlah Pesanan')

# Menampilkan grid
plt.grid(True)

# Menampilkan line chart
plt.show()

"""Berdasarkan line plot distribusi diatas, diketahui prime time atau waktu dengan orderan yang relatif banyak terdapat pada jam 10 sampai 15.

## Distribusi Produk

### Top 10 Produk Order pada Dataset
"""

# Hitung jumlah pesanan untuk setiap produk
product_order_counts = df['product_name'].value_counts()

# Pilih 10 produk dengan order terbanyak
top_10_products = product_order_counts.nlargest(10)

# Buat bar plot
plt.figure(figsize=(12, 8))
top_10_products.plot(kind='bar', color='skyblue')
plt.title('Top 10 Produk dengan Order Terbanyak')
plt.xlabel('ID Produk')
plt.ylabel('Jumlah Pesanan')
plt.xticks(rotation=90, ha='right')  # Menambahkan rotasi untuk label sumbu x
plt.show()

"""### Top 10 Produk Order pada Prime Time"""

# Filter data untuk prime time (jam 10-15)
prime_time_data = df[(df['order_hour_of_day'] >= 10) & (df['order_hour_of_day'] <= 15)]

# Hitung jumlah pesanan untuk setiap produk
product_order_counts = prime_time_data.groupby('product_name').size()

# Pilih 10 produk dengan order terbanyak
top_10_products = product_order_counts.nlargest(10)

# Buat bar plot
plt.figure(figsize=(12, 8))
top_10_products.plot(kind='bar', color='skyblue')
plt.title('Top 10 Produk dengan Order Terbanyak pada Prime Time')
plt.xlabel('Nama Produk')
plt.ylabel('Jumlah Pesanan')
plt.xticks(rotation=90, ha='right')  # Menambahkan rotasi untuk label sumbu x
plt.show()

"""Pada prime time penjualan water seltzer sparkling water lebih banyak dari milk.

## Distribusi Department

### Top 10 Department Order pada Dataset
"""

# Hitung jumlah pesanan untuk setiap Departemen
product_order_counts = df['department'].value_counts()

# Pilih 10 Departemen dengan order terbanyak
top_10_products = product_order_counts.nlargest(10)

# Buat bar plot
plt.figure(figsize=(12, 8))
top_10_products.plot(kind='bar', color='skyblue')
plt.title('Top 10 Departemen dengan Order Terbanyak')
plt.xlabel('ID Departemen')
plt.ylabel('Jumlah Pesanan')
plt.xticks(rotation=90, ha='right')  # Menambahkan rotasi untuk label sumbu x
plt.show()

"""### Top 10 Department Order pada Prime Time"""

# Filter data untuk prime time (jam 10-15)
prime_time_data = df[(df['order_hour_of_day'] >= 10) & (df['order_hour_of_day'] <= 15)]

# Hitung jumlah pesanan untuk setiap Departemen
product_order_counts = prime_time_data.groupby('department').size()

# Pilih 10 Departemen dengan order terbanyak
top_10_products = product_order_counts.nlargest(10)

# Buat bar plot
plt.figure(figsize=(12, 8))
top_10_products.plot(kind='bar', color='skyblue')
plt.title('Top 10 Departemen dengan Order Terbanyak pada Prime Time')
plt.xlabel('Nama Departemen')
plt.ylabel('Jumlah Pesanan')
plt.xticks(rotation=90, ha='right')  # Menambahkan rotasi untuk label sumbu x
plt.show()

"""Top 10 departemen pada prime time masih sama dengan keseluruhan data

## Distribusi Produk setiap Departemen
"""

# Group by 'department' and count the number of unique 'product_id's in each department
product_count_per_department = df.groupby('department')['product_id'].nunique()

# Plot the product counts per department
product_count_per_department.plot(kind='bar', figsize=(10, 6), color='skyblue')

# Set plot labels and title
plt.xlabel('Departmen')
plt.ylabel('Jumlah Produk')
plt.title('Jumlah Produk setiap Departemen')

# Show the plot
plt.show()

"""## Distribusi User dengan Produk Order Terbanyak"""

# Menghitung nilai counts product_name untuk setiap user_id
user_product_counts = df.groupby(['user_id', 'product_name']).size().reset_index(name='total')

# Menampilkan DataFrame baru
user_product_counts

# Menghitung total produk order untuk setiap user_id
total_products_per_user = user_product_counts.groupby('user_id')['total'].sum()

# Pilih 10 user dengan total produk order terbanyak
top_10_users = total_products_per_user.nlargest(10)

# Buat bar plot
plt.figure(figsize=(12, 8))
top_10_users.plot(kind='bar', color='skyblue')
plt.title('Top 10 Pengguna dengan Total Produk Order Terbanyak')
plt.xlabel('User ID')
plt.ylabel('Total Produk Order')
plt.xticks(rotation=0)  # Tanpa rotasi untuk label sumbu x
plt.show()

"""# Data Preparation

## Menyiapkan Dataset untuk Rekomendasi Produk Berdasarkan Add to Cart
"""

# Menghitung nilai counts product_name untuk setiap user_id
user_product_counts = df.groupby(['user_id', 'department', 'product_name']).size().reset_index(name='total')

# Menampilkan DataFrame baru
user_product_counts

# Mengubah user_id menjadi list tanpa nilai yang sama
user_ids = user_product_counts['user_id'].unique().tolist()
print('list user_id: ', user_ids)

# Melakukan encoding user_id
user_to_user_encoded = {x: i for i, x in enumerate(user_ids)}
print('encoded user_id : ', user_to_user_encoded)

# Melakukan proses encoding angka ke ke user_id
user_encoded_to_user = {i: x for i, x in enumerate(user_ids)}
print('encoded angka ke user_id: ', user_encoded_to_user)

# Mengubah product_name menjadi list tanpa nilai yang sama
product_ids = user_product_counts['product_name'].unique().tolist()

# Melakukan proses encoding product_name
product_to_product_encoded = {x: i for i, x in enumerate(product_ids)}

# Melakukan proses encoding angka ke product_name
product_encoded_to_product = {i: x for i, x in enumerate(product_ids)}

product_encoded_to_product[0]

# Mendapatkan jumlah user
num_users = len(user_to_user_encoded)
print(num_users)

# Mendapatkan jumlah product
num_product = len(product_to_product_encoded)
print(num_product)

# Mengubah order menjadi nilai float
user_product_counts['total'] = user_product_counts['total'].values.astype(np.float32)

# Nilai minimum order
min_order = min(user_product_counts['total'])

# Nilai maksimal order
max_order = max(user_product_counts['total'])

print('Number of User: {}, Number of product: {}, Min order: {}, Max order: {}'.format(
    num_users, num_product, min_order, max_order
))

# Mapping userID ke dataframe user
user_product_counts['user_id'] = user_product_counts['user_id'].map(user_to_user_encoded)

# Mapping placeID ke dataframe product_name
user_product_counts['product_id'] = user_product_counts['product_name'].map(product_to_product_encoded)

user_product_counts

"""# Modeling"""

user_product_counts

# Membuat variabel x untuk mencocokkan data user dan resto menjadi satu value
x = user_product_counts[['user_id', 'product_id']].values

# Membuat variabel y untuk membuat total dari penjualan dan diskalakan dengan minmaxscaller
y = user_product_counts['total'].apply(lambda x: (x - min_order) / (max_order - min_order)).values

# Membagi menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * user_product_counts.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

class RecommenderNet(tf.keras.Model):

  # Insialisasi fungsi
  def __init__(self, num_users, num_product, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_product = num_product
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias
    self.product_embedding = layers.Embedding( # layer embeddings product
        num_product,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.product_bias = layers.Embedding(num_product, 1) # layer embedding product bias

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    product_vector = self.product_embedding(inputs[:, 1]) # memanggil layer embedding 3
    product_bias = self.product_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_product = tf.tensordot(user_vector, product_vector, 2)

    x = dot_user_product + user_bias + product_bias

    return tf.nn.sigmoid(x) # activation sigmoid

model = RecommenderNet(num_users, num_product, 50) # inisialisasi model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

from tensorflow.keras.utils import plot_model

# Build the model
model.build(input_shape=(128, 2))

# Tampilkan plot arsitektur model
plot_model(model, to_file='model_architecture.png', show_shapes=True, show_layer_names=True)

# Memulai training

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 128,
    epochs = 20,
    validation_data = (x_val, y_val)
)

plt.figure()
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['Training Loss', 'Validation Loss'], loc='upper right')
plt.title('Training and Validation Loss Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.show()

plt.figure()
plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.legend(['Training root_mean_squared_error', 'Validation root_mean_squared_error'], loc='upper right')
plt.title('Training and Validation root_mean_squared_error Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('root_mean_squared_error')
plt.show()

"""Hasil pelatihan menunjukan metrik yang bagus karena penurunan loss dan RMSE pada data test linear dengan data train, dan nilai evaluasinya tidak terlalu jauh hingga akhir pelatihan. Pada epoch terakhir (20) mendapat hasil evaluasi dengan val_loss: 0.0362 - val_root_mean_squared_error: 0.0139."""

from google.colab import drive
drive.mount('/content/drive')

# save model
model.save('/content/drive/MyDrive/Colab Notebooks/product_recommendation', save_format='tf')

"""# Model Inference"""

# load model
model = tf.keras.models.load_model('/content/drive/MyDrive/Colab Notebooks/product_recommendation')

# Mendapatkan satu pengguna secara acak
user_id = user_product_counts.user_id.sample(1).iloc[0]

# Mendapatkan daftar produk yang telah dipesan oleh pengguna
products_ordered_by_user = set(user_product_counts[user_product_counts.user_id == user_id]['product_id'].values)

# Mendapatkan semua produk yang ada dalam dataframe
all_products = set(user_product_counts['product_id'].unique())

# Mendapatkan produk yang tidak diorder oleh pengguna
products_not_ordered_by_user = list(all_products - products_ordered_by_user)


products_ordered_by_user_df = user_product_counts[user_product_counts.user_id == user_id]
# products_ordered_by_user_df = products_ordered_by_user_df.sort_values(by='total', ascending=False).head(5)
products_ordered_by_user_df

user_id

# products_not_ordered_by_user = [x for x in products_not_ordered_by_user]
user_product_array = np.hstack(
    ([[user_id]] * len(products_not_ordered_by_user), np.array([products_not_ordered_by_user]).T)
)

user_product_counts

# Memprediksi rekomendasi produk
recomended_product = model.predict(user_product_array).flatten()

# Mengambil indeks produk yang direkomendasikan secara berurutan
top_recomended_product_indices = recomended_product.argsort()[-10:][::-1]

# Mengambil product IDs yang sesuai dengan produk yang direkomendasikan
recommended_product_names = [
    product_encoded_to_product.get(products_not_ordered_by_user[x]) for x in top_recomended_product_indices
]


# Menampilkan hasil rekomendasi
print('Showing recommendations for user: {}'.format(user_id))
print('===' * 9)
print('Top 5 product order from user')
print('----' * 8)

top_product_user = (
    products_ordered_by_user_df.sort_values(
        by='total',
        ascending=False
    )
    .head(5)
    .product_name.values
)

# Melakukan proses encoding angka ke product_name
for product_name in top_product_user:
    product_info = product_count_per_department[product_count_per_department['product_name'] == product_name].iloc[0]
    print(f"Department: {product_info['department']}, Product Name: {product_info['product_name']}")

print('----' * 8)
print('Top 10 product recommendation')
print('----' * 8)

for product_name in recommended_product_names:
    product_info = product_count_per_department[product_count_per_department['product_name'] == product_name].iloc[0]
    print(f"Department: {product_info['department']}, Product Name: {product_info['product_name']}")
