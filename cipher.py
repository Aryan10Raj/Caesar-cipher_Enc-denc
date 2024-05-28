
def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
            
        # Add non-alphabet characters unchanged
        else:
            result += char

    return result

def decrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Decrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)

        # Decrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
            
        # Add non-alphabet characters unchanged
        else:
            result += char

    return result

# Main logic
choice = input("Want to encrypt or decrypt (e/d): ").lower()
if choice not in ('e', 'd'):
    print("Wrong input")
else:
    text = input("Enter the message: ")
    s = int(input("Enter the shift value: "))
    
    if choice == 'e':
        print("Text: " + text)
        print("Shift: " + str(s))
        print("Cipher: " + encrypt(text, s))
    elif choice == 'd':
        print("Text: " + text)
        print("Shift: " + str(s))
        print("Cipher: " + decrypt(text, s))

    