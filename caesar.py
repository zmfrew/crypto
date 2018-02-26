def alphabet_position(letter):
    return ord(letter.lower()) - 97

def rotate_character(char, rot):
    char_index = alphabet_position(char)
    if char.isalpha():
        new_char = chr((char_index + rot) % 26 + 97)
        if char.isupper():
            new_char = new_char.upper()
    else:
        return char
    return new_char

def encrypt(text, rot):
    text_list = list(text)
    new_text_list = []
    for char in text_list:
        new_text_list.append(rotate_character(char, rot))
    new_text = "".join(new_text_list)
    return new_text

def main():
    user_text = input("Type a message:")
    user_rot = int(input("Rotate by:"))
    print(encrypt(user_text, user_rot))

if __name__ == "__main__":
    main()