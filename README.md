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
.
├─ main.py                # Streamlit UI (parametreler, sonuçlar, harita, grafik)
├─ maps.py                # Google Maps: geocode + distance matrix
├─ aco.py                 # ACO algoritması (run_aco fonksiyonu)
├─ schools.py             # 12 nokta listesi (SCHOOLS)
├─ requirements.txt
└─ .streamlit/
   └─ secrets.toml        # GOOGLE_MAPS_API_KEY (GitHub'a yükleme!)



