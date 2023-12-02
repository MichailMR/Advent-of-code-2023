import numpy as np

inp = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

ints = [str(i) for i in list(range(10))]

maxred = 12
maxgreen = 13
maxblue = 14

res = 0
for i, line in enumerate(inp.split('\n')):
    rounds = line[7:].split(';')
    cool = 1
    for r in rounds:
        red, green, blue = 0, 0, 0
        for pull in r.split(','):
            num = int(''.join([char for char in pull if char in ints]))
            if 'red' in pull:
                red = num
            elif 'green' in pull:
                green = num
            elif 'blue' in pull:
                blue = num
        cool *= (red <= maxred and green <= maxgreen and blue <= maxblue)
    if cool:
        res += i+1
        print(i+1)

print(res)