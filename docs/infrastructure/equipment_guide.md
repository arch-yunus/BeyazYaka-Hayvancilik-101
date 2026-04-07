# Ekipman Seçim Rehberi | Equipment Selection Guide
## Modern Hayvancılık İşletmelerinde Teknoloji ve Mekanizasyon

> **TR:** İşletmenin verimliliği, seçilen ekipmanların işletme ölçeğiyle (Herd Size) uyumuna bağlıdır. Yanlış kapasite seçimi ya atıl yatırım ya da operasyonel tıkanıklık demektir.
>
> **EN:** Efficiency depends on the alignment of equipment with farm scale. Miscalculated capacity results in dormant investment or operational bottlenecks.

---

## 🥛 1. Sağım Sistemleri | Milking Systems

Seçim, günlük sağım süresinin (max 3-4 saat/grup) toplam hayvan sayısına oranlanmasıyla yapılır.

| Sistem Tipi | Ölçek (İnek Sayısı) | Verimlilik (İnek/Saat) | Özellikler |
|---|---|---|---|
| **Sırt Üstü (Tandem)** | 10 - 20 | 10 - 15 | Hayvanı tek tek izleme kolaylığı. |
| **Balık Kılçığı (Herringbone)** | 40 - 150 | 25 - 45 | Orta ölçekli sürüler için altın standart. |
| **Paralel (Side-by-Side)** | 150 - 500 | 60 - 120 | Hızlı giriş-çıkış, yüksek operasyonel hız. |
| **Döner (Rotary)** | 500+ | 150 - 450 | Endüstriyel ölçek, yüksek yatırım, az işçilik. |
| **Robotik (VMS)** | 40 - 70 (Unit) | Otomatik | 24 saat sağım, yüksek veri analitiği. |

---

## 🌾 2. Yem Hazırlama ve Dağıtım | TMR Wagons

TMR (Tam Karışım Rasyonu) hazırlarken homojenlik (Peet-Wheel testi) esastır.

### Rasyon Mikser Vagonu (TMR Wagon)
- **Kapasite Hesabı:** Ortalama 1 m³ kapasite ≈ 6-8 sağmal inek (günlük 2 servis için).
- **Helezon Tipleri:** 
    - **Dikey (Vertical):** Uzun lifli kaba yemleri parçalamada üstün.
    - **Yatay (Horizontal):** Daha homojen karışım, daha hassas tartım.
- **Kritik Özellik:** Tartım sistemi (Load cells) kesinlikle hassas (±1kg) olmalıdır.

---

## ❄️ 3. Süt Soğutma ve Depolama | Milk Cooling

Sütün sağım sonrası ilk 2 saat içinde +4°C'ye düşürülmesi bakteri üremesini (SHS) önlemek için şarttır.

- **Tank Kapasitesi:** 2 günlük (4 sağım) toplam süt veriminin %20 fazlası olmalıdır.
- **Plakalı Soğutucu (Plate Heat Exchanger):** Sütü tanka girmeden önce kuyu suyu ile soğutarak enerji tasarrufu (%30-50) sağlar.
- **İnverter Kompresör:** Elektrik tüketimini optimize eder.

---

## 📡 4. Akıllı Tarım ve Sensörler | Precision Farming

| Teknoloji | Fonksiyon | ROI (Yıl) |
|---|---|---|
| **Aktivite Tasması (Collar)** | Kızgınlık takibi, geviş sayma | 1.5 - 2.5 |
| **Rumen pH Bolusu** | Beslenme (Asidoz) takibi | 2.0 - 3.0 |
| **Akıllı Süt Ölçer** | Süt verimi, iletkenlik (Mastitis) | 1.0 - 2.0 |
| **Buzağı Emzirme Robotu** | Otomatik buzağı besleme | 3.0+ |

---

## 🛠️ 5. Bakım ve Servis | Maintenance SOP

- **Pulsatör:** 6 ayda bir teknik servis kontrolü.
- **Süt Lastikleri (Liners):** 2500 sağımda bir (veya 6 ay) değişim şarttır.
- **Vakum Pompası:** Yağ seviyesi ve kayış gerginliği her ay kontrol edilmelidir.

📄 **İlgili Yazılım → [scripts/ration_calculator.py](file:///g:/Di%C4%9Fer%20bilgisayarlar/Diz%C3%BCst%C3%BC%20Bilgisayar%C4%B1m/github%20repolar%C4%B1m/BeyazYaka-Hayvancilik-101/scripts/ration_calculator.py)** (Maliyet analizi için)
