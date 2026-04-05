# Edge AI ile Hastalık Tespiti | Edge AI for Disease Detection

## Neden Edge AI?

Bulut tabanlı AI çiftlik ortamında birden fazla sorunla karşılaşır:
1. **Gecikme (Latency)**: Sürekli internet bağlantısı yok.
2. **Bant Genişliği**: Kamera görüntüleri GB/Gün tüketir.
3. **Maliyet**: Bulut işlem maliyeti yüksek.

**Edge AI** çözümü: Modeli sensörün yanındaki düşük güçlü bilgisayarda (Jetson Nano, Coral TPU, Pi 5) çalıştır.

## Pratik Kullanım Senaryoları

| Senaryo | Giriş Verisi | Model Tipi | Doğruluk |
|---|---|---|---|
| **Kızgınlık Tespiti** | Aktivite ivmesi (BLE) | Random Forest / LSTM | %88-94 |
| **Topallık Skoru** | Adım analizi (kamera) | CNN (MobileNet) | %85-91 |
| **Öksürük Tespiti** | Ses kaydı (mikrofon) | CNN + Spectrogram | %82-89 |
| **Vücut Kondisyon Skoru** | Kamera görüntüsü | ResNet/EfficientNet | %79-86 |

## Minimal Donanım Stack'i

```
Raspberry Pi 5 (8GB)         ← Koordinasyon ve MQTT yönetimi
+ Coral USB Accelerator      ← TensorFlow Lite model inferansı
+ 4G/LoRa Modülü             ← Uzak bölge bağlantısı
Maliyet: ~5,000 TL (2026)
```

## Öksürük Tespit Modeli: Adım Adım

```python
# Kütüphane: librosa (ses analizi), tflite-runtime (edge inference)
import librosa
import numpy as np

def extract_features(audio_path, sr=22050):
    y, sr = librosa.load(audio_path, sr=sr, duration=3.0)
    mel_spec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    log_mel = librosa.power_to_db(mel_spec, ref=np.max)
    return log_mel  # Shape: (128, time) → Model girdisi

# Eşik: Ses >75dB + frekans 200-800Hz + süre 0.2-0.6s → Öksürük adayı
```

## Kızgınlık Tespit Algoritması (Basit Versiyon)

```python
def detect_estrus(activity_data: list, baseline_avg: float) -> bool:
    """
    activity_data: Son 6 saatlik aktivite ölçümleri (adım/saat)
    baseline_avg: Hayvanın 21 günlük ortalama aktivitesi
    
    Kızgınlık: Aktivite > baseline_avg * 3.0 (200-300% artış)
    """
    peak_activity = max(activity_data)
    return peak_activity > (baseline_avg * 3.0)
```
