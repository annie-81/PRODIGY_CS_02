from PIL import Image
def encrypt_image(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))
            r = min(r + 2, 255) 
            g = min(g + 2, 255)
            b = min(b + 2, 255)
            img.putpixel((x, y), (r, g, b))
    encrypted_image = "encrypted_image.png"
    img.save(encrypted_image)
    print("Image encrypted successfully!")
    return encrypted_image
def decrypt_image(encrypted_image):
    encrypted_img = Image.open(encrypted_image)
    width, height = encrypted_img.size
    for y in range(height):
        for x in range(width):
            r, g, b = encrypted_img.getpixel((x, y))
            r = max(r - 2, 0) 
            g = max(g - 2, 0)
            b = max(b - 2, 0)
            encrypted_img.putpixel((x, y), (r, g, b))
    encrypted_img.show()
image_path = "ocean-waves.jpg"  
encrypted_image = encrypt_image(image_path)
decrypt_image(encrypted_image)
