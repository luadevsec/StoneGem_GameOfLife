from ascii_art import tela

from ascii_art import full, empty
text = ''.join([full, full, empty, full,full, full, empty, empty, full, full, empty])

print(text)
x = 0
for i in range(1, len(text), 2):
    if text[i] == '█':
        print( x, "= alive")
    else:
        print( x, "= dead")
    x = x + 1