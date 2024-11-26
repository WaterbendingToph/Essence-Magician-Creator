import random

input = open("EssenceAbilityDescriptionsToWrite.txt", "r+")
output = open("ListGeneratorOutput.md", "w")

contents = []
for x in range(300):
    nextLine = input.read()
    if nextLine == "": 
        break
    contents.append(nextLine.split('\n') )
contents = contents[0]

output.write('Descriptions are 250 characters total for each rank. (I will have to change the database table to match this later and need to add affinities to essence abilities too as a varchar). \n')
output.write('List out in this order: Name - costs - cooldown - action cost - type - secondary types - affinities - essences <- (commas between multiples for any one thing, 60 chars 4 essences) MUST LIST ALL 8 - none - when N/A \n')
output.write('Affinities are: (\'Rigid\', \'Incorporeal\', \'Life\', \'Death\', \'Holy\', \'Unholy\', \'Astral\', \'Swarm\', \'Corruption\', \'Magic\', \'Fire\', \'Water\', \'Earth\', \'Wind\', \'Iron\', \' Lightning\', \'Plant\', \'Cold\', \'Light\', \'Dark\'). \n')
output.write('Iron Rank description on the next line w/ each rank\'s description on another line formatted like:\nIron Rank:\nBronze Rank: etc.\n')
output.write('Costs are:(\'low\', \'moderate\', \'high\', \'very high\', \'extreme\') listed in the order: stamina mana health with commas between them and with per second behind each cost if applicable\n')
output.write('Cooldowns are(\'none\', \'5 seconds\', \'10 seconds\', \'30 seconds\', \'1 minute\', \'10 minutes\', \'1 hour\', \'6 hours\', \'12 hours\', \'1 day\', \'1 rank\') \n')
output.write('Types are(\'special ability\', \'drain\', \'familiar\', \'ritual\', \'special attack\', \'conjuration\', \'spell\', \'summoning\', \'puppet\', \'aura\', \'execute\', \'counter-execute\', \'perception\', \'channeling\', \'dimension\', \'teleport\', \'looting\', \'combination\', \'movement\', \'instantaneous movement\') \n')
output.write('Make sure to delete this line from the EssenceAbilityDescriptionsToWrite.txt textfile when done to keep progress! \n\n\n')
linesToWrite = contents
ranks = ['Iron', 'Bronze', 'Silver', 'Gold', 'Diamond']
output.write(random.choice(linesToWrite).strip() + ' up to the rank of ' + random.choices(ranks, weights=(10, 29.5, 40, 20, 0.5), k=1 )[0] + '\n\t\n')

# baseEssences = contents[0].split()
# confluenceEssences = contents[2].split()
# abilityTypes = contents[4:]
# for x in range(len(baseEssences) ):
#     baseEssences[x] = baseEssences[x].capitalize()
# for x in range(len(confluenceEssences) ):
#     confluenceEssences[x] = confluenceEssences[x].capitalize()
# for x in range(len(abilityTypes) ):
#     abilityTypes[x] = abilityTypes[x].capitalize()

# allEssences = []
# for x in baseEssences:
#     allEssences.append(x)
# for x in confluenceEssences:
#     allEssences.append(x)

# allCombos = []
# for essenceIndex in range(len(allEssences) ):
#     for abilityTypeIndex in range(len(abilityTypes) ):
#         output.write('Give an example ability in the ' + allEssences[essenceIndex] + ' essence that belongs to primarily the ' + abilityTypes[abilityTypeIndex] + ' type              \n')
