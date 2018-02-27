from helpers import alphabet_position, rotate_character

def encrypt(text, e_key):
    text_list = list(text)
    e_key_list = list(e_key)
    new_text_list = []
    idx = 0
    for index, char in enumerate(text_list):
        if idx == len(e_key):
            idx = 0
        char_index = alphabet_position(e_key_list[idx])
        new_text_list.append(rotate_character(char, char_index))
        if text_list[index] == " ":
            idx = idx
        else:
            idx += 1
    new_text = "".join(new_text_list)
    return new_text

def main():
    user_text = input("Type a message:")
    user_rot = input("Encryption key:")
    print(encrypt(user_text, user_rot))

if __name__ == "__main__":
    main()