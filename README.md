# Tugas Besar Data Science II4042 AI for Business

13519040 - Shafira Naya Aprisadianti
18219090 - Vania Alya Qonita  
18219106 - Fathiyya Maghfirah Teddy

**Deployment Link: https://skincarerecommendation.herokuapp.com**

## Deskripsi Perusahan

BeautyHaul merupakan #1 Curated Beauty e-Commerce yang ingin membuat pengalaman berbelanja Anda menjadi simple & cepat, semuanya dalam 1 click. Visi dari beautyhaul adalah membuat beauty ekosistem yang saling terintegrasi mulai dari Review, Blog, Forum, Penjualan dan Events. Misi dari beautyhaul adalah membantu semua orang menjadi cantik & mendapatkan produk-produk kecantikan terbaik yang telah dikurasi secara ketat dengan harga yang terjangkau dan membantu membesarkan lokal brand dari Indonesia untuk bisa masuk ke pasar internasional.

Sumber : https://www.beautyhaul.com/

## Masalah

BeautyHaul memiliki e-commerce yang menjual berbagai macam brand. Hal ini seharusnya menjadi kelebihan tersendiri bagi perusahaan karena dapat dimanfaatkan untuk membuat pelanggan bisa membeli lebih banyak produk dari brand yang berbeda-beda. Namun, saat ini kebanyakan pelanggan hanya membeli produk dari brand yang sama. Hal ini akan membuat e-commerce kalah saing jika ada platform lain yang menawarkan harga lebih murah. Oleh karena itu, perusahaan perlu mencari cara agar pelanggan mendapat manfaat dari membeli produk berbeda brand pada platform yang sama.

Masalah bisnis yang difokuskan adalah : Bagaimana agar konsumen berbelanja lebih banyak produk dari brand yang lebih variatif.

**Pertanyaan:**  
Bagaimana perusahaan dapat memberikan rekomendasi produk berdasarkan kecocokan ingredients dari produk yang dilihat pelanggan dan jenis kulit dari pelanggan?
Bagaimana perusahaan dapat menemukan kategori yang cocok dengan produk sesuai dengan atribut-atribut lainnya?
**Pengukuran Keberhasilan:**  
Pengukuran keberhasilan solusi: Persentase peningkatan penjualan dari brand yang variatif dan persentase peningkatan retaining customer

## Solusi

Berdasarkan masalah yang ada, kami merumuskan solusi berupa recommendaion system dengan memanfaatkan data deskripsi dan ingredients dari produk. Pemberian rekomendasi produk akan ditentukan berdasarkan perankingan similaritas antar suatu produk dengan produk lainnya.

Pemberian rekomendasi dengan cara mencocokan similaritas produk berdasarkan deskripsi dan ingredients dapat dilakukan karena sebuah permasalahan kulit biasanya dapat diatasi dengan ingredients tertentu. Oleh karena itu, sebuah produk yang mengandung ingredients yang sama kurang lebih menangani masalah kulit yang sama dan cocok untuk tipe kulit yang sama

Dibuat juga sebuah solusi berupa sistem clustering yang dapat mengelompokkan produk dan memetakannya terhadap kategori produk tersebut.

## Data

Data didapat dari web scraping beautyhaul.com, dengan menggunakan web scraper (BeautifulSoup) pada link <a href="https://colab.research.google.com/drive/1ZnQ__IPne8TnKjggfltNdIvPDw6qrO5A?authuser=1#scrollTo=ZsmuIKwYNSuf" target="_blank">berikut</a>. Data-data yang dipakai adalah nama produk, brand, deskripsi, dan ingredients.

## Akses Website

Berikut merupakan hasil model yang telah kami deploy.
Link Recommendation System : https://skincarerecommendation.herokuapp.com/recommendation
Link Clustering : https://skincarerecommendation.herokuapp.com/clustering

## Cara menjalankan web di lokal

```bash
git clone https://github.com/shafiranaya/skincare-recommendation.git
virtualenv venv
source venv/bin/activate
python app.py
```
