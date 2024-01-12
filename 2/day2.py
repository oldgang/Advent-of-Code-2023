# Check if the game is possible
def game_possible(game):
    # maximum: 12 red cubes, 13 green cubes, 14 blue cubes
    cubeLimit = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    game = game.split(':')[1].strip()
    rounds = game.split(';')
    rounds = [round.strip() for round in rounds]
    for round in rounds:
        colors = round.split(',')
        colors = [color.strip() for color in colors]
        for color in colors:
            cubeCount, color = color.split(' ')
            if int(cubeCount) > cubeLimit[color]:
                return False
    return True

# # Read the example file
# with open('2/example.txt', 'r') as f:
#     lines = f.readlines()
#     lines = [line.strip() for line in lines]

# Read the input file
with open('2/input.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

# Part 1 - Sum the game IDs of the possible games
sum = 0
for line in lines:
    if game_possible(line):
        gameID = line.split(':')[0].split(' ')[1]
        sum += int(gameID)
print('Part 1:', sum)