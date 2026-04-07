# Mastitis Yönetim Protokolü | Mastitis Management Protocol
## Süt İşletmelerinde Ekonomik Kayıpların Önlenmesi İçin Teknik Rehber

> **TR:** Mastitis, dünya çapında süt sığırcılığı işletmelerinin en büyük ekonomik gider kalemidir. Bu protokol, klinik ve subklinik mastitisin tespiti, tedavisi ve en önemlisi önlenmesi için standart operasyon prosedürlerini (SOP) içerir.
>
> **EN:** Mastitis is the largest economic burden for dairy farms worldwide. This protocol contains SOPs for detection, treatment, and prevention of clinical and subclinical mastitis.

---

## 🔬 1. Tanı ve Tespit | Detection & Diagnosis

### 1.1 Klasik Belirtiler (Klinik Mastitis)
- **Meme:** Şişkinlik, kızarıklık, ısı artışı, ağrı (dokunmaya hassasiyet).
- **Süt:** Pıhtılı, kanlı, su renginde veya sarımtırak görünüm.
- **Hayvan:** Ateş, iştahsızlık, çökme (Sistemik form).

### 1.2 Subklinik Mastitis (Görünmez Tehlike)
- Gözle görülür bir belirti yoktur.
- **Somatik Hücre Sayısı (SHS):** > 200,000 hücre/mL.
- **California Mastitis Test (CMT):** Sağım öncesi her memeden alınan numunelerle pıhtılaşma kontrolü.

| CMT Skoru | Anlamı | Yaklaşık SHS (bin/mL) |
|---|---|---|
| **0 (Negatif)** | Sağlıklı | < 100 |
| **İz (Trace)** | Şüpheli / İyileşiyor | 150 - 500 |
| **1 (Hafif)** | Subklinik Mastitis | 500 - 1,500 |
| **2 (Orta)** | Klinik Öncesi | 1,500 - 5,000 |
| **3 (Şiddetli)** | Akut/Klinik | > 5,000 |

---

## 🐄 2. Sağım Hijyeni — 6 Adım Kuralı | Milking Hygiene

Sağım sırasında çapraz bulaşmayı önlemek için aşağıdaki adımlar her sağımda tavizsiz uygulanmalıdır:

1. **Ön Sağım (Forestripping):** Memeden ilk 2-3 damla sütün siyah bir kaba (Strip Cup) sağılması. Pıhtı kontrolü ve süt kanallarındaki bakterilerin atılması.
2. **Pre-dip (Ön Dezenfeksiyon):** Memelerin hızlı etkili bir dezenfektan (Daldırma kabı) ile ıslatılması. 30 saniye beklenmelidir.
3. **Kurulama:** Her hayvan için **ayrı ve temiz** bir kâğıt havlu veya dezenfekte edilmiş bez kullanılarak memelerin kurulanması.
4. **Sağım Başlığı Takma:** Hava emilmeden başlıkların takılması.
5. **Sağım Sonu Kontrolü:** Başlıkların "over-milking" (fazla sağım) yapmadan, vakum kesilerek çıkarılması.
6. **Post-dip (Son Dezenfeksiyon):** Sağım sonrası memelerin koruyucu bir film tabakası oluşturan dezenfektana daldırılması. **Kritik:** Sfingter kası 30 dk boyunca açık kalır; hayvanın yatması önlenmelidir (taze yem verilerek).

---

## 💊 3. Tedavi Yaklaşımı | Treatment Approach

> [!CAUTION]
> Tüm antibiyotik tedavileri Veteriner Hekim kontrolünde ve **Süt/Et Arınma Süreleri (Withdrawal Period)** gözetilerek yapılmalıdır.

### 3.1 Hafif Vakalar
- Siklik sağım (Memenin 2-3 saatte bir tamamen boşaltılması).
- Destekleyici vitamin/mineral takviyesi.

### 3.2 Şiddetli (Klinik) Vakalar
- **Kültür ve Duyarlılık Testi:** Hangi bakterinin (E.coli, Staph. aureus, Strep. uberis) olduğunu tespit et.
- **Meme İçi Antibiyotik:** Meme kanalı yoluyla uygulama.
- **Sistemik Antibiyotik:** Kas içi veya damar yoluyla (Veteriner kontrolünde).
- **Anti-inflamatuar:** Ağrı ve ateşi düşürmek için.

---

## 🛡️ 4. Korunma Stratejileri | Prevention

1. **Kuru Dönem Tedavisi (DCT):** Laktasyon sonunda her hayvanın memesine koruyucu antibiyotik/mühürleyici uygulanması.
2. **Kronik Vakaların Eliminasyonu:** Tedaviye yanıt vermeyen "Portör" hayvanların sürüden çıkarılması.
3. **Ekipman Bakımı:** Sağım makinesinin vakum ve nabız (pulsator) ayarlarının 6 ayda bir kalibre edilmesi.
4. **Yataklık Yönetimi:** Hayvanların yattığı yerlerin kuru ve temiz (kum veya temiz sap) tutulması.

---

## 📊 Mastitis Analiz Tablosu (Örnek)

| Parametre | Hedef | Alarm Seviyesi |
|---|---|---|
| **Sürü Ortalama SHS** | < 150,000 | > 250,000 |
| **Yıllık Yeni Vaka Oranı** | < %20 | > %40 |
| **Kuru Dönem Başarı Oranı** | > %85 | < %70 |
| **Süt Kaybı (SHS 500k vs 100k)** | - | %10 Kayıp / İnek |

📄 **İlgili Yazılım → [scripts/herd_health_tracker.py](file:///g:/Di%C4%9Fer%20bilgisayarlar/Diz%C3%BCst%C3%BC%20Bilgisayar%C4%B1m/github%20repolar%C4%B1m/BeyazYaka-Hayvancilik-101/scripts/herd_health_tracker.py)**
