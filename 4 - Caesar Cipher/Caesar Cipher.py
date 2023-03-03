from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    if cipher_direction != "encode" and cipher_direction != "decode":
        print("Invalid option")
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if position + shift_amount < 26:
                new_position = position + shift_amount
            elif position + shift_amount >= 26:
                new_position = (position + shift_amount) % 26
            elif position + shift_amount < 0 and position + shift_amount >= -26:
                new_position = position + shift_amount + 26
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")

# aplica conditii doar pe shift_amount (nu chiar merge :)) )

# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     if cipher_direction != "encode" and cipher_direction != "decode":
#         print("Invalid option")
#     for letter in start_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             if shift_amount >= 26 or shift_amount < -27:
#                 shift_amount %=26
#             elif shift_amount < 0:
#                 shift_amount +=26
#             new_position = position + shift_amount
#             end_text = alphabet[new_position]
#         else:
#             end_text += letter
#     print(f"The {cipher_direction}d text is {end_text}")


print(logo)
go_again = "yes"

while go_again == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
