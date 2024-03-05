
# Laporan Proyek Recomendation System - Andhar Siraj Munir

## Domain Proyek

### Latar Belakang

Dalam industri ritel, persaingan semakin ketat. Supermarket / ecommerce harus memastikan bahwa mereka memberikan pengalaman berbelanja yang unik dan relevan bagi pelanggan mereka. Sistem rekomendasi yang efisien dapat membantu supermarket mempertahankan dan menarik pelanggan [[1]](https://www.mdpi.com/2071-1050/13/9/4985). Berdasarkan penelitian, personalisasi menjadi kunci dalam menghadapi persaingan ini. Pelanggan mengharapkan pengalaman yang disesuaikan dengan preferensi individu mereka [[2]](https://books.google.co.id/books?hl=en&lr=&id=l831EAAAQBAJ&oi=fnd&pg=PP1&dq=Pelanggan+mengharapkan+pengalaman+yang+disesuaikan+dengan+preferensi+individu+mereka&ots=V24CCk7cxv&sig=LLEWAOITUm7KEzhYRxf2wgYx9-I&redir_esc=y#v=onepage&q&f=false). Dengan memahami preferensi ini, supermarket dapat menawarkan rekomendasi produk yang relevan, meningkatkan kepuasan pelanggan, dan memperkuat loyalitas. Selain itu, efisiensi pemasaran juga menjadi faktor penting. Dengan memanfaatkan sistem rekomendasi, supermarket dapat mengoptimalkan kampanye pemasaran, seperti mengirimkan penawaran khusus berdasarkan perilaku pembelian sebelumnya [[3]](https://www.mdpi.com/2071-1050/15/23/16151). Semua ini bertujuan untuk menciptakan pengalaman berbelanja yang lebih baik dan memperkuat posisi supermarket di pasar yang kompetitif.

Dalam era digital saat ini, sistem rekomendasi memainkan peran penting dalam menghadirkan pengalaman yang disesuaikan bagi pengguna. Dengan memanfaatkan data pelanggan dan algoritma cerdas, sistem rekomendasi dapat memberikan saran produk yang relevan, meningkatkan retensi pelanggan, dan mendorong penjualan.

Dataset supermarket yang Anda gunakan adalah sumber daya berharga untuk memahami perilaku pembelian pelanggan, dataset yang dipakai adalah Supermarket dataset for predictive marketing 2023 [[4]](https://www.kaggle.com/datasets/hunter0007/ecommerce-dataset-for-predictive-marketing-2023/data). Dataset ini mencakup informasi tentang transaksi, produk yang dibeli, dan profil pelanggan. Dengan menganalisis data ini, sistem dapat mengidentifikasi pola pembelian, preferensi pelanggan, dan hubungan antara produk.

## Business Understanding

### Problem Statements
Bagaimana membuat model sistem rekomendasi produk berdasarkan aktivitas order pembeli lain dengan colaborative filtering?

### Goals
Menghasilkan rekomendasi produk yang sesuai dengan preferensi pembeli sebelumnya dengan collaborative filtering.

### Solution Statements
Membuat atsitektur model RecommenderNet untuk melatih dataset menggunakan data riwayat order pembeli.


## Data Understanding

### Sumber Data

Dataset yang digunakan pada proyek ini adalah dataset *Supermarket dataset for predictive marketing 2023* yang didapatkan dari Kaggle. Detail sumber dataset ditunjukan pada Tabel 1.


Tabel 1. Deskripsi *Supermarket dataset for predictive marketing 2023*
Jenis | Keterangan
--- | ---
Sumber | [Kaggle Dataset : *Supermarket dataset for predictive marketing 2023*](https://www.kaggle.com/datasets/vikasukani/loan-eligible-dataset)
Lisensi | *Data files © Original Authors* @rupesh kumar
Kategori | *Retail and Shopping, Intermediate, E-Commerce Services*
Jenis dan Ukuran Berkas | CSV (16 MB)

### Infomasi Dataset

Informasi atribut dataset ditunjukan pada Tabel 2 berikut.

Tabel 2. *Value Key* Dataset
Nama Kolom | Keterangan
--- | ---
*order_id* |	Kunci unik yang mengidentifikasi setiap pesanan.
*user_id* |	Atribut yang memberikan informasi tentang pengguna yang melakukan * pesanan.
*order_number* |	Atribut yang mencatat nomor pesanan.
*order_dow* |	Atribut yang mencatat hari dalam seminggu pesanan dibuat.
*order_hour_of_day* |	Atribut yang mencatat waktu pesanan dibuat.
*days_since_prior_order* |	Atribut yang mencatat sejarah pesanan, yaitu berapa hari sejak pesanan sebelumnya dibuat.
*product_id* |	Kunci unik untuk mengidentifikasi produk dalam pesanan.
*add_to_cart_order* |	Atribut yang mencatat jumlah item yang ditambahkan ke keranjang.
*reordered* |	Atribut yang menunjukkan pemesanan ulang terjadi.
*department_id* |	Kunci unik yang mengidentifikasi departemen produk.
*Credit_History* |	Riwayat kredit memenuhi panduan.
*department* |	Nama departemen produk.
*product_name* |	Nama produk.


### Data Visualization
* Distribusi Produk
![top 10 produk terbanyak](https://github.com/andharsm/supermarket-product-recommendation-system/assets/114974933/a86c9714-88ac-4a2b-b81f-925c4e1bf108)
Gambar 1. Top 10 Produk Order

* Distribusi Departemen
![top 10 departemen terbanyak](https://github.com/andharsm/supermarket-product-recommendation-system/assets/114974933/b1e85179-c17b-4093-b736-2aaafc1f8a39)
Gambar 2. Top 10 Departemen Order

* Distribusi Produk per Departemen
![produk per departemen](https://github.com/andharsm/supermarket-product-recommendation-system/assets/114974933/02ac2c41-710a-4cf3-a11b-bfe0a106cf7a)
Gambar 3. Distribusi Produk per Departemen

* Distribusi Pengguna
![top 10 pengguna dengan total produk order terbanyak](https://github.com/andharsm/supermarket-product-recommendation-system/assets/114974933/0b29b245-a7a4-46a9-b3af-fd74a9b5987a)
Gambar 4. Top 10 Pengguna dengan Total Produk Order Terbanyak

## Data Preparation

Dalam proyek ini, dilakukan beberapa tahap data preparation guna mendapatkan hasil yang maksimal sesuai tujuan.

Memilih beberapa atribut saja yaitu 'user_id', 'departement', 'product_name', dan 'product_id'.

Menambahkan atribut total dengan menghitung order produk unik pada setiap *user*, dan menghapus data produk duplikat tiap departemen. Hasil dataframe ditunjukan pada Tabel 3.

Tabel 3. Hasil dari Penambahan Atribut
user_id | department | product_name | total | product_id
--- | --- | --- | --- | ---
0 |	dairy eggs |	packaged cheese |	2.0 |	0
0 |	deli |	fresh dips tapenades |	1.0 |	1
0 |	deli |	lunch meat |	1.0 |	2
0 |	deli |	prepared soups salads |	1.0 |	3
0 |	produce |	fresh fruits |	3.0 |	4
---- | ---- | ---- | ---- | ----

### Split Dataset
Tujuan dari pembagian dataset ini adalah untuk membagi data menjadi dua yang digunakan untuk melatih dan mengevaluasi kinerja model dengan bantuan library train_test_split [[5]](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html). Pada proyek ini, 80 persen dataset digunakan untuk melatih model, dan 20 persen sisanya digunakan untuk mengevaluasi model.


## Modeling
Tahap modeling, model yang digunakan adalah RecommenderNet. Berikut adalah penjelasan mengenai model RecommenderNet yang Anda berikan:

1. Inisialisasi Model:
Model ini merupakan turunan dari kelas tf.keras.Model.
Dalam metode __init__, beberapa parameter diinisialisasi, termasuk num_users (jumlah pengguna), num_product (jumlah produk), dan embedding_size (ukuran embedding).
* Empat layer embedding didefinisikan:
* user_embedding: Menghasilkan vektor embedding untuk setiap pengguna.
* user_bias: Menghasilkan bias untuk setiap pengguna.
* product_embedding: Menghasilkan vektor embedding untuk setiap produk.
* product_bias: Menghasilkan bias untuk setiap produk.

2. Fungsi call:
Fungsi ini mengimplementasikan logika model.
Pertama, vektor embedding pengguna dan bias pengguna diambil berdasarkan input.
Selanjutnya, vektor embedding produk dan bias produk diambil.
Hasil perkalian tensor antara vektor pengguna dan vektor produk dihitung.
Akhirnya, hasil dari penjumlahan dot product dengan bias pengguna dan bias produk diaktivasi menggunakan fungsi sigmoid.

3. Compile Model:
Model di-compile dengan menggunakan fungsi loss BinaryCrossentropy dan optimizer Adam.
Metrik yang digunakan adalah Root Mean Squared Error (RMSE).

## Evaluasi

Metrik evaluasi yang digunakan adalah Root Mean Squared Error (RMSE) yang mengukur tingkat akurasi hasil dari perkiraan model yang telah dibuat.

![loss evaluasi](https://github.com/andharsm/supermarket-product-recommendation-system/assets/114974933/84f5d89d-186d-4382-a621-89df2b890d78)  
Gambar 5. *Metric evaluation loss*

![rmse evaluasi](https://github.com/andharsm/supermarket-product-recommendation-system/assets/114974933/511ba185-1c26-4514-be03-91c0a34fb8f6)
Gambar 6. *Metric evaluation loss* RMSE

Berdasarkan Gambar 5 dan Gambar 6, hasil pelatihan menunjukan metrik yang bagus karena penurunan loss dan RMSE pada data test linear dengan data train, dan nilai evaluasinya tidak terlalu jauh hingga akhir pelatihan. Pada epoch terakhir (20) mendapat hasil evaluasi dengan val_loss: 0.0362 - val_root_mean_squared_error: 0.0139.

## Referensi
[1] Lin R-H, Chuang W-W, Chuang C-L, Chang W-S. Applied Big Data Analysis to Build Customer Product Recommendation Model. Sustainability. 2021; 13(9):4985. https://doi.org/10.3390/su13094985

[2] Sitorus, S. A. (2024). Pemasaran 5.0: Revolusi Pengalaman Konsumen. Yayasan Pendidikan Cendekia Muslim.

[3] Stalidis G, Karaveli I, Diamantaras K, Delianidi M, Christantonis K, Tektonidis D, Katsalis A, Salampasis M. Recommendation Systems for e-Shopping: Review of Techniques for Retail and Sustainable Marketing. Sustainability. 2023; 15(23):16151. https://doi.org/10.3390/su152316151

[4] Kumar, R. Supermarket dataset for predictive marketing 2023

[5] Pedregosa, F, dkk. (2021). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research.  
