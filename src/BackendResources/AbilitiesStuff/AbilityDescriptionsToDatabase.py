#   OVERALL PLAN FOR THIS SCRIPT:
#       READ IN THE FILE AND PARSE IT OUT AS A LIST OF ABILITIES
#       4 EACH ABILITY:
#           FIND EACH PIECE OF INFORMATION THAT COULD BE IN THE STRING & LIST WHICH ONES ARE THERE
#           USE THAT LIST OF WHICH INFO IS THERE TO ADD THE (types) PIECE TO THE OUTPUT STRING
#           THEN COLLATE ALL FOUND INFO INTO THE 2ND () OF THE STRING 
#           WRITE THE STRING TO THE OUTPUT FILE
#   USE THE ERROR OUTPUT FILE FOR ANY ABILITY WITH ERRORS IN IT ALONG W/ STRING ABOUT WHAT'S WRONG - FASTER FOR ME TO EDIT THAN TO MAKE THS SCRIPT FIX THE ERRORS THAT IT CATCHES

#   READ IN THE FILE AND SETUP OUTPUT FOR LATER
input = open("testingInput.txt", "r+")
output = open("testingOutput.txt", "w")
errorOutput = open("testingErrorOutput.txt", "w")

abilities = []
for x in range(300):
    nextLine = input.read()
    if nextLine == "": 
        break
    abilities.append(nextLine.split('\n\n') )
abilities = abilities[0]


for x in abilities:
    if len(x) == 0:
        abilities.remove(x)

