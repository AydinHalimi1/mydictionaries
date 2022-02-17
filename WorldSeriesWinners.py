infile = open('WorldSeriesWinners.txt','r')
infile1 = open('WorldSeriesWinners.txt','r')

output = int(input("Enter a year from 1903 to 2009: "))

if output == 1904:
    print('No World Series Winner')
elif output == 1994:
    print('No World Series Winner')
else:

    ws_winner = {}

    for line in infile:
        line = line.rstrip("\n")
        if line in ws_winner:
            ws_winner[line] = ws_winner[line] + 1
        else:
            ws_winner[line] = 1
    ws_winner[line]

    print(ws_winner)

    year = {}

    counter = 1902
    for line in infile1:
        line = line.rstrip("\n")
        if counter == 1903:
         counter += 2
         year[counter] = line
        elif counter == 1993:
            counter += 2
            year[counter] = line
        else:
            counter += 1
            year[counter] = line
    year[counter] = line

    counter = output
    outcome = year[counter]
    wins = ws_winner[outcome]

    print("Team:",outcome)
    print("Number of WS wins:",wins)