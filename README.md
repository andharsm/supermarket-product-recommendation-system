
# Laporan Proyek Machine Learning - Andhar Siraj Munir

## Domain Proyek

### Latar Belakang

Dalam industri ritel, persaingan semakin ketat. Supermarket / ecommerce harus memastikan bahwa mereka memberikan pengalaman berbelanja yang unik dan relevan bagi pelanggan mereka. Sistem rekomendasi yang efisien dapat membantu supermarket mempertahankan dan menarik pelanggan [[1]](https://www.mdpi.com/2071-1050/13/9/4985). Berdasarkan penelitian, personalisasi menjadi kunci dalam menghadapi persaingan ini. Pelanggan mengharapkan pengalaman yang disesuaikan dengan preferensi individu mereka [[2]](https://books.google.co.id/books?hl=en&lr=&id=l831EAAAQBAJ&oi=fnd&pg=PP1&dq=Pelanggan+mengharapkan+pengalaman+yang+disesuaikan+dengan+preferensi+individu+mereka&ots=V24CCk7cxv&sig=LLEWAOITUm7KEzhYRxf2wgYx9-I&redir_esc=y#v=onepage&q&f=false). Dengan memahami preferensi ini, supermarket dapat menawarkan rekomendasi produk yang relevan, meningkatkan kepuasan pelanggan, dan memperkuat loyalitas. Selain itu, efisiensi pemasaran juga menjadi faktor penting. Dengan memanfaatkan sistem rekomendasi, supermarket dapat mengoptimalkan kampanye pemasaran, seperti mengirimkan penawaran khusus berdasarkan perilaku pembelian sebelumnya [[3]](https://www.mdpi.com/2071-1050/15/23/16151). Semua ini bertujuan untuk menciptakan pengalaman berbelanja yang lebih baik dan memperkuat posisi supermarket di pasar yang kompetitif.

Dalam era digital saat ini, sistem rekomendasi memainkan peran penting dalam menghadirkan pengalaman yang disesuaikan bagi pengguna. Dengan memanfaatkan data pelanggan dan algoritma cerdas, sistem rekomendasi dapat memberikan saran produk yang relevan, meningkatkan retensi pelanggan, dan mendorong penjualan.

Dataset supermarket yang digunakan adalah sumber daya berharga untuk memahami perilaku pembelian pelanggan, dataset yang dipakai adalah Supermarket dataset for predictive marketing 2023 [[4]](https://www.kaggle.com/datasets/hunter0007/ecommerce-dataset-for-predictive-marketing-2023/data). Dataset ini mencakup informasi tentang transaksi, produk yang dibeli, dan profil pelanggan. Dengan menganalisis data ini, sistem dapat mengidentifikasi pola pembelian, preferensi pelanggan, dan hubungan antara produk.

## Business Understanding

### Problem Statements
Bagaimana membuat model sistem rekomendasi produk berdasarkan aktivitas order pembeli lain dengan colaborative filtering?
* Tantangan utama dalam sistem rekomendasi saat ini adalah memberikan rekomendasi yang akurat dan sesuai dengan preferensi setiap pengguna.
* Fokus pada aktivitas order pembeli lain menjadi penting karena memberikan wawasan yang lebih baik mengenai preferensi pengguna daripada hanya mengandalkan data pengguna tersebut.

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

Dilakukan pengecekan Deskripsi Statik terhadap dataframe, baik data numerikal maupun data Kategorikal

Tabel 3. Deskripsi Statik Data Numerik
| Statistik    | order_id   | user_id    | order_number | order_dow  | order_hour_of_day | days_since_prior_order | product_id | add_to_cart_order | reordered | department_id |
|--------------|------------|------------|--------------|------------|---------------------|-----------------------|------------|-------------------|-----------|----------------|
| Count        | 2019501    | 2019501    | 2019501      | 2019501    | 2019501             | 1895159               | 2019501    | 2019501           | 2019501   | 2019501        |
| Mean         | 1707013    | 103067     | 17.15138     | 2.735367   | 13.43948            | 11.38603               | 71.20590   | 8.363173          | 0.5897427 | 9.928349       |
| Std          | 985983.2    | 59491.17    | 17.52576     | 2.093882   | 4.241008            | 8.97098                | 38.20727   | 7.150059          | 0.4918804 | 6.282933       |
| Min          | 10         | 2          | 1            | 0          | 0                  | 0                     | 1         | 1                 | 0         | 1              |
| 25%          | 852649     | 51584      | 5            | 1          | 10                 | 5                     | 31        | 3                 | 0         | 4              |
| 50%          | 1705004    | 102690     | 11           | 3          | 13                 | 8                     | 83        | 6                 | 1         | 9              |
| 75%          | 2559031    | 154600     | 24           | 5          | 16                 | 15                    | 107       | 11                | 1         | 16             |
| Max          | 3421080    | 206209     | 100          | 6          | 23                 | 30                    | 134       | 137               | 1         | 21             |

Informasi yang dapat diambil dari deskripsi statistik data yang ditunjukan pada Tabel 3:

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


Tabel 4. Deskripsi Statik Data Kategorikal
| Statistik  | department | product_name  |
|------------|------------|---------------|
| Count      | 2019501    | 2019501       |
| Unique     | 21         | 134           |
| Top        | produce    | fresh fruits  |
| Freq       | 588996     | 226039        |

Tabel 4 menunjukan Deskripsi statik dari kategorikal seperti berikut:

* Department
Count: Jumlah total baris atau entri dalam kolom 'department' adalah 2,019,501.

Unique: Ada 21 nilai unik dalam kolom 'department', yang berarti terdapat 21 departemen berbeda dalam dataset.

Top: Nilai yang paling sering muncul (modus) dalam kolom 'department' adalah 'produce'.

Freq: Frekuensi atau jumlah kemunculan departemen 'produce' adalah 588,996 kali.

* Product Name
Count: Jumlah total baris atau entri dalam kolom 'product_name' adalah 2,019,501.

Unique: Ada 134 nilai unik dalam kolom 'product_name', yang berarti terdapat 134 jenis produk berbeda dalam dataset.

Top: Produk yang paling sering muncul (modus) dalam kolom 'product_name' adalah 'fresh fruits'.

Freq: Frekuensi atau jumlah kemunculan produk 'fresh fruits' adalah 226,039 kali.
 
### Data Visualization
* Distribusi Produk
![top 10 produk terbanyak](https://github.com/andharsm/supermarket-product-recommendation-system/assets/114974933/a86c9714-88ac-4a2b-b81f-925c4e1bf108)
Gambar 1. Top 10 Produk Order

Berdasarkan visualisasi distribusi pada Gambar 1, dapat terlihat bahwa produk-produk segar seperti buah dan sayuran mendominasi peringkat teratas. Produk susu seperti yogurt dan susu juga cukup populer, bersama dengan produk camilan seperti keju kemasan, air berkarbonasi, dan chips/pretzel. Produk bebas laktosa dan roti menduduki peringkat terakhir dalam 10 daftar produk yang paling sering dibeli.

* Distribusi Departemen
![top 10 departemen terbanyak](https://github.com/andharsm/supermarket-product-recommendation-system/assets/114974933/b1e85179-c17b-4093-b736-2aaafc1f8a39)
Gambar 2. Top 10 Departemen Order

Dari Gambar 2, dapat terlihat bahwa departemen-produk segar seperti buah dan sayuran (Produce) mendominasi peringkat teratas. Produk-produk dasar seperti susu dan telur (Dairy Eggs) serta produk camilan (Snacks) juga sangat populer di antara pelanggan. 

* Distribusi Produk per Departemen
![produk per departemen](https://github.com/andharsm/supermarket-product-recommendation-system/assets/114974933/02ac2c41-710a-4cf3-a11b-bfe0a106cf7a)
Gambar 3. Distribusi Produk per Departemen

Ditunjukan pada Gambar 3 jumlah produk per departemen, terlihat bahwa departemen dengan variasi produk terbanyak adalah "Personal Care" dengan 17 produk, diikuti oleh "Pantry" dengan 12 produk, dan "Frozen" serta "Snacks" masing-masing memiliki 11 produk. Sementara itu, "Bulk", "Missing", dan "Other" memiliki jumlah produk yang sangat terbatas, hanya satu produk.

* Distribusi Pengguna
![top 10 pengguna dengan total produk order terbanyak](https://github.com/andharsm/supermarket-product-recommendation-system/assets/114974933/0b29b245-a7a4-46a9-b3af-fd74a9b5987a)
Gambar 4. Top 10 Pengguna dengan Total Produk Order Terbanyak


Gambar 4 menunjukan 10 data jumlah total transaksi (order) per user_id, terlihat bahwa user dengan ID 176478 memiliki jumlah transaksi tertinggi sebanyak 460 kali. Disusul oleh user dengan ID 129928 dan 126305 yang masing-masing memiliki 405 dan 384 transaksi. Insight dari data ini menunjukkan bahwa 10 pengguna teratas) memiliki aktivitas pembelian yang sangat tinggi, memberikan kontribusi signifikan pada total transaksi. 

## Data Preparation

Dalam proyek ini, dilakukan beberapa tahap data preparation guna mendapatkan hasil yang maksimal sesuai tujuan.

* Pengecekan Missing Value
Pada dataset yang digunakan terdapat 124342 baris data null pada kolom 'days_since_prior_order'. Karena kolom tersebut tidak digunakan maka kolom tersebut akan didrop dari data frame.

* Membuat Dictionary Product dan Department
Dilakukan proses encode data produk dan departemen menjadi integer unik, kemudian hasil encode tersebut dibuatkan dictionary berdasarkan label data aslinya.

Dictionary ini akan digunakan untuk maping pada proses deployment atau model inference saat menggunakan model untuk prediksi. Kamus tersebut akan lebih mudah diterapkan dalam maping daripada pencocokan data berdasarkan dataframe.

* Menyiamkan Dataframe Baru
Memilih beberapa atribut saja yaitu 'user_id', 'departement', 'product_name', dan 'product_id'.

Menambahkan atribut total dengan menghitung order produk unik pada setiap *user*, dan menghapus data produk duplikat tiap departemen. Hasil dataframe ditunjukan pada Tabel 5.

Tabel 5. Hasil dari Penambahan Atribut
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
Tahap modeling, model yang digunakan adalah RecommenderNet. Model RecomenmenderNet merupakan referensi model dari situs resmi keras yang digunakan dalam membuat sistem rekomendasi film dan mendapat hasil evaluasi val_loss: 0.6121 [[6]](https://keras.io/examples/structured_data/collaborative_filtering_movielens/). Pada proyek ini, model RecomenderNet tersebut akan diujikan dalam dataset supermarket untuk keperluan rekomendasi produk dengan collaborative filtering. Berikut adalah penjelasan mengenai model RecommenderNet:

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


![loss evaluasi](https://github.com/andharsm/supermarket-product-recommendation-system/assets/114974933/84f5d89d-186d-4382-a621-89df2b890d78)  
Gambar 5. *Metric evaluation loss*

![rmse evaluasi](https://github.com/andharsm/supermarket-product-recommendation-system/assets/114974933/511ba185-1c26-4514-be03-91c0a34fb8f6)
Gambar 6. *Metric evaluation loss* RMSE

Berdasarkan Gambar 5 dan Gambar 6, hasil pelatihan menunjukan metrik yang bagus karena penurunan loss dan RMSE pada data test linear dengan data train, dan nilai evaluasinya tidak terlalu jauh hingga akhir pelatihan. Pada epoch terakhir (20) mendapat hasil evaluasi dengan val_loss: 0.0362 - val_root_mean_squared_error: 0.0139.

## Evaluasi

* Merik RMSE
Metrik evaluasi yang digunakan adalah Root Mean Squared Error (RMSE) yang mengukur tingkat akurasi hasil dari perkiraan model yang telah dibuat. Root Mean Squared Error (RMSE) adalah salah satu metrik evaluasi yang umum digunakan untuk mengukur sejauh mana perbedaan antara nilai yang diprediksi oleh model dan nilai yang sebenarnya pada suatu dataset.

Rumus RMSE ditunjukan Gambar 7 berikut:

![rumus rmse](https://github.com/andharsm/supermarket-product-recommendation-system/assets/114974933/e8e64aea-f5fa-4e57-9e08-a9387c973612)
Gambar 7. Rumus RMSE

Dan dari proses training didapatkan RMSE terhadap data validasi 0.0139, dimana hasil ini lebih baik daripada penerapan pada dataset film yang ada disitus resmi keras.

Model inference
=========
Hasil rekomendasi dari user: 35474

Top 5 product order from user

- Department: babies, Product Name: diapers wipes
- Department: produce, Product Name: packaged vegetables fruits
- Department: produce, Product Name: fresh fruits
- Department: beverages, Product Name: water seltzer sparkling water
- Department: dairy eggs, Product Name: milk

Top 10 product recommendation

- Department: produce, Product Name: fresh vegetables
- Department: pets, Product Name: cat food care
- Department: alcohol, Product Name: beers coolers
- Department: frozen, Product Name: frozen meals
- Department: snacks, Product Name: energy granola bars
- Department: alcohol, Product Name: red wines
- Department: produce, Product Name: packaged produce
- Department: alcohol, Product Name: spirits
- Department: beverages, Product Name: energy sports drinks
- Department: frozen, Product Name: ice cream ice

User 35474 menunjukkan preferensi yang cenderung terfokus pada kebutuhan keluarga dengan anak kecil berdasarkan top 5 best product, mengingat pembelian produk bayi seperti diapers wipes. Selain itu, kecenderungan untuk memilih produk-produk segar dari departemen produce, bersama dengan pembelian minuman sehat seperti air mineral, menunjukkan kesadaran terhadap gaya hidup sehat. Dengan memasukkan produk-produk dari berbagai departemen seperti dairy eggs dan snacks, user ini menunjukkan keinginan untuk diversifikasi dalam pembelian. Rekomendasi tambahan seperti cat food, beers, dan frozen meals menunjukkan potensi minat dalam produk-produk khusus dan variasi. Adanya produk alkohol seperti beers, red wines, dan spirits juga mengindikasikan kemungkinan user ini sebagai peminum alkohol atau memiliki kebutuhan untuk produk alkohol berdasarkan user lainnya. 

## Referensi
[1] Lin R-H, Chuang W-W, Chuang C-L, Chang W-S. Applied Big Data Analysis to Build Customer Product Recommendation Model. Sustainability. 2021; 13(9):4985. https://doi.org/10.3390/su13094985

[2] Sitorus, S. A. (2024). Pemasaran 5.0: Revolusi Pengalaman Konsumen. Yayasan Pendidikan Cendekia Muslim.

[3] Stalidis G, Karaveli I, Diamantaras K, Delianidi M, Christantonis K, Tektonidis D, Katsalis A, Salampasis M. Recommendation Systems for e-Shopping: Review of Techniques for Retail and Sustainable Marketing. Sustainability. 2023; 15(23):16151. https://doi.org/10.3390/su152316151

[4] Kumar, R. Supermarket dataset for predictive marketing 2023

[5] Pedregosa, F, dkk. (2021). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research.

[6] Banerjee, s. (2020). Collaborative Filtering for Movie Recommendations.
