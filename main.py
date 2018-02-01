# Get key and plaintext from file
# Encipher
# Print Play text then Cipher text
# Decipher
# Print result from Decipher

# import sys


def readFile(file):  # Takes in a file and returns its content
    fp = open('sample2_modified.txt', 'r')
    fileText = fp.read()
    print(fileText)
    return fileText


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

def shift(letter, num):
    letter_num = ord(letter)
    num_mod = num%26
    shifted = (letter_num + num_mod)
    shifted = (shifted%26)+65
    cipher = chr(shifted)
    return cipher
    
def encode(plain_text,key):  # Take in a list and encode with hardcoded key
    c = 0
    cipher_text = []
    plain = []
    plain.extend(plain_text)    

    # If the letter is in an even position in the array then use the first key letter, else use the second
    for item in plain:
        if (c % 2) == 0:
            temp_res = shift(item,key[0])
            cipher_text.append(temp_res)
            c = c + 1

        else:
            temp_res = shift(item,key[1])
            cipher_text.append(temp_res)
            c = c + 1
    return cipher_text

# Take in a cipher_text and a key ==> (cipher_text[i] - key[i])+65 then cast to chr and return.
def decode(cipher_text,in_key):
    key = []
    key.extend(in_key)
    decoded = []
    mod_num = 0
    c = 0;
    print (key[c])
    c +=1
    print (key[c])
    for letter in cipher_text:
        temp = ord(letter)
        # num_key = int(key[c])
        temp = int(temp)
        new_temp = temp - num_key
        if (new_temp < 0): # If temp < 0 then add 26 and keep going with decoding
            new_temp = temp + 26
        dec_letter = chr(temp + 65)
        decoded.append(dec_letter)
        if (c == len(key)): # If at the end of the key array then reset key[i]
            c = 0
        else:
            c = c+1
    return decoded




    

def main():
    plaintext = readFile("sample2_modified.txt")
    key = [72,73]
    to_cipher = []
    counter = 0

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
    # print("Length of original message: %d \t -------------\n Length of to_cipher: %d"%(len(plaintext),len(to_cipher)))
    print("\n\nUpper case of Plain Text: ")
    for word in range(1, len(to_cipher)):
        print(to_cipher[word], end='')

    print("\n\nPrinting cipher_text: ")
    cipher_text = encode(to_cipher,key)
    for word in range(1, len(cipher_text)):
        print(cipher_text[word], end='')
    print('')
    #print ((len(cipher_text)))
    #print ((len(to_cipher)))
    
    print ('Calling Decrypt function: \n')
    decrypted = decode(cipher_text,key)

    for word in range(1, len(decrypted)):
        print(decrypted[word], end='')
    
main()
