##Get key and plaintext from file

##Encipher

#Print Play text then Cipher text

##Decipher

#Print result from Decipher

from urllib import request
import sys


def readFile(file): #Takes in a file and returns its content
    fp = open('sample2_modified.txt', 'r')
    fileText = fp.read()
    print(fileText)
    fp.close()
    return fileText

def writeToFile(file, textInput): #Writes to the specified file(creates it if it doesn't exist)
    fp = open(file, 'w')
    fp.write(textInput)
    #    print(fileText)
    fp.close()
    #counter = counter+1

#C : ith letter of cipher
#p : ith leter of plain_text
#k : jth letter of key
#%26 : remainder after dividing by 26
#c = (p+k)%26
def encode(plain_text): #Take in a list and encode with hardcoded key
    key = ['H','I']
    plain = []
    c = 0
    cipher_text = []
    #plain_text.append('L')
    if (len(plain_text))%2 != 0:
        plain_text.append('X')
        print('Last value in plain_text: %s'%(plain_text[-1]))

    #print (ord('a')+ord('b')) turning char into int
    for item in plain_text:
        plain.append(item)
        if (c%2) == 0:
            #cipher_text.append(chr((ord(item)+ord(key[0]))%26))
            print('H = 72  + %d = %s ' %((ord(plain_text.index(c))), item))
            print(' mod26(' + key[0] + ' + ' + plain_text.index(c) + '\) = ' + (((ord(item))+(ord(key[0]))) % 26))
            c = c+1

        else:
            print('H = 72  + %d = %s ' % (ord(plain_text.index(c)), item))
            print(' mod26(' + key[0] + ' + ' + plain_text.index(c) + '\) = ' + (((ord(item))+(ord(key[0]))) % 26))
            c = c+1
    return cipher_text





def main():
    plaintext = readFile("sample2_modified.txt")
    key = ['h', 'i']
    to_cipher = []
    counter = 0

    for element in plaintext: # Turns each letter to uppercase and adds it to: to_cipher
        if element.isalpha():
            element = element.upper()
            #print(element)
            #plaintext.index(counter) = element
            to_cipher.append(element)
        else:
            #print(element)
            to_cipher.append(element)
    #Testing the above loop
    #print(to_cipher)
    #print("Length of original message: %d \t -------------\n Length of to_cipher: %d"%(len(plaintext),len(to_cipher)))
    print ("\n\nUpper case of Plain Text: ")
    for word in range(1, len(to_cipher)):
        print(to_cipher[word],end='')

    print("\n\nPrinting cipher_text: ")
    cipher_text = encode(to_cipher)
    print (cipher_text)
main()

