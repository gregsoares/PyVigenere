# Get key and plaintext from file
# Encipher
# Print Play text then Cipher text
# Decipher
# Print result from Decipher

# import string
# import sys
import string

from builtins import sum


def readFile(file):  # Takes in a file and returns its content
    fp = open('sample2_modified.txt', 'r')
    text_file = fp.read()
    # print(fileText)
    return text_file


def writeToFile(file, textInput):  # Writes to the specified file(creates it if it doesn't exist)
    fp = open(file, 'w')
    fp.write(textInput)
    #    print(fileText)
    fp.close()
    # counter = counter+1

    # C : ith letter of cipher
    # p : ith leter of plain_text
    # k : jth letter of key
    # %26 : remainder after dividing by 26
    # c = (p+k)%26


# def shift(letter, num):
#    letter_num = ord(letter)
#    num_mod = num%26
#    shifted = (letter_num + num_mod)
#    shifted = (shifted%26)+65
#    cipher = chr(shifted)
#    return cipher

def encode(plain_text, key):  # Take in a list and encode with hardcoded key
    letter_num = ord(plain_text)
    num_mod = key % 26
    shifted = (letter_num + num_mod)
    shifted = (shifted % 26) + 65
    cipher = chr(shifted)
    return cipher


# Take in a cipher_text and a key ==> (cipher_text[i] - key[i])+65 then cast to chr and return.
def decode(cipher_text, key):
    temp = ord(cipher_text)

    mod_num = (temp - key)

    if (mod_num < 0):  # If mod_num < 0 then add 26 and keep going with decoding
        mod_num = mod_num + 26
    dec_letter = chr((mod_num + 65))
    # print(dec_letter)
    return dec_letter


def LetterFreq(txt):
    c = 0
    sum = 0
    # txt = str.strip((str(txt)))
    del txt[0]
    letter_dict = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0,
                   'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0,
                   'Y': 0, 'Z': 0}
    pos_zero = dict(letter_dict)
    pos_one = dict(letter_dict)
    # print('\n \t\t --------INCOMING TXT IN FRQ --------\n {}'.format(txt))
    for letter in txt:
        if (letter.isalpha()) and letter in letter_dict:
            if (c % 2) == 0:
                pos_zero[letter] += 1
                letter_dict[letter] += 1
            else:
                pos_one[letter] += 1
                letter_dict[letter] += 1
        c = c + 1
    # sum += letter_dict.values()
    # letter_dict = letter_dict.sort()
    print(letter_dict)
    print('Total letters counted: {}'.format(sum))
    #for k, v in letter_dict.items():
#    print('Total letter count: \t Group 0 Letter count: \t Group 1 letter count: \n' +
#              '\n{}: {} \t\t {}: {} \t\t{}: {}\n'.format(letter_dict.items(),letter_dict.values(),pos_zero.keys(),pos_zero.values(),pos_one.keys(),pos_one.values()))
    print('\t --- POSITION 0 FREQUENCY: ---\n {}'.format(pos_zero))
    print('\t --- POSITION 1 FREQUENCY: ---\n {}'.format(pos_one))
    print('\t --- Values POS 1: ---\n {}'.format(pos_one.values()))

    return letter_dict


def main():
    plaintext = readFile("sample2_modified.txt")
    key = [72, 73]
    to_cipher = []
    counter = 0
    cipher_text = []

    for element in plaintext:  # Turns each letter to uppercase and adds it to: to_cipher
        if element.isalpha():
            element = element.upper()
            # print(element)
            # plaintext.index(counter) = element
            to_cipher.append(element)
        else:
            to_cipher.append(element)
    # Testing the above loop
    # print(to_cipher)

    print("\nLength of original message: %d \t -------------\n Length of to_cipher: %d" % (
    len(plaintext), len(to_cipher)))
    print("\nUpper case of Plain Text: ")
    for word in range(1, len(to_cipher)):
        print(to_cipher[word], end='')

    print("\nPrinting cipher_text: ")
    for letter in to_cipher:
        if (counter % 2) == 0:
            cipher_letter = encode(letter, key[0])
        else:
            cipher_letter = encode(letter, key[1])
        print(cipher_letter, end='')
        cipher_text.append(cipher_letter)
        counter = counter + 1
    decrypted = []
    c = 0
    print('\n\n --- Calling Decrypt function: ')
    for letter in cipher_text:
        if (letter.isalpha()) == True:
            if (c % 2) == 0:
                decrypted.append(decode(letter, key[0]))
            else:
                decrypted.append(decode(letter, key[1]))
            c = c + 1
    for _ in decrypted: print(_, end=''),
    print('\n\t--- Length of decrypted message: {}'.format(len(decrypted)))

    print('\n --- Calling LetterFreq():')
    let_freq = LetterFreq(to_cipher)
    cipher_word_count = dict(let_freq)
    print('\nCipher text word count: \n')
    print(cipher_word_count)

    # for word in range(1, len(decrypted)):
    #    print(decrypted[word], end='')


main()
