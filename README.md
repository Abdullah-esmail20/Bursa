# Bursa
# ACO – Bursa Rota Optimizasyonu (Senaryo 3)
**Bursa Geri Dönüşüm Aracı için Karınca Kolonisi Optimizasyonu (Ant Colony Optimization – ACO) ile en verimli rota planlama**

Bu proje, Bursa’daki **12 nokta/okul** arasında bir aracın en kısa/etkin turu oluşturmasını hedefler.  
Mesafeler **Google Maps (Geocoding + Distance Matrix API)** üzerinden gerçek yol koşullarına göre alınır, ardından **ACO algoritması** ile optimuma yakın rota hesaplanır ve sonuçlar **Streamlit arayüzünde** grafik + harita olarak gösterilir.

---

## Projenin Faydası / Neden Önemli?
Bu çalışma “teorik optimizasyonu” gerçek dünyaya bağlar:

- **Yakıt ve zaman tasarrufu:** Daha kısa rota → daha az mesafe → daha düşük maliyet.
- **Operasyon verimliliği:** Geri dönüşüm/servis/dağıtım gibi saha operasyonlarında günlük planlamayı iyileştirir.
- **Gerçek veri kullanımı:** Uydurma mesafe yerine Google’ın yol verisiyle (mode: driving/walking/transit) hesaplama.
- **Parametre analizi:** ACO parametrelerini değiştirerek farklı sonuçlar gözlemlenebilir (alpha/beta/evaporation vb.).
- **Görselleştirme:** Sonuçların harita üstünde görülebilmesi, raporlama ve sunum açısından güçlüdür.

Bu proje; lojistik, rota planlama, akıllı şehirler, atık yönetimi ve dağıtım sistemleri gibi alanlarda uygulanabilir.

---

## Özellikler
- 12 nokta (okullar) arasında rota optimizasyonu
- Google Maps ile:
  - Adres → koordinat (Geocoding)
  - Koordinatlar arası mesafe matrisi (Distance Matrix)
- ACO ile:
  - En iyi tur + toplam mesafe
  - İterasyonlara göre yakınsama (convergence) grafiği
- Folium haritası:
  - Nokta işaretleri
  - En iyi turun polyline çizimi
- Streamlit arayüzünde parametre kontrolü:
  - Karınca sayısı, iterasyon sayısı, alpha, beta, buharlaşma, Q, ulaşım modu

---

## Ekran Çıktıları
- **En iyi toplam mesafe (km)**
- **En iyi tur (index)** ve **adresler**
- **Convergence grafiği** (en iyi mesafe/iterasyon)
- **Harita üzerinde rota** (marker + polyline)

---

---

## Görselleştirme

### En İyi Rota Haritası
- Okullar **kırmızı noktalar** ile gösterilir  
- Optimum rota **mavi kesikli çizgi** ile belirtilir  
- Okullar ziyaret sırasına göre numaralandırılır  
- Çıktı dosyası: `figure/rota.png`

### Yakınsama Grafiği
- X ekseni: İterasyon sayısı  
- Y ekseni: En kısa mesafe (km)  
- Algoritmanın zamanla nasıl kararlı hale geldiğini gösterir  
- Çıktı dosyası: `figure/convergence.png`

---

## Mesafe Hesaplama (OSRM)

Okullar arası sürüş mesafeleri, **OSRM (Open Source Routing Machine) API** kullanılarak hesaplanır.

- Gerçek yol mesafeleri kullanılır  
- Mesafeler kilometre cinsine dönüştürülür  
- API hatası durumunda alternatif mesafe hesaplama yöntemleri uygulanabilir  

---

## Streamlit Kullanıcı Arayüzü

Arayüz üzerinden kullanıcılar:
- Karınca sayısını belirleyebilir  
- İterasyon sayısını ayarlayabilir  
- Buharlaşma oranını (Rho) değiştirebilir  
- Tek tıkla optimizasyonu başlatabilir  
- Rota haritası ve yakınsama grafiğini inceleyebilir  

### Kullanım Adımları:
1. Parametreleri ayarla  
2. **“Rota Optimizasyonunu Başlat”** butonuna tıkla  
3. En kısa mesafeyi görüntüle  
4. Grafikler üzerinden sonuçları analiz et  

---

## Üretilen Çıktılar

- En kısa atık toplama rotası  
- Toplam mesafe (km)  
- Rota görselleştirmesi  
- Yakınsama grafiği  

---
## 🗺️ En İyi Rota Haritası
![En İyi Rota](https://github.com/Abdullah-esmail20/Bursa/blob/c3fb42702b1036a03223c9a937e2507dd7fdd6b8/rote2.png)

## 📈 Yakınsama Grafiği
![Yakınsama Grafiği](figure/convergence.png)


## Çalıştırma Talimatları

```bash
pip install -r requirements.txt
streamlit run main.py

## Kullanılan Teknolojiler
- Python
- Streamlit
- NumPy
- Matplotlib
- Folium + streamlit-folium
- googlemaps (Google Maps Python Client)

---

## Proje Yapısı
Kodunuz bu dosyaları bekler:

```text
aco_bursa_waste/
├── core/               # ACO Algoritması ve Mesafe Hesaplamaları [cite: 147]
├── data/               # Okul Koordinat Verileri (12 Lise) [cite: 147]
├── visual/             # Harita ve Grafik Çizim Fonksiyonları [cite: 147]
├── figure/             # Kaydedilen Sonuç Grafikleri [cite: 147]
├── main.py             # Streamlit Ana Uygulama Dosyası [cite: 147]
└── README.md           # Proje Tanıtım Dosyası [cite: 147]



