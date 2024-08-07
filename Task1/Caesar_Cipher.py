def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    shift = shift % 26  # Normalize the shift to be within the range of the alphabet

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase letters separately
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            # Shift the character and wrap around if necessary
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            # Non-alphabetic characters are added as is
            result += char

    return result

def main():
    while True:
        mode = input("Enter mode (encrypt/decrypt) or 'exit' to quit: ").lower()
        if mode == 'exit':
            break
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")
            continue
        
        text = input("Enter the message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value! Please enter an integer.")
            continue

        result = caesar_cipher(text, shift, mode)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
