import sys
try:
    from PIL import Image
    
    def crop_transparent(img_path, save_path):
        img = Image.open(img_path)
        bbox = img.getbbox()
        if bbox:
            cropped = img.crop(bbox)
            w, h = cropped.size
            sz = max(w, h)
            square = Image.new('RGBA', (sz, sz), (0, 0, 0, 0))
            offset = ((sz - w) // 2, (sz - h) // 2)
            square.paste(cropped, offset)
            square.save(save_path)
            print("Cropped and saved to", save_path)
        else:
            print("Image is entirely transparent.")
            
    crop_transparent("../Imputs/Juanchi Notion Avatar Transparente.png", "../Imputs/favicon.png")
except ImportError:
    print("Pillow not installed.")
