'''github repo link https://github.com/AhmedCDU/Softwarenow.git'''
def separate_and_convert(input_string):
    # Separate the string into number and letter substrings
    number_string = ''.join([char for char in input_string if char.isdigit()])
    letter_string = ''.join([char for char in input_string if char.isalpha()])

    print("Number String:", number_string)
    print("Letter String:", letter_string)

    # Convert even numbers in the number string to ASCII Code Decimal Values
    even_numbers = [int(num) for num in number_string if int(num) % 2 == 0]
    ascii_codes_numbers = [ord(str(even)) for even in even_numbers]

    print("Even Numbers:", even_numbers)
    print("ASCII Code Decimal Values for Even Numbers:", ascii_codes_numbers)

    # Convert upper-case letters in the letter string to ASCII Code Decimal Values
    upper_case_letters = [char for char in letter_string if char.isupper()]
    ascii_codes_letters = [ord(upper) for upper in upper_case_letters]

    print("Upper-case Letters:", upper_case_letters)
    print("ASCII Code Decimal Values for Upper-case Letters:", ascii_codes_letters)


def decrypt_cryptogram(cryptogram, shift_key):
    decrypted_text = ''
    for char in cryptogram:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - base - shift_key) % 26 + base)
        else:
            decrypted_text += char
    return decrypted_text


# Example 1
string_example = '56aAww1984sktr235270aYmn145ss785fsq31D0'
print("Example 1:")
separate_and_convert(string_example)

# Example 2
cryptogram_example = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
print("\nExample 2:")
for shift_key in range(26):
    decrypted_text = decrypt_cryptogram(cryptogram_example, shift_key)
    print(f"Shift Key {shift_key}: {decrypted_text}")
