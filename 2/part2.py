import re
FILENAME = "input.txt"


def power(game) -> int:
    cube_count_map = {}
    for hand in game:
        for count, colour in zip(hand[::2], hand[1::2]):
            if colour not in cube_count_map.keys():
                cube_count_map[colour] = int(count)
            else:
                if cube_count_map[colour] < int(count):
                    cube_count_map[colour] = int(count) #update with new minimum possible count
    pow = 1
    for colour in cube_count_map:
        pow *= cube_count_map[colour]
    return pow

def main():
    sum = 0

    with open(FILENAME, "r") as file:
        for line in file.readlines():
            game_id = int(re.findall('[0123456789]*:', line)[0][0:-1])
            game = [ list(filter(None, re.split(',| |;|:', x))) for x in line[line.find(':'):].strip().split(';') if x != "" ] 
            # print(game_id)
            # print(game)
            sum += power(game)
    print(sum)
            
    

if __name__ == "__main__":
    main()