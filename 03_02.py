mr_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
           'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
           'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
           'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
           '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}


def char_to_mr(input_string: str):
    mr_string = ''
    for ch in input_string:
        print(ch)
        if mr_dict.get(ch) is not None:
            mr_string += mr_dict.get(ch)
            mr_string += ' '
        else:
            mr_string += ch
    return mr_string


print(char_to_mr('HELLO PYTHON 3'))