#   VARIABLES AND FUNCTIONS TO BE USED IN THE LOOP AS NECESSARY
costsEnum = "ENUM ('low', 'moderate', 'high', 'very high', 'extreme', 'beyond extreme', 'low per second', 'moderate per second', 'high per second', 'extreme per second', 'beyond extreme per second')"
cooldownsEnum = "ENUM ('none', '5 seconds', '10 seconds', '30 seconds', '1 minute', '10 minutes', '1 hour', '6 hours', '12 hours', '1 day', '1 rank')"
typesEnum = "ENUM ('special ability', 'drain', 'familiar', 'ritual', 'special attack', 'conjuration', 'spell', 'summoning', 'aura', 'execute', 'counter-execute', 'perception', 'channeling', 'dimension', 'teleport', 'looting', 'combination', 'movement', 'instantaneous movement', 'puppet')"
essencesEnum = "ENUM ('adept', 'ape', 'armor', 'axe', 'balance', 'bat', 'bear', 'bee', 'bird', 'blight', 'blood', 'bone', 'bow', 'cage', 'cat', 'cattle', 'chain', 'claw', 'cloth', 'cloud', 'cold', 'coral', 'corrupt', 'crocodile', 'crystal', 'dance', 'dark', 'death', 'deep', 'deer', 'dimension', 'discord', 'dog', 'duck', 'dust', 'earth', 'echo', 'elemental', 'eye', 'feast', 'feeble', 'fire', 'fish', 'flea', 'flesh', 'foot', 'fork', 'fox', 'frog', 'fungus', 'gathering', 'glass', 'goat', 'grazen', 'growth', 'gun', 'hair', 'hammer', 'hand', 'harmonic', 'heidel', 'hook', 'horse', 'hunger', 'hunt', 'ice', 'iron', 'knife', 'knowledge', 'life', 'light', 'lightning', 'lizard', 'locust', 'lurker', 'magic', 'malign', 'manatee', 'might', 'mirage','mirror', 'monkey', 'moon', 'mouse', 'myriad', 'needle', 'net', 'octopus', 'omen', 'owl', 'pangolin', 'paper', 'plant', 'potent', 'rabbit', 'rake', 'rat', 'renewal', 'resolute', 'rune', 'sand', 'sceptre', 'serene', 'shark', 'shield', 'shimmer', 'ship', 'shovel', 'sickle', 'sin', 'skunk', 'sloth', 'smoke', 'snake', 'song', 'spear', 'spider', 'spike', 'staff', 'star', 'sun', 'swift', 'sword', 'technology', 'tentacle', 'thread', 'trap', 'tree', 'trowel', 'turtle', 'vast', 'vehicle', 'venom', 'visage', 'void', 'wall', 'wasp', 'water', 'whale', 'wheel', 'whip', 'wind', 'wing', 'wolf', 'wood', 'zeal', 'action', 'alchemy', 'ambush', 'animate', 'anzu', 'arsenal', 'avatar', 'battlfield', 'beguiling', 'behemoth', 'boundary', 'bounty', 'cataclysm', 'chaotic', 'charlatan', 'chimera', 'cyborg', 'cycle', 'cyclops', 'dawn', 'desolate', 'discordant', 'doom', 'doppleganger', 'dragon', 'eclipse', 'edifice', 'effigy', 'empower', 'fertility', 'fey', 'firebird', 'force', 'forge', 'fortress', 'garuda', 'gate', 'glimeron', 'gorgon', 'griffon', 'guardian', 'harpy', 'harvest', 'hydra', 'immortal', 'jackalope', 'juggernaut', 'karmic', 'kraken', 'leviathan', 'lotus', 'magitech', 'manticore', 'master', 'ministration', 'minotaur', 'mystic', 'nebula', 'nemesis', 'oasis', 'ocean', 'onslaught', 'phantasmagoria', 'pheonix', 'predatory', 'prison', 'prosperity', 'refracting', 'resonating', 'roc', 'sacrafice', 'scribe', 'serpent', 'simulacrum', 'skirmish', 'sky', 'soaring', 'sovereign', 'stellar', 'storm', 'succubus', 'swarm', 'talisman', 'thunderbird', 'time', 'tranquil', 'transfiguration', 'transgression', 'troll', 'twilight', 'undeath', 'unity', 'verdant', 'vessel', 'vision', 'volcano', 'vortex', 'weave', 'wendigo', 'wrath', 'ziz')"
costsList = ['low', 'moderate', 'high', 'very high', 'extreme', 'beyond extreme', 'low per second', 'moderate per second', 'high per second', 'extreme per second', 'beyond extreme per second', 'none']
cooldownsList = ['none', '5 seconds', '10 seconds', '30 seconds', '1 minute', '10 minutes', '1 hour', '6 hours', '12 hours', '1 day', '1 rank']
typesList = ['special ability', 'drain', 'familiar', 'ritual', 'special attack', 'conjuration', 'spell', 'summoning', 'aura', 'execute', 'counter-execute', 'perception', 'channeling', 'dimension', 'teleport', 'looting', 'combination', 'movement', 'instantaneous movement', 'puppet']
essencesList = ['adept', 'ape', 'armor', 'axe', 'balance', 'bat', 'bear', 'bee', 'bird', 'blight', 'blood', 'bone', 'bow', 'cage', 'cat', 'cattle', 'chain', 'claw', 'cloth', 'cloud', 'cold', 'coral', 'corrupt', 'crocodile', 'crystal', 'dance', 'dark', 'death', 'deep', 'deer', 'dimension', 'discord', 'dog', 'duck', 'dust', 'earth', 'echo', 'elemental', 'eye', 'feast', 'feeble', 'fire', 'fish', 'flea', 'flesh', 'foot', 'fork', 'fox', 'frog', 'fungus', 'gathering', 'glass', 'goat', 'grazen', 'growth', 'gun', 'hair', 'hammer', 'hand', 'harmonic', 'heidel', 'hook', 'horse', 'hunger', 'hunt', 'ice', 'iron', 'knife', 'knowledge', 'life', 'light', 'lightning', 'lizard', 'locust', 'lurker', 'magic', 'malign', 'manatee', 'might', 'mirage', 'mirror', 'monkey', 'moon', 'mouse', 'myriad', 'needle', 'net', 'octopus', 'omen', 'owl', 'pangolin', 'paper', 'plant', 'potent', 'pure', 'rabbit', 'rake', 'rat', 'renewal', 'resolute', 'rune', 'sand', 'scepter', 'serene', 'shark', 'shield', 'shimmer', 'ship', 'shovel', 'sickle', 'sin', 'skunk', 'sloth', 'smoke', 'snake', 'song', 'spear', 'spider', 'spike', 'staff', 'star', 'sun', 'swift', 'sword', 'technology', 'tentacle', 'thread', 'trap', 'tree', 'trowel', 'turtle', 'vast', 'vehicle', 'venom', 'visage', 'void', 'wall', 'wasp', 'water', 'whale', 'wheel', 'whip', 'wind', 'wing', 'wolf', 'wood', 'zeal', 'action', 'alchemy', 'ambush', 'animate', 'anzu', 'arsenal', 'avatar', 'battlfield', 'beguiling', 'behemoth', 'boundary', 'bounty', 'cataclysm', 'chaotic', 'charlatan', 'chimera', 'cyborg', 'cycle', 'cyclops', 'dawn', 'desolate', 'discordant', 'doom', 'doppleganger', 'dragon', 'eclipse', 'edifice', 'effigy', 'empower', 'fertility', 'fey', 'firebird', 'force', 'forge', 'fortress', 'garuda', 'gate', 'glimeron', 'gorgon', 'griffon', 'guardian', 'harpy', 'harvest', 'hydra', 'immortal', 'jackalope', 'juggernaut', 'karmic', 'kraken', 'leviathan', 'lotus', 'magitech', 'manticore', 'master', 'medusa', 'ministration', 'minotaur', 'mystic', 'nebula', 'nemesis', 'oasis', 'ocean', 'onslaught', 'phantasmagoria', 'pheonix', 'predatory', 'prison', 'prosperity', 'refracting', 'resonating', 'roc', 'sacrafice', 'scribe', 'serpent', 'simulacrum', 'skirmish', 'sky', 'soaring', 'sovereign', 'stellar', 'storm', 'succubus', 'swarm', 'talisman', 'thunderbird', 'time', 'tranquil', 'transfiguration', 'transgression', 'troll', 'twilight', 'undeath', 'unity', 'verdant', 'vessel', 'vision', 'volcano', 'vortex', 'weave', 'wendigo', 'wrath', 'ziz']
affinitiesList = ['none', 'rigid', 'incorporeal', 'life', 'death', 'holy', 'unholy', 'astral', 'swarm', 'corruption', 'magic', 'fire', 'water', 'earth', 'wind', 'iron', 'lightning', 'plant', 'cold', 'light', 'dark']

