from ultralytics import YOLO

# 1. Adım: Önceden eğitilmiş temel modeli indir ve yükle (YOLOv8 Nano)
model = YOLO('yolov8n.pt')

# 2. Adım: Eğitimi başlat
print("Eğitim başlıyor! RTX 2070 Super...")

results = model.train(
    data='data.yaml',     # Veri setimizin kimlik dosyası
    epochs=50,            # Tüm resimleri 50 kere baştan sona incele
    imgsz=640,            # Resimleri 640x640'a ölçekle (standart)
    batch=16,             # VRAM'i taşırmamak için tek seferde 16 resim al
    device=0,             # 0 numaralı GPU'yu (Senin RTX'i) kullan
    name='tank_modeli',   # Sonuçların kaydedileceği klasörün adı
    plots=True            # Eğitim bitince başarı grafiklerini (loss vb.) çizdir
)

print("Eğitim tamamlandı! Sonuçlar 'runs/detect/tank_modeli' klasörüne kaydedildi.")