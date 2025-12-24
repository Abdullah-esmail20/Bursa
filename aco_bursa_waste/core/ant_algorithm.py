import numpy as np
import random
from data.coordinates import SCHOOLS
from core.matrix_utils import get_distance_matrix
from config import ALPHA, BETA, Q

# تغيير الاسم من aco_calistir إلى run_aco ليطابق ما يطلبه ملف main.py
def run_aco(karinca_sayisi, iterasyon_sayisi, buharlasman_orani):
    # Okul koordinatlarını al
    koordinatlar = [(s['lat'], s['lon']) for s in SCHOOLS]
    nokta_sayisi = len(koordinatlar)
    
    # Mesafe matrisini OSRM üzerinden al [cite: 126, 152]
    mesafe_matrisi = get_distance_matrix(koordinatlar)
    
    # Feromon matrisini ilklendir (Başlangıçta her yol eşit) 
    feromonlar = np.ones((nokta_sayisi, nokta_sayisi))
    
    en_iyi_yol = None
    en_kisa_mesafe = float('inf')
    mesafe_gecmisi = []

    for i in range(iterasyon_sayisi):
        tum_yollar = []
        for k in range(karinca_sayisi):
            yol = karinca_yolu_olustur(nokta_sayisi, feromonlar, mesafe_matrisi)
            mesafe = yol_mesafesi_hesapla(yol, mesafe_matrisi)
            tum_yollar.append((yol, mesafe))
            
            # En iyi yolu güncelle
            if mesafe < en_kisa_mesafe:
                en_kisa_mesafe = mesafe
                en_iyi_yol = yol
        
        # Feromon buharlaşması ve güncellemesi [cite: 130, 152]
        feromonlar *= (1 - buharlasman_orani)
        for yol, mesafe in tum_yollar:
            for s in range(nokta_sayisi - 1):
                feromonlar[yol[s]][yol[s+1]] += Q / mesafe
        
        mesafe_gecmisi.append(en_kisa_mesafe)
        
    return en_iyi_yol, mesafe_gecmisi

def karinca_yolu_olustur(nokta_sayisi, feromonlar, mesafe_matrisi):
    yol = [random.randint(0, nokta_sayisi - 1)] # Rastgele من مدرسة البداية
    ziyaret_edilmeyenler = list(set(range(nokta_sayisi)) - set(yol))
    
    while ziyaret_edilmeyenler:
        su_an = yol[-1]
        olasiliklar = []
        
        # Karıncanın اختيار المدرسة التالية بناءً على الفرومون والمسافة [cite: 130, 152]
        for hedef in ziyaret_edilmeyenler:
            tau = feromonlar[su_an][hedef] ** ALPHA
            eta = (1.0 / mesafe_matrisi[su_an][hedef]) ** BETA
            olasiliklar.append(tau * eta)
            
        toplam_olasilik = sum(olasiliklar)
        secim_olasiliklari = [o / toplam_olasilik for o in olasiliklar]
        
        sonraki_durak = random.choices(ziyaret_edilmeyenler, weights=secim_olasiliklari)[0]
        yol.append(sonraki_durak)
        ziyaret_edilmeyenler.remove(sonraki_durak)
    
    yol.append(yol[0]) # العودة للبداية (TSP)
    return yol

def yol_mesafesi_hesapla(yol, mesafe_matrisi):
    toplam = 0
    for i in range(len(yol) - 1):
        toplam += mesafe_matrisi[yol[i]][yol[i+1]]
    return toplam