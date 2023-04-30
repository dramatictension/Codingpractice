alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

keepgoing = True

def cipher(inputtext, shiftamount, cipher_direction):
    
  ciphertext = ""
  for letter in inputtext:
    if letter in alphabet:
        position = alphabet.index(letter)
        if cipher_direction == "encode":
            newposition = position + shiftamount
        elif cipher_direction == "decode":
            newposition = position - shiftamount
        newletter = alphabet[newposition]
        ciphertext += newletter
    else:
       ciphertext += letter
  print(f"Your {cipher_direction}d text is {ciphertext}")
     

while keepgoing == True:
    keepgoing = False
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    cipher(inputtext=text, shiftamount=shift, cipher_direction=direction,)
    print("Keep going? Y or N")
    query = input("").lower()
    if query == "y":
     keepgoing = True
    else:
        keepgoing = False
        print("Thanks for using me!")