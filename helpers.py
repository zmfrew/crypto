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