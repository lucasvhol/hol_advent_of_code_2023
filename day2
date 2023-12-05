
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Open the input file from the same directory as the script
games_input = open(os.path.join(script_dir, "input.txt"), "r")
games_input = games_input.read()

# Define the maximum number of cubes in the bag
max_cubes = {"red": 12, "green": 13, "blue": 14}

# Parse the games data
def parse_games_input(games_input):
    games = []
    for line in games_input.strip().split("\n"):
        game_id, rounds = line.split(":")
        game_id = int(game_id.split(" ")[1])  # Extract the game number
        rounds_data = rounds.split(";")
        rounds_list = []
        for round_data in rounds_data:
            cubes = {"red": 0, "green": 0, "blue": 0}
            for cube_info in round_data.strip().split(","):
                number, color = cube_info.strip().split(" ")
                cubes[color] = max(cubes[color], int(number))
            rounds_list.append(cubes)
        games.append((game_id, rounds_list))
    return games

# Check if a game is possible
def is_game_possible(game, max_cubes):
    for round_cubes in game[1]:
        for color in max_cubes:
            if round_cubes[color] > max_cubes[color]:
                return False
    return True

# Parse the games data
games = parse_games_input(games_input)

# Check each game and sum the IDs of possible games
possible_games_sum = sum(game[0] for game in games if is_game_possible(game, max_cubes))

print(f"Solution: {possible_games_sum}")