def outputAbilityDetailsToErrorFile(errorMessage, abilityTextBlock):
    errorOutput.write(errorMessage + " in this ability:\n")
    for x in abilityTextBlock:
        errorOutput.write(x + '\n')
    errorOutput.write('\n')

def findWhichFromSetInString(listOfValues, stringWithValueInIt):
    for x in listOfValues:
        if stringWithValueInIt.find(x) != -1:
            return x
    return 'Could not find any value from the list in the string'

for ability in abilities:
    errorFound = False
    command = 'INSERT INTO abilities ('
    commandSecondHalf = ') VALUES ('
    allLines = ability.split('\n')

    
    detailedInformation = allLines[0].split(' - ')
    if len(detailedInformation) == 0:
        continue
    
    if len(detailedInformation) != 8:
        outputAbilityDetailsToErrorFile("Incorrect number of inputs or one of the '-' dividers doesn't have a space on both sides of it", allLines)
        continue

#       ALL OF THESE VARIABLES AND CODE CHUNKS ARE TO READ IN THE detailedInformation BITS, CHECK THEM FOR ERRORS AND PREPARE THEM TO ADD TO THE command TO OUTPUT
#           I AM COLLECTING ALL THE INFO THEN ADDING THEM TO THE COMMAND AT THE END BC/ WE NEED TO KNOW WHICH THINGS ARE THERE TO ADD THEM ALL TO THE CMD AT ONCE, IS THERE A BETTER WAY?
    name, costs, cooldown, actionCost = detailedInformation[0], detailedInformation[1], detailedInformation[2], detailedInformation[3]
    firstType, otherTypes, affinities, essences = detailedInformation[4], detailedInformation[5], detailedInformation[6], detailedInformation[7]

