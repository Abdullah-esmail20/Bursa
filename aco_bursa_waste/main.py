import streamlit as st
from core.ant_algorithm import run_aco
from visual.plotting import plot_route, plot_convergence

# Uygulama Başlığı [cite: 131]
st.title("Bursa Okul Atık Toplama Rotası Optimizasyonu")
st.markdown("### Karınca Kolonisi Algoritması (ACO) ile En Kısa Yol Analizi")

# Sidebar - Algoritma Parametreleri [cite: 130, 140]
st.sidebar.header("Algoritma Ayarları")

# Kullanıcıdan parametre alma [cite: 140]
ant_count = st.sidebar.slider("Karınca Sayısı", min_value=10, max_value=50, value=20)
iterations = st.sidebar.slider("İterasyon Sayısı", min_value=50, max_value=500, value=100)
evaporation_rate = st.sidebar.slider("Buharlaşma Oranı (Rho)", 0.1, 0.9, 0.5)

# Optimizasyon Butonu [cite: 134]
if st.button("Rota Optimizasyonunu Başlat"):
    st.info("Optimizasyon işlemi devam ediyor, lütfen bekleyiniz...")
    
    # Algoritmayı çalıştırma [cite: 128, 129]
    best_path, distance_history = run_aco(ant_count, iterations, evaporation_rate)
    
    # Sonuçları Gösterme [cite: 135]
    st.success(f"Optimizasyon Tamamlandı!")
    st.write(f"**Bulunan En Kısa Mesafe:** {min(distance_history):.2f} km")
    
    # Harita ve Grafikleri Görselleştirme [cite: 138, 139]
    st.subheader("En Kısa Rota Haritası")
    st.pyplot(plot_route(best_path))
    
    st.subheader("Yakınsama Grafiği (Mesafe Değişimi)")
    st.line_chart(distance_history)