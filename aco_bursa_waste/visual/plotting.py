import matplotlib.pyplot as plt
import networkx as nx
from data.coordinates import SCHOOLS
import os

def plot_route(en_iyi_yol):
    """
    En iyi rotayı Bursa haritası düzleminde çizer ve figure/rota.png olarak kaydeder.
    """
    plt.figure(figsize=(12, 8))
    
    # Okul isimlerini ve koordinatlarını al
    isimler = [SCHOOLS[i]['name'] for i in en_iyi_yol]
    lats = [SCHOOLS[i]['lat'] for i in en_iyi_yol]
    lons = [SCHOOLS[i]['lon'] for i in en_iyi_yol]
    
    # Noktaları çiz (Okullar)
    plt.scatter(lons, lats, c='red', s=100, label='Okullar')
    
    # Yolları çiz (Rota çizgileri)
    plt.plot(lons, lats, 'b--', alpha=0.6, label='Atık Toplama Rotası')
    
    # Okul isimlerini yanlarına yaz
    for i, isim in enumerate(isimler):
        if i < len(isimler) - 1: # Son durak başlangıçla aynı olduğu için tekrar yazma
            plt.text(lons[i], lats[i], f" {i+1}. {isim}", fontsize=9, verticalalignment='bottom')

    plt.title("Bursa Okul Atık Toplama - En İyi Rota")
    plt.xlabel("Boylam (Longitude)")
    plt.ylabel("Enlem (Latitude)")
    plt.legend()
    plt.grid(True)
    
    # Dosyayı kaydet [cite: 147]
    if not os.path.exists('figure'):
        os.makedirs('figure')
    plt.savefig('figure/rota.png')
    
    return plt

def plot_convergence(mesafe_gecmisi):
    """
    Algoritmanın iterasyonlara göre mesafe gelişimini çizer ve figure/convergence.png olarak kaydeder.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(mesafe_gecmisi, color='green', linewidth=2)
    
    plt.title("Algoritma Yakınsama Grafiği")
    plt.xlabel("İterasyon Sayısı")
    plt.ylabel("En Kısa Mesafe (km)")
    plt.grid(True)
    
    # Dosyayı kaydet [cite: 147]
    if not os.path.exists('figure'):
        os.makedirs('figure')
    plt.savefig('figure/convergence.png')
    
    return plt