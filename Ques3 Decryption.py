'''github repo link https://github.com/AhmedCDU/Softwarenow.git'''

#Decryption

def decrypt(text, key):
    decrypted_text = ""

    for char in text:
        if char.isalpha():
            shifted = ord(char) - key

            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26

            decrypted_text += chr(shifted)
        else:
            decrypted_text += char

    return decrypted_text

# Encrypted code
encrypted_code = "tybony inevnoyr = 100\n\nzl_qvpg = ('xr11': 'inyhr1', 'xr12': 'inyhr2', 'xr13': 'inyhr3']\n\nqrs cebprff_ahzoref():\n\n   tybony tybony_inevnoyr\n   ybpny inevnoyr = 5 \n   ahzoref [1, 2, 3, 4, 5]\n\n  juvyr ybpny inevnoyr > 0:\n     vs ybpny inevnoyr % 2 == 0: \n        ahzoref.erzbir(ybpny_inevnoyr) \n     ybpny inevnoyr -= 1\n\n  erghea ahzoref\n\nzl_frg {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}\nerfhyg cebprff_ahzoref(ahzoref=zl_frg)\n\nqrs zbqvs1_qvpg():\n\n   ybpny_inevnoyr - 10 \n   zl_qvpg['xr14'] ybpny inevnoyr\n\nzbqvsl_qvpg(5)\n\nqrs heangr tybony(): \n   tybony tybony_inevnoyr \n   tybony_inevnoyr += 10\n\nsbe v va enatr(5): \n   cevag(v)\n   V+= 1\n\nvs zī_frg vf abg Abar naq z1_qvpg['xr14'] ==10: \n   cevag('Pbaqvgvba zrg!')\n\nvs 5 abg va zl_qvpg: \n   cevag('5 abg sbhaq va gur qvpgvbanel!')\n\ncevag(tybony_inevnoyr)\ncevag(z1_qvpg)\ncevag(zl_frg)"

# Key used for encryption
key = 13

# Decrypt the code
decrypted_code = decrypt(encrypted_code, key)

# Display the decrypted code
print(decrypted_code)

