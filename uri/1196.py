
wertyu = {
    '1': '`', '2': '1', '3': '2',
    '4': '3', '5': '4', '6': '5',
    '7': '6', '8': '7', '9': '8',
    '0': '9', '-': '0', '=': '-',
    'W': 'Q', 'E': 'W', 'R': 'E',
    'T': 'R', 'Y': 'T', 'U': 'Y',
    'I': 'U', 'O': 'I', 'P': 'O',
    'S': 'A', 'D': 'S', 'F': 'D',
    'G': 'F', 'H': 'G', 'J': 'H',
    'K': 'J', 'L': 'K', 'X': 'Z',
    'C': 'X', 'V': 'C', 'B': 'V',
    'N': 'B', 'M': 'N', ',': 'M',
    '.': ',', '/': '.', ' ': ' ',
    '[': 'P', ']': '[', '\\': ']',
    ';': 'L', "'": ';', 'A': '',
    'Q': '', 'Z': ''
}

while True:
    try:
        texto = list(input())

        for i in range(len(texto)):
            texto[i] = wertyu[texto[i]]

        print(''.join(texto))
    except EOFError:
        break
