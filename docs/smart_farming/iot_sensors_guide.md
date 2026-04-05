# Akıllı Hayvancılık İOT Sensörleri | Smart Farming IoT Sensors

Veri madenciliği, ahırın içindeki "gürültüyü" "bilgiye" dönüştürür.

## Sensör Tipleri ve Protokoller (TR)

| Sensör | Tip | Protokol | Kullanım Amacı |
| :--- | :--- | :--- | :--- |
| **Aktivite Sensörü** | İvmeölçer | BLE / LoRa | Kızgınlık ve Topallık Tespiti |
| **Rumen pH Bolusu** | Kimyasal Sensör | ISM Band | Asidoz (SARA) Erken Uyarısı |
| **THI Sensörü** | Nem/Isı | WiFi / RS485 | Sıcak Stresi Kontrolü |
| **Süt Sayacı** | Optik/Akış | Profinet | Verim ve Somatik Hücre Sayısı (SHS) |

### Teknoloji Seçimi (EN)

1. **LoRaWAN**: Uzun menzil (10-15km) ve düşük güç tüketimi için merada ideal.
2. **NB-IoT**: GSM altyapısı kullanarak hücresel bağlantı sağlar; küçük işletmeler için uygun.
3. **Edge AI**: Verinin buluta gitmeden cihaz üzerinde işlenmesi (Örn: Öksürük sesiyle hastalık tespiti).

---

## IoT Sensor Selection (EN)

1. **Activity Sensors**: Accelerometers for heat and lameness detection.
2. **Rumen pH Bolus**: Real-time monitoring of stomach acidity to prevent SARA.
3. **Environmental Sensors**: Tracking Temperature Humidity Index (THI).
