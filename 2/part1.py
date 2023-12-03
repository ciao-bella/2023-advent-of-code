import re
FILENAME = "input.txt"

cube_count_map = {'red': 12, 'green':13, 'blue': 14}

def is_hand_possible(hand: str) -> bool:

    for count, colour in zip(hand[::2], hand[1::2]):
        if(cube_count_map[colour] < int(count)):
            return False
    return True

def is_game_possible(game: str) -> bool:
    for hand in game:
        if not is_hand_possible(hand):
            return False
    return True

def main():
    sum = 0

    with open(FILENAME, "r") as file:
        for line in file.readlines():
            game_id = int(re.findall('[0123456789]*:', line)[0][0:-1])
            game = [ list(filter(None, re.split(',| |;|:', x))) for x in line[line.find(':'):].strip().split(';') if x != "" ] 
            # print(game_id)
            # print(game)
            
            if is_game_possible(game):
                sum+=game_id
    print(sum)
            
    

if __name__ == "__main__":
    main()