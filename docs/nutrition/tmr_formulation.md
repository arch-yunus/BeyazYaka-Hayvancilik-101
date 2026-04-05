# TMR Formülasyon Kılavuzu | Step-by-Step TMR Formulation

## TMR Nedir ve Neden Önemlidir?

**TMR (Total Mixed Ration / Tam Yem Rasyonu)**, kaba yem ve kesif yemin homojen biçimde karıştırıldığı yem hazırlama yöntemidir. Geleneksel ayrı yemleme yöntemlerinden temel farkı şudur: **Hayvan her lokmada eşit oranda besin alır, seçim yapamaz.**

### Seçimli Yem Tehlikesi

Seçimli yemlemede (yani kaba ve kesif yemin ayrı verildiği), Holstein gibi yüksek verimli bir inek:
1. Çok sevdiği kesif yemi önce yer → Rumen asidozu riski artar.
2. Kaba yemi sonraya bırakır ya da hiç yemez → Rumen pH dengesi bozulur.
3. Sonuç: **SARA → Topallık → Verim düşüşü → Erken sürü çıkışı**

## Adım Adım TMR Formülasyon

### Adım 1: Hayvan Kategorisini Belirle

| Grup | Tanım |
|---|---|
| **Dry Cow (Kuru İnek)** | Doğuma 60-20 gün kalan |
| **Close-up (Yaklaşma)** | Doğuma 21 gün kalan — Kritik geçiş dönemi |
| **Fresh Cow** | Yeni doğurmuş, ilk 21 gün |
| **Laktasyon Pik** | 20-100. gün — En yüksek enerji ihtiyacı |
| **Orta Laktasyon** | 100-200. gün |
| **Geç Laktasyon** | 200-305. gün |

### Adım 2: Besin Gereksinimleri

Pik laktasyondaki Holstein (≥35 L/gün):

| Besin | Gereksinim |
|---|---|
| Kuru Madde Alımı | 22-25 kg/gün |
| Ham Protein | %17-18 (DM bazlı) |
| NDF | min %28 (DM bazlı) |
| Nişasta | max %26 (DM bazlı) |
| NEL | 1.65-1.75 Mcal/kg |
| Kalsiyum | %0.80 |

### Adım 3: Yem Listesi Derleme

**Kaba Yemler:**
1. Mısır Silajı (Temel enerji + lif kaynağı)
2. Yonca Silajı (Ham protein kaynağı)
3. Buğday Samanı (NDF artışı için)

**Kesif Yemler:**
1. Arpa/Mısır (Enerji)
2. Soya Küspesi / Pamuk Tohumu Küspesi (Protein)
3. Biyerası / Kuru Şeker Pancarı Posası (Yavaş fermente enerji)

### Adım 4: Karışım Oranını Belirle (Deneme-Yanılma veya NRC Modeli)

```
Örnek Formül (Pik Laktasyon Holstein - 22 kg DM hedefi):
- Mısır Silajı:      20 kg (as fed)
- Yonca Silajı:       5 kg
- Pamuk Tohumu K.:    3 kg
- Arpa:               6 kg
- Soya Küspesi:       4 kg
- Biyeras (Kuru):     2 kg
- Mineral-Vitamin Prx: 0.3 kg
─────────────────────────────
Toplam:              40.3 kg (as fed) → ~22 kg DM
```

### Adım 5: Doğrulama

`scripts/ration_calculator.py` aracını kullanarak son besin profilini hesapla.

### Adım 6: Karıştırma Sırası (Mikser Yüklemesi)

```
1. Uzun kaba yem (Saman)         → İlk yükle
2. Kuru kesif yemler              → Sonra
3. Islak materyaller (Silaj)      → Ortada
4. Sıvı katkılar (Koruyucu, Ab.) → En son
5. Karıştırma süresi: 3-5 dakika (FAZLA karıştırma NDF yıkar!)
```

## Penn State Parçacık Ayırıcısı (PSPS) Değerlendirme

| Elek | Boyut | İdeal Oran |
|---|---|---|
| Üst (Uzun Parça) | > 19mm | %2-8 |
| Orta | 8-19mm | %30-50 |
| Alt | < 8mm | %30-50 |
| Taban | < 1mm | %20 max |
