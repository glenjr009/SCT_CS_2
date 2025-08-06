from PIL import Image
import os

# --- My image encryption tool ---

def encrypt_with_xor(image_path, key):
    """Encrypts an image using a basic XOR cipher."""
    try:
        img = Image.open(image_path)
        img = img.convert("RGB") 
        width, height = img.size
        
        output_img = Image.new('RGB', (width, height))
        
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                
                # XOR the pixel values with our key
                new_r = r ^ key
                new_g = g ^ key
                new_b = b ^ key
                
                output_img.putpixel((x, y), (new_r, new_g, new_b))
        
        output_path = f"encrypted_{os.path.basename(image_path)}"
        output_img.save(output_path)
        print(f"Image encrypted with XOR. Saved as {output_path}")
        return output_path

    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def decrypt_with_xor(image_path, key):
    """Decrypts a XOR-encrypted image."""
    # XOR decryption is the same as encryption
    return encrypt_with_xor(image_path, key)


def encrypt_swap_channels(image_path):
    """Encrypts by swapping pixel channels (e.g., RGB to GBR)."""
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")
        width, height = img.size
        
        swapped_img = Image.new('RGB', (width, height))
        
        for y in range(height):
            for x in range(width):
                r, g, b = img.getpixel((x, y))
                
                # Simple swap of the color channels
                swapped_img.putpixel((x, y), (g, b, r))
        
        output_path = f"channels_swapped_{os.path.basename(image_path)}"
        swapped_img.save(output_path)
        print(f"Image channels swapped. Saved as {output_path}")
        return output_path

    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# --- Main part of the script ---
if __name__ == "__main__":
    
    input_file = "test_image2.jpeg" #Add the image name as per yours in the exact same folder where the source code is present
    input_file = "test_image.jpeg"
    input_file = "test_image3.jpeg"
    encryption_key = 123
    
    # Let's try the XOR encryption and decryption
    print("\n--- Running XOR Cipher ---")
    encrypted_file_path = encrypt_with_xor(input_file, encryption_key)
    if encrypted_file_path:
        decrypt_with_xor(encrypted_file_path, encryption_key)
    
    print("\n--- Running Channel Swapper ---")
    # This encryption is also its own decryption
    swapped_file_path = encrypt_swap_channels(input_file)
    if swapped_file_path:
        encrypt_swap_channels(swapped_file_path)