#       HANDLE THE NAME OF THE ABILITY
    name = name.strip()
    if len(name) > 60:
        outputAbilityDetailsToErrorFile('The name of this ability is too long, it must be under 60 characters', allLines)
        continue

    command += '\'name\''
    commandSecondHalf += '\'' + name + '\''


#       HANDLE THE COSTS OF THE ABILITY
    staminaCost, manaCost, healthCost = '', '', ''
    costStrings = costs.split(',')
    if len(costStrings) == 1 and costStrings[0] == 'none':
        staminaCost, manaCost, healthCost = 'none', 'none', 'none'
        commandSecondHalf += ', \'none\', \'none\', \'none\''
    else:
        for x in range(len(costStrings) ):
            costStrings[x] = costStrings[x].strip()
            staminaIndex, manaIndex, healthIndex = costStrings[x].find('stamina'), costStrings[x].find('mana'), costStrings[x].find('health')
            costIsPerSecond = costStrings[x].find('per second')
            if staminaIndex != -1:
                staminaCost = costStrings[x][:costStrings[x].find('stamina') ]
                if costIsPerSecond != -1:
                    staminaCost = staminaCost + 'per second'
            if manaIndex != -1:
                manaCost = costStrings[x][:costStrings[x].find('mana') ]
                if costIsPerSecond != -1:
                    manaCost = manaCost + 'per second'
            if healthIndex != -1:
                healthCost = costStrings[x][:costStrings[x].find('health') ]
                if costIsPerSecond != -1:
                    healthCost = healthCost + 'per second'
        
    costStrings = [staminaCost, manaCost, healthCost]
    costListedFoundTypoOrNoCostListed = True
    for x in costStrings:
        if findWhichFromSetInString(costsList, x) != 'Could not find any value from the list in the string':
            costListedFoundTypoOrNoCostListed = False
            break
    if costListedFoundTypoOrNoCostListed == True:
        outputAbilityDetailsToErrorFile('There was either no cost listed or there was a typo in the cost listed for', allLines)
        continue
    
    command += ', \'stamina\', \'mana\', \'health\''
    if staminaCost == '':
        commandSecondHalf += ', \'none\''
    else:
        commandSecondHalf += ', \'' + staminaCost + '\''
    if manaCost == '':
        commandSecondHalf += ', \'none\''
    else:
        commandSecondHalf += ', \'' + manaCost + '\''
    if healthCost == '':
        commandSecondHalf += ', \'none\''
    else:
        commandSecondHalf += ', \'' + healthCost + '\''


#       HANDLE THE COOLDOWN OF THE ABILITY
    cooldown = cooldown.strip().lower()
    if  findWhichFromSetInString(cooldownsList, cooldown) == 'Could not find any value from the list in the string':
        outputAbilityDetailsToErrorFile('The cooldowns were listed incorrectly, probably just a typo', allLines)
        continue

    command += ', \'cooldown\''
    commandSecondHalf += ', \'' + cooldown + '\''
    

#       HANDLE THE ACTION COST OF THE ABILITY
    actionCost = actionCost.strip().split(' ')[0]
    if actionCost == 'none':
        actionCost = '0'
    if actionCost != 'reaction':
        if int(actionCost) > 255:
            outputAbilityDetailsToErrorFile('The number of actions is way too high, it must be in the range of 1-255 or be listed as: none, or reaction', allLines)
            continue

    command += ', \'actionCost\''
    commandSecondHalf += ', \'' + actionCost + '\''


#       HANDLE THE FIRST TYPE OF THE ABILITY
    firstType = firstType.strip().lower()
    if findWhichFromSetInString(typesList, firstType) == 'Could not find any value from the list in the string':
        outputAbilityDetailsToErrorFile('The listed primary type is mispelled', allLines)
        continue

    if firstType != 'none':
        command += ', \'firstType\''
        commandSecondHalf += ', \'' + firstType + '\''


#       HANDLE THE LESS-PROMINENT TYPES OF THE ABILITY
    secondType, thirdType, fourthType = '', '', ''
    otherTypes = otherTypes.split(',')
    for x in range(len(otherTypes) ):
        otherTypes[x] = otherTypes[x].strip().lower()
        if otherTypes[x] == '':
            otherTypes.pop(x)
    if len(otherTypes) >= 4 and ( (otherTypes.count('ritual') == 1 or firstType == 'ritual') and otherTypes.count('spell') == 1):
        otherTypes.remove('spell')
    if len(otherTypes) > 3:
        outputAbilityDetailsToErrorFile('There are a maximum of 4 allowable types for any ability there are too many', allLines)
        continue
    if len(otherTypes) > 0:
        secondType = otherTypes[0]
        if len(otherTypes) > 1:
            thirdType = otherTypes[1]
            if len(otherTypes) == 3:
                fourthType = otherTypes[2]
    
    if secondType != 'none':
        command += ', \'secondType\''
        commandSecondHalf += ', \'' + secondType + '\''
        if thirdType != '':
            command += ', \'thirdType\''
            commandSecondHalf += ', \'' + thirdType + '\''
            if fourthType != '':
                command += ', \'fourthType\''
                commandSecondHalf += ', \'' + fourthType + '\''
    

#       HANDLE THE AFFINITY(-IES) OF THE ABILITY
    firstAffinity, secondAffinity, thirdAffinity = '', '', ''
    if len(affinities) != 0:
        affinities = affinities.split(',')
        if len(affinities) > 3:
            outputAbilityDetailsToErrorFile('More than the maximum of three affinities were listed', allLines)
            continue
        for x in range(len(affinities) ):
            affinities[x] = affinities[x].strip().lower()
            if findWhichFromSetInString(affinitiesList, affinities[x] ) == 'Could not find any value from the list in the string':
                outputAbilityDetailsToErrorFile('One of the affinities listed is mispelled', allLines)
                errorFound = True
                continue
        if errorFound == True:
            continue
        firstAffinity = affinities[0]
        if len( affinities) > 1:
            secondAffinity = affinities[1]
            if len(affinities) == 3: 
                thirdAffinity == affinities[2]


#       HANDLE THE ESSENCES THAT CAN GIVE THIS ESSENCE
    firstEssence, secondEssence, thirdEssence, fourthEssence, fifthEssence = '', '', '', '', ''
    sixthEssence, seventhEssence, eighthEssence, ninthEssence, tenthEssence = '', '', '', '', ''
    sourceEssences = essences.split(',')
    for x in range(len(sourceEssences) ):
        sourceEssences[x] = sourceEssences[x].strip().lower()
        if findWhichFromSetInString(essencesList, sourceEssences[x] ) == 'Could not find any value from the list in the string':
            outputAbilityDetailsToErrorFile('One of the essences listed was mispelled or a comma is missing / put somewhere dumb', allLines)
            errorFound = True
            break
        if x == 0:
            firstEssence = sourceEssences[x]
            command += ', \'firstEssence\''
            commandSecondHalf += ', \'' + firstEssence + '\''
        elif x == 1:
            secondEssence = sourceEssences[x]
            command += ', \'secondEssence\''
            commandSecondHalf += ', \'' + secondEssence + '\''
        elif x == 2:
            thirdEssence = sourceEssences[x]
            command += ', \'thirdEssence\''
            commandSecondHalf += ', \'' + thirdEssence + '\''
        elif x == 3:
            fourthEssence = sourceEssences[x]
            command += ', \'fourthEssence\''
            commandSecondHalf += ', \'' + fourthEssence + '\''
        elif x == 4:
            fifthEssence = sourceEssences[x]
            command += ', \'fifthEssence\''
            commandSecondHalf += ', \'' + fifthEssence + '\''
        elif x == 5:
            sixthEssence = sourceEssences[x]
            command += ', \'sixthEssence\''
            commandSecondHalf += ', \'' + sixthEssence + '\''
        elif x == 6: 
            seventhEssence = sourceEssences[x]
            command += ', \'seventhEssence\''
            commandSecondHalf += ', \'' + seventhEssence + '\''
        elif x == 7:
            eighthEssence = sourceEssences[x]
            command += ', \'eighthEssence\''
            commandSecondHalf += ', \'' + eighthEssence + '\''
        elif x == 8:
            ninthEssence = sourceEssences[x]
            command += ', \'ninthEssence\''
            commandSecondHalf += ', \'' + ninthEssence + '\''
        elif x == 9:
            tenthEssence = sourceEssences[x]
            command += ', \'tenthEssence\''
            commandSecondHalf += ', \'' + tenthEssence + '\''
    if errorFound == True:
        continue
    
    

#       HANDLE THE DESCRIPTIONS OF THE ABILITY'S FUNCTIONING
    descriptions = []
    descriptionIronRank = allLines[1][len('Iron Rank: '): ].strip()
    if len(descriptionIronRank) > 250: 
        outputAbilityDetailsToErrorFile('The maximum length is 250 characters, the iron rank description was too long', allLines)
        continue
    descriptions.append(descriptionIronRank)
    command += ', \'descriptionIronRank\''
    descriptionBronzeRank, descriptionSilverRank, descriptionGoldRank, descriptionDiamondRank = '', '', '', ''
    if len(allLines) < 2 or len(allLines) > 6:
        outputAbilityDetailsToErrorFile('Too many or not enough lines were fed in, there really should only be one per ability rank after the first line in', allLines)
        continue
    if len(allLines) >= 3 and len(allLines[2][len('Bronze Rank: '): ].strip() ) > 0:
        descriptionBronzeRank = allLines[2][len('Bronze Rank: '): ].strip()
        descriptions.append(descriptionBronzeRank)
        command += ', \'descriptionBronzeRank\''
        if len(descriptionBronzeRank) > 250: 
            outputAbilityDetailsToErrorFile('The maximum length is 250 characters, the bronze rank description was too long', allLines)
            continue
        if len(allLines) >= 4 and len(allLines[3][len('Silver Rank: '): ].strip() ):
            descriptionSilverRank = allLines[3][len('Silver Rank: '): ].strip()
            descriptions.append(descriptionSilverRank)
            command += ', \'descriptionSilverRank\''
            if len(descriptionSilverRank) > 250: 
                outputAbilityDetailsToErrorFile('The maximum length is 250 characters, the silver rank description was too long', allLines)
                continue
            if len(allLines) >= 5 and len(allLines[4][len('Gold Rank: '): ].strip() ):
                descriptionGoldRank = allLines[4][len('Gold Rank: '): ].strip()
                descriptions.append(descriptionGoldRank)
                command += ', \'descriptionGoldRank\''
                if len(descriptionGoldRank) > 250: 
                    outputAbilityDetailsToErrorFile('The maximum length is 250 characters, the gold rank description was too long', allLines)
                    continue
                if len(allLines) == 6 and len(allLines[5][len('Diamond Rank: '): ].strip() ):
                    descriptionDiamondRank = allLines[5][len('Diamond Rank: '): ].strip()
                    descriptions.append(descriptionDiamondRank)
                    command += ', \'descriptionDiamondRank\''
                    if len(descriptionDiamondRank) > 250: 
                        outputAbilityDetailsToErrorFile('The maximum length is 250 characters, the diamond rank description was too long', allLines)
                        continue
    
    
#       OUTPUT THIS ABILITY NOW THAT THERE ARE NO EASY ERRORS TO CATCH AND ALL INFO HAS BEEN READ IN
    output.write(command + '\n')
    output.write(commandSecondHalf + '\n')
    for x in descriptions:
        output.write(', \'' + x + '\'\n')
    output.write(');\n')















