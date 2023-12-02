import numpy as np

inp = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

ints = [str(i) for i in list(range(10))]

res = 0
for i, line in enumerate(inp.split('\n')):
    rounds = line[7:].split(';')
    red, green, blue = 0, 0, 0
    for r in rounds:
        for pull in r.split(','):
            num = int(''.join([char for char in pull if char in ints]))
            if 'red' in pull and num > red:
                red = num
            elif 'green' in pull and num > green:
                green = num
            elif 'blue' in pull and num > blue:
                blue = num
    res += red*green*blue

print(res)