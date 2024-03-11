from PIL import Image

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size
    
    # Convert image to RGB mode
    img = img.convert("RGB")
    
    # Encrypt each pixel
    pixels = img.load()
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[x, y] = (r, g, b)
    
    # Save encrypted image
    encrypted_image_path = image_path.split('.')[0] + '_encrypted.png'
    img.save(encrypted_image_path)
    print("Image encrypted successfully!")
    return encrypted_image_path

def decrypt_image(image_path, key):
    # Open the encrypted image
    img = Image.open(image_path)
    width, height = img.size
    
    # Convert image to RGB mode
    img = img.convert("RGB")
    
    # Decrypt each pixel
    pixels = img.load()
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[x, y] = (r, g, b)
    
    # Save decrypted image
    decrypted_image_path = image_path.split('_encrypted.')[0] + '_decrypted.png'
    img.save(decrypted_image_path)
    print("Image decrypted successfully!")
    return decrypted_image_path

def main():
    while True:
        print("\n1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            image_path = input("Enter path to image file: ")
            key = int(input("Enter encryption key: "))
            encrypted_image_path = encrypt_image(image_path, key)
            print("Encrypted image saved at:", encrypted_image_path)
        elif choice == '2':
            image_path = input("Enter path to encrypted image file: ")
            key = int(input("Enter decryption key: "))
            decrypted_image_path = decrypt_image(image_path, key)
            print("Decrypted image saved at:", decrypted_image_path)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
