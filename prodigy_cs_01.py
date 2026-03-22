def caesar_cipher(text, shift, mode):
    result = ""
    
    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def get_text():
    while True:
        text = input("Enter the text: ").strip()
        if text != "":
            return text
        else:
            print("Text cannot be empty. Try again.")


def get_shift():
    while True:
        try:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Shift must be between 1 and 25.")
        except ValueError:
            print("Invalid input! Enter a number.")


def main():
    print("=== Caesar Cipher Program ===")
    
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '3':
            print("Program Ended!")
            break
        
        elif choice == '1' or choice == '2':
            text = get_text()
            shift = get_shift()
            
            mode = "encrypt" if choice == '1' else "decrypt"
            result = caesar_cipher(text, shift, mode)
            
            print(f"\n{mode.capitalize()}ed Text: {result}")
        
        else:
            print("Invalid choice! Please select 1, 2 or 3.")


if __name__ == "__main__":
    main()