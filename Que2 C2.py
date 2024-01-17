'''github repo link https://github.com/AhmedCDU/Softwarenow.git'''

def separate_and_convert(input_string):
    # Separate into number and letter substrings
    number_string = ''.join([char for char in input_string if char.isdigit()])
    letter_string = ''.join([char for char in input_string if char.isalpha()])

    # Convert even numbers in the number substring to ASCII Code Decimal Values
    even_numbers = [int(num) for num in number_string if int(num) % 2 == 0]
    ascii_values_numbers = [ord(str(num)) for num in even_numbers]

    # Convert upper-case letters in the letter substring to ASCII Code Decimal Values
    upper_case_letters = [char for char in letter_string if char.isupper()]
    ascii_values_letters = [ord(char) for char in upper_case_letters]

    return number_string, letter_string, ascii_values_numbers, ascii_values_letters


# Example usage
input_string = '56aAww1984sktr235270aYmn145ss785fsq31D0'
result = separate_and_convert(input_string)

print("Number String:", result[0])
print("Letter String:", result[1])
print("ASCII Values of Even Numbers:", result[2])
print("ASCII Values of Upper-case Letters:", result[3])

# Decrypting cryptogram

def decrypt_cryptogram(cryptogram, shift_key):
    decrypted_quote = ''
    for char in cryptogram:
        if char.isalpha():
            if char.isupper():
                decrypted_quote += chr((ord(char) - shift_key - ord('A')) % 26 + ord('A'))
            else:
                decrypted_quote += chr((ord(char) - shift_key - ord('a')) % 26 + ord('a'))
        else:
            decrypted_quote += char

    return decrypted_quote


# Example usage with the provided cryptogram
cryptogram = "VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY " \
             "NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF " \
             "URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR"
for shift in range(26):
    decrypted_text = decrypt_cryptogram(cryptogram, shift)
    print(f"Shift Key: {shift} - Decrypted Text: {decrypted_text}")
