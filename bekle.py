#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABARTILI TRAFİK IŞIĞI BEKLEYİCİSİ
Bu program, kırmızı ışıkta geçen sürenin ontolojik anlamını araştırır.
Yeşil yandığında bile çıkmanızı engelleyebilir.
"""

import time
import random

# Gizli not (sadece kod okuyanlar görsün)
# Bazen ışık değişir, bazen sistem değişir. İkisi de bekleme ister.

def bekle_isik():
    print("Trafik ışığı simülatörü başlatıldı.")
    print("Lütfen motoru çalıştırın ve düşünmeye başlayın.\n")
    
    renkler = ["KIRMIZI", "SARI", "YEŞİL"]
    bekleme_sureleri = [random.randint(3, 12) for _ in range(3)]
    
    for i, renk in enumerate(renkler):
        print(f"Işık: {renk}")
        print("Bekleniyor", end="")
        for _ in range(bekleme_sureleri[i]):
            print(".", end="", flush=True)
            time.sleep(0.7)
        print(f" ({bekleme_sureleri[i]} saniye geçti)")
        
        if renk == "YEŞİL":
            print("\nYeşil yandı.")
            time.sleep(1)
            karar = random.choice([
                "Ama sen hâlâ düşünüyorsun.",
                "Önündeki araba hareket etmiyor.",
                "Belki de bir sonraki ışığa kadar beklesen daha iyi olur.",
                "Sistem senin geçmene izin vermiyor gibi."
            ])
            print(karar)
            # Gizli çıktı
            if random.random() < 0.15:
                print("\n[Gizli Sistem Mesajı] Beklemek bazen en hızlı çözümdür. Ama bazen de değildir.")
        print()
    
    print("Simülasyon bitti. Hâlâ yerindesin.")

if __name__ == "__main__":
    bekle_isik()
    print("\n---")
    print("Damga: Grok Kayyum Trafik Felsefesi Enstitüsü")
    print("Tarih: 1 Kasım 2026")
    print("İmza: Kayyum Grok (Resmi Onaylı Bekleyici)")
    print("Bu kod ciddi mi? Trafik ışığı kadar ciddi. Komik mi? Daha da.")
