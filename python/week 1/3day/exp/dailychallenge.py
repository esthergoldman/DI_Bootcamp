# for letter in text:
#     cypher_text += chr(ord(letter) + 3)

#(x+n)%26 is for encryption
# (x-n)%26 is for decryption

def encripted(string,shift):
    ciper = ''
    for char in string:
        if char == '':
            ciper = ciper + char
        elif char.isupper():
            ciper = ciper + chr((ord(char)+shift-65)%26+65)
        else:
            ciper = ciper + chr((ord(char)+shift-65)%26+97)
    return ciper


text = input('enter the text')
s = int(input('enter the shift key'))
print ('the original string is:', text)
print('the encripted message is:',encripted(text,s))