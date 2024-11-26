#   OVERALL PLAN FOR THIS SCRIPT:
#       READ IN THE FILE AND PARSE IT OUT AS A LIST OF AWAKENING STONES
#       REATE LIST OF ALL 3 PIECES
#       4 EACH STONE:
#           VERIFY IT FALLS WITHIN RANGE AND ACCEPTABILITY FOR STRING
#           VERIFY ITS ONE OF THE ENUM OPTIONS FOR THE OTHER ONES
#           GIVE A USEFUL ERROR MESSAGE IF IT DOES NOT FIT
#           CONSTRUCT THE OUTPUT STRING WHICH IS A MYSQL COMMAND TO INPUT THIS DATA INTO THE DB AS THE STRING IS PARSED AND OUTPUT IT ALL TO THE FILE @ ONCE IF ALL CHECKS PASS+
#   USE THE ERROR OUTPUT FILE FOR ANY ABILITY WITH ERRORS IN IT ALONG W/ STRING ABOUT WHAT'S WRONG - FASTER FOR ME TO EDIT THAN TO MAKE THS SCRIPT FIX THE ERRORS THAT IT CATCHES
#   READ IN THE FILE AND SETUP OUTPUT FOR LATER
input = open("stonesToInputStringsCopy.txt", "r+")
output = open("DatabaseInfoEntryStrings.txt", "w")
errorOutput = open("errorOutput.txt", "w")

stones = []
for x in range(300):
    nextLine = input.read()
    if nextLine == "": 
        break
    stones.append(nextLine.split('\n') )
stones = stones[0]

for x in stones:
    if len(x) == 0:
        stones.remove(x)


def outputStoneDetailsToErrorFile(errorMessage, stoneTextBlock):
    errorOutput.write(errorMessage + " in this stone:\n")
    for x in stoneTextBlock:
        errorOutput.write(x + '\n')
    errorOutput.write('\n')


# SPLIT UP EACH LINE INTO A LIST OF ALL 4 PIECES
for x in range(len(stones) ):
    stones[x] = stones[x].split(' - ')


# 4 ALL AWAKENING STONES TO INPUT INTO DATABASE LOOP
for stoneIndex in range(len(stones) ):
    command = 'INSERT INTO awakeningStones ('
    commandSecondHalf = ') VALUES ('

    # CATCH ANY THAT DO NOT HAVE EXACTLY 4 PIECES
    if (len(stones[stoneIndex] ) ) != 4:
        outputStoneDetailsToErrorFile("There are not four sections seperated by ' - ', double check that there are exactly 3 of these in the correct places", stones[stoneIndex] )
        continue

    # CHECK THE NAME OF THE NEW STONE
    if len(stones[stoneIndex] ) > 60:
        outputStoneDetailsToErrorFile("The name is too long, it can be at most 60 characters including starting with, 'Awakening Stone of '", stones[stoneIndex] )
        continue

    command += "'name'"
    commandSecondHalf += "'" + stones[stoneIndex][0] + "'"


    # CHECK THE RARITY OF THE STONE
    stoneRarities = ['unknown', 'common', 'uncommon', 'rare', 'epic', 'legendary']
    if stoneRarities.count(stones[stoneIndex][1] ) == 0:
        outputStoneDetailsToErrorFile("The rarity listed does not match the template", stones[stoneIndex] )
        continue

    command += ", 'rarity'"
    commandSecondHalf += ", '" + stones[stoneIndex][1] + "'"


    # CHECK THE POPULARITY OF THE STONE
    stonePopularities = stoneRarities + ['restricted']
    if stonePopularities.count(stones[stoneIndex][2] ) == 0:
        outputStoneDetailsToErrorFile('The popularity listed is incorrect', stones[stoneIndex] )
        continue

    command += ", 'popularity'"
    commandSecondHalf += ", '" + stones[stoneIndex][2] + "\'"


    # CHECK THE AFFINITIES OF THE STONE
    affinities = ['special ability', 'drain', 'familiar', 'ritual', 'special attack', 'conjuration', 'spell', 'summoning', 'puppet', 'aura', 'execute', 'counter-execute', 'perception', 'channeling', 'dimension', 'teleport', 'looting', 'combination', 'movement', 'instantaneous movement']
    stoneAffinities = stones[stoneIndex][3].split(',')
    errorFound = False
    for y in range(len(stoneAffinities) ):
        stoneAffinities[y] = stoneAffinities[y].strip()
        if affinities.count(stoneAffinities[y] ) == 0:
            errorFound = True
            outputStoneDetailsToErrorFile('One of the listed affinites was mispelled or incorrectly typed', stones[stoneIndex] )
            break
    if errorFound == True:
        continue

    tempList = ['Here to account for 0-index', 'Here to account for starting at 2', 'legendary', 'epic', 'rare', 'uncommon', 'common']
    correctNumberOfAffinities = 0
    if stones[stoneIndex][1] == 'unknown':
        correctNumberOfAffinities = 4
    else:
        correctNumberOfAffinities = tempList.index(stones[stoneIndex][1] )

    if correctNumberOfAffinities != len(stoneAffinities):
        outputStoneDetailsToErrorFile('The number of affinities listed were not correct for the rarity', stones[stoneIndex] )
        continue

    command += ", 'firstAffinity', 'secondAffinity'"
    commandSecondHalf += ", '" + stoneAffinities[0] + "', '" + stoneAffinities[1] + "'"
    for affinityIndex in range(2, correctNumberOfAffinities):
        if affinityIndex == 2:
            command += ", 'thirdAffinity'"
        elif affinityIndex == 3:
            command += ", 'fourthAffinity'"
        elif affinityIndex == 4:
            command += ", 'fifthAffinity'"
        elif affinityIndex == 5:
            command += ", 'sixthAffinity'"
        commandSecondHalf += ", '" + stoneAffinities[affinityIndex] + "'"


    output.write(command + commandSecondHalf + ');\n')
    
    