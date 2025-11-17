import cv2
import os
import numpy as np
from glob import glob
from PIL import Image

def tile_jpg_to_png(jpg_path, output_dir, tile_size=1024):
    base_name = os.path.splitext(os.path.basename(jpg_path))[0]
    tile_dir = os.path.join(output_dir, base_name)
    os.makedirs(tile_dir, exist_ok=True)

    img = cv2.imread(jpg_path)
    if img is None:
        print(f"Bild konnte nicht geladen werden: {jpg_path}")
        return

    height, width = img.shape[:2]
    count = 0

    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            w = min(tile_size, width - x)
            h = min(tile_size, height - y)

            tile = img[y:y+h, x:x+w]
            tile_rgb = cv2.cvtColor(tile, cv2.COLOR_BGR2RGB)

            # PADDING, falls Tile kleiner ist als 1024x1024
            if w < tile_size or h < tile_size:
                padded_tile = np.zeros((tile_size, tile_size, 3), dtype=np.uint8)
                padded_tile[0:h, 0:w] = tile_rgb
                tile_rgb = padded_tile

            out_path = os.path.join(tile_dir, f"{base_name}_tile_{count:05}.png")
            Image.fromarray(tile_rgb).save(out_path)
            count += 1

    print(f"✅ {count} Tiles aus {base_name} gespeichert in {tile_dir}")

input_folder = r"C:/Users/seven/Desktop/Masterarbeit/Bearbeitung/Masterarbeit/Test/evaluation/The Big Ten Academic Alliance"
output_folder = r"C:/Users/seven/Desktop/Masterarbeit/Bearbeitung/Masterarbeit/Test/evaluation/hist_pikto"

# Alle JPG-Dateien im Input-Ordner verarbeiten
jpg_files = glob(os.path.join(input_folder, "*.jpg"))

for jpg_path in jpg_files:
    tile_jpg_to_png(jpg_path, output_folder, tile_size=1024)

