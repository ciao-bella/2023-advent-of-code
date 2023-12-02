
#assumes that there is at least one occurrence of a number (either as a word or number) in line
def getLineNumber(line: str) -> int:

    #create a place to hold all the strings we may be looking for
    number_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    number_strings_value = {}
    for s, i in zip(number_strings, range(len(number_strings)) ):
        number_strings_value[s] = i + 1

    for i in range(1, 10):
        number_strings.append(str(i))

    min_index = len(line)
    max_index = -1

    first_num = ""
    last_num = ""

    for s in number_strings:
        min = line.find(s) #returns the smallest index of subword s in line
        max = line.rfind(s) #returns largest index of subword s in line

        if ( min != -1 and min < min_index ):
            min_index = min
            first_num = s
        
        if ( max > max_index):
            max_index = max
            last_num = s

    # print(first_num + " " + last_num)
    # print(line)
    # print("")

    #convert first num and last num to integer
    n1 = 0
    n2 = 0

    if ( first_num.isdigit()):
        n1 = int(first_num)
    else:
        n1 = number_strings_value[first_num]
    
    if ( last_num.isdigit()):
        n2 = int(last_num)
    else:
        n2 = number_strings_value[last_num]

    return n1 * 10 + n2
    


def main():
    f = open("input.txt","r")

    sum = 0

    for line in f.readlines():
        if (line != ""):
            # print(getLineNumber(line))
            sum += getLineNumber(line)

    print(sum)

if __name__ == "__main__":
    main()