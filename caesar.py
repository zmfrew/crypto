from helpers import alphabet_position, rotate_character

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