import os
import json
import shutil

# Dosya yollarını kendi bilgisayarına göre ayarla
input_dir = r"D:\tankaidataset\solo"
output_dir = r"D:\yolo_dataset"

# YOLO için gerekli klasör yapısını oluşturuyoruz
os.makedirs(f"{output_dir}/images/train", exist_ok=True)
os.makedirs(f"{output_dir}/labels/train", exist_ok=True)

img_counter = 0

print("Dönüştürme işlemi başlıyor, lütfen bekleyin...")

# Bütün sequence klasörlerini tek tek geziyoruz
for folder_name in os.listdir(input_dir):
    folder_path = os.path.join(input_dir, folder_name)
    
    if not os.path.isdir(folder_path):
        continue

    # JSON ve Resim dosyalarının yollarını belirliyoruz
    json_path = os.path.join(folder_path, "step0.frame_data.json")
    img_path = os.path.join(folder_path, "step0.camera.png")

    if not os.path.exists(json_path) or not os.path.exists(img_path):
        continue

    # JSON dosyasını okuyoruz
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    try:
        capture = data["captures"][0]
        img_width, img_height = capture["dimension"]
        annotations = capture["annotations"][0]["values"]
    except (KeyError, IndexError):
        continue  # JSON yapısında eksik varsa bu klasörü atla

    # Dosyaları YOLO klasörüne taşırken yeniden isimlendiriyoruz (tank_0, tank_1 vb.)
    new_name = f"tank_{img_counter}"
    new_img_path = os.path.join(output_dir, "images", "train", f"{new_name}.png")
    new_txt_path = os.path.join(output_dir, "labels", "train", f"{new_name}.txt")

    # Resmi yeni klasöre kopyala
    shutil.copy(img_path, new_img_path)

    # YOLO txt dosyasını oluştur ve matematiği uygula
    with open(new_txt_path, 'w') as txt_file:
        for ann in annotations:
            x_min, y_min = ann["origin"]
            box_w, box_h = ann["dimension"]

            # YOLO Normalizasyon Matematiği
            x_center = (x_min + (box_w / 2.0)) / img_width
            y_center = (y_min + (box_h / 2.0)) / img_height
            w_norm = box_w / img_width
            h_norm = box_h / img_height

            class_id = 0 # Tek sınıfımız var (Tank), YOLO 0'dan başlar

            # txt dosyasına satırı yazıyoruz
            txt_file.write(f"{class_id} {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}\n")
    
    img_counter += 1

print(f"İşlem tamamlandı! Toplam {img_counter} adet resim ve etiket D:\\yolo_dataset klasörüne kaydedildi.")