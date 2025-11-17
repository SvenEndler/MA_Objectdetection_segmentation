import os
import shutil
import random
from glob import glob
from tqdm import tqdm

# ====== Pfade anpassen ======
images_root = r"C:\Users\seven\Desktop\Masterarbeit\Bearbeitung\Masterarbeit\Test\Piktogramme\images"
labels_root = r"C:\Users\seven\Desktop\Masterarbeit\Bearbeitung\Masterarbeit\Test\Piktogramme\labels"
output_images = r"C:\Users\seven\Desktop\Masterarbeit\Bearbeitung\Masterarbeit\Test\Piktogramme\train_data_2\images"
output_labels = r"C:\Users\seven\Desktop\Masterarbeit\Bearbeitung\Masterarbeit\Test\Piktogramme\train_data_2\labels"
# =============================

train_ratio = 0.8  # 80 % Train / 20 % Val

# Zielstruktur erstellen
for split in ["train", "val"]:
    os.makedirs(os.path.join(output_images, split), exist_ok=True)
    os.makedirs(os.path.join(output_labels, split), exist_ok=True)

# Zufälligkeit reproduzierbar machen (optional)
random.seed(42)

# Alle Kartenordner ermitteln
map_names = [d for d in os.listdir(images_root) if os.path.isdir(os.path.join(images_root, d))]
map_names.sort()

print("🚀 Erstelle Trainings- und Validierungsdatensatz pro Karte...\n")

for map_name in tqdm(map_names):
    image_dir = os.path.join(images_root, map_name)
    label_dir = os.path.join(labels_root, map_name)

    image_paths = glob(os.path.join(image_dir, "*.png"))
    if not image_paths:
        print(f"⚠️  Keine Bilder in {map_name} gefunden, überspringe...")
        continue

    # Shuffle & Split
    random.shuffle(image_paths)
    split_idx = int(len(image_paths) * train_ratio)
    train_imgs = image_paths[:split_idx]
    val_imgs = image_paths[split_idx:]

    def copy_pairs(img_list, split_name):
        for img_path in img_list:
            base = os.path.splitext(os.path.basename(img_path))[0]
            lbl_path = os.path.join(label_dir, f"{base}.txt")

            # Zielpfade
            img_dst = os.path.join(output_images, split_name, f"{map_name}_{base}.png")
            lbl_dst = os.path.join(output_labels, split_name, f"{map_name}_{base}.txt")

            # Dateien kopieren
            shutil.copy(img_path, img_dst)
            if os.path.exists(lbl_path):
                shutil.copy(lbl_path, lbl_dst)
            else:
                print(f"⚠️  Kein Label für {img_path}")

    copy_pairs(train_imgs, "train")
    copy_pairs(val_imgs, "val")

print("\n✅ Fertig!")
print(f"Train/Val-Split (80/20) erstellt in:")
print(f"  📁 {output_images}")
print(f"  📁 {output_labels}")
