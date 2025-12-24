import requests
import numpy as np
import time

def get_distance_matrix(koordinatlar):
    """
    OSRM API kullanarak okullar arasındaki sürüş mesafesi matrisini oluşturur.
    """
    nokta_sayisi = len(koordinatlar)
    # Mesafeleri tutmak için sıfır matrisi oluştur (nokta_sayisi x nokta_sayisi)
    mesafe_matrisi = np.zeros((nokta_sayisi, nokta_sayisi))
    
    # Koordinatları OSRM formatına çevir (boylam,enlem;boylam,enlem...)
    coords_str = ";".join([f"{lon},{lat}" for lat, lon in koordinatlar])
    
    # OSRM Table Service URL (Sürüş mesafesi için)
    # annotations=distance parametresi mesafeyi metre cinsinden döndürür
    url = f"http://router.project-osrm.org/table/v1/driving/{coords_str}?annotations=distance"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data['code'] == 'Ok':
            # Metreyi kilometreye çevirerek matrise ata
            mesafe_matrisi = np.array(data['distances']) / 1000.0
            return mesafe_matrisi
        else:
            print("Hata: OSRM verisi alınamadı.")
            return None
            
    except Exception as e:
        print(f"Bağlantı Hatası: {e}")
        # Hata durumunda (yedek plan) kuş uçuşu mesafe hesaplayan bir fonksiyon çağrılabilir
        return None