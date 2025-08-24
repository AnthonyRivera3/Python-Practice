#ceaser cypher
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']








# def encrypt(original_text, shift_ammount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_postion = alphabet.index(letter) + shift_ammount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_postion]
        
    
#     print(f"Here is the encoded result:{cipher_text}")

# def decrypt(original_text, shift_ammount):
#     decypher_text =""
#     for letter in original_text:
#         shifted_postion = alphabet.index(letter) - shift_ammount
#         shifted_position %= len(alphabet)
#         decypher_text += alphabet[shifted_postion]
#     print(f"Here is the decoded message: {decypher_text}")


def caesar(original_text, shift_ammount, encode_or_decode):
    decypher_text =""


    if encode_or_decode == 'decode':
            shift_ammount *=-1

            
    for letter in original_text:
        
        if encode_or_decode == 'exit':
            return 0

        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_ammount
            shifted_position %= len(alphabet)
            decypher_text += alphabet[shifted_position]
        else:
            decypher_text += letter
    
    if encode_or_decode == 'encode':
        print(f"Here is the encoded message: {decypher_text}")
    else:
        print(f"Here is the decoded message: {decypher_text}")
    
    



text = input("Type your message:\n").lower()
shift = int(input("Type the shift nummber:\n"))
direction = input("Type 'encode' to encrypt or 'decode' to decrypt or 'exit' to escape \n")
caesar(original_text= text, shift_ammount = shift, encode_or_decode = direction)





