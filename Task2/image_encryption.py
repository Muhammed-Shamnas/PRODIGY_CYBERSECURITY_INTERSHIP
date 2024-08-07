from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path):
    image = Image.open(image_path).convert("RGB")
    image_array = np.array(image)
    
    # Encrypt by adding 50 to each pixel value (simple example)
    encrypted_array = (image_array + 50) % 256  # Ensure values stay within valid range (0-255)
    
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(image_path, output_path):
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Decrypt by subtracting 50 from each pixel value
    decrypted_array = (image_array - 50) % 256  # Ensure values stay within valid range (0-255)
    
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Decrypted image saved as {output_path}")

def main():
    while True:
        mode = input("Enter mode (encrypt/decrypt) or 'exit' to quit: ").lower()
        if mode == 'exit':
            break
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")
            continue
        
        image_path = input("Enter the path of the image: ")
        output_path = input("Enter the output path for the processed image (including file name and extension): ")

        if mode == 'encrypt':
            encrypt_image(image_path, output_path)
        elif mode == 'decrypt':
            decrypt_image(image_path, output_path)

if __name__ == "__main__":
    main()
