def encrypt(message, morse_dict):
    morse_code = []
    for char in message:
        if char == " ":
            morse_code.append("   ")
        elif char in morse_dict:
            morse_code.append(morse_dict[char])
    return " ".join(morse_code)

def decrypt(message, morse_dict):
    REVERSE_DICT = {value: key for key, value in morse_dict.items()}
    words = message.split("   ")
    decoded_message = []

    for word in words:
        letters = word.split(" ")
        decoded_word = ""
        for letter in letters:
            if letter in REVERSE_DICT:
                decoded_word += REVERSE_DICT[letter]
        decoded_message.append(decoded_word)

    return " ".join(decoded_message)