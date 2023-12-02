
def getLineNumber(line: str) -> int:
    n1 = 0
    n2 = 0

    #find the first digit in line
    i = 0
    while ( i < len(line) ):
        if ( line[i].isdigit() ):
            n1 = int(line[i])
            break
        i+=1

    
    #find last digit in line
    i = len(line) - 1
    while ( i >= 0):
        if ( line[i].isdigit()):
            n2 = int(line[i])
            break
        i -= 1

    return n1 * 10 + n2



f = open("input.txt","r")

sum = 0

for line in f.readlines():
    if (line != ""):
        sum += getLineNumber(line)

print(sum)   