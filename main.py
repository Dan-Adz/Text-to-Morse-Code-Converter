# Text to Morse Code Converter

code_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '...-', '5': '...', '6': '-...', '7': '--...', '8': '---..',
    '9': '----.',
}
str_morse = ""
str_input = (input('Convert this into Morse Code: ')).lower()
cant_translate = []

# Converts all convertable characters ands adds them to the morse code string
# Characters that could not be converted are added to a separate list
# If the character is a space a divider is added to the morse code string to show where words end/begin
for let in str_input:
    if let in code_dict.keys():
        str_morse += code_dict[let]
        str_morse += ' '
    elif let == ' ':
        str_morse += '/ '
    else:
        cant_translate.append(let)

print(f'The String in Morse Code is: {str_morse}')
if len(cant_translate) > 0:
    print(f'The following characters could not be translated: {set(cant_translate)}')
