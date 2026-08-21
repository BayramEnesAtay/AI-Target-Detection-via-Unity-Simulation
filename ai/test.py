from ultralytics import YOLO

# Kendi eğittiğimiz modelin beynini yüklüyoruz
model = YOLO('best.pt')

# İnternetten indirdiğimiz fotoğrafı modele gösteriyoruz
# conf=0.5 parametresi: "Eğer %50'den fazla eminsen kutu çiz" demektir.
# save=True parametresi: Çizdiği kutulu fotoğrafı bilgisayara kaydetmesini sağlar.
results = model.predict(source='tank.jpg', save=True, conf=0.5)

print("Test tamamlandı! Kutulu fotoğraf 'runs/detect/predict' klasörünün içine kaydedildi.")