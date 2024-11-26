import random

input = open("AwakeningStoneInfoToWrite.txt", "r+")
output = open("AwakeningStoneGeneratorOutput.md", "w")

contents = []
for x in range(300):
    nextLine = input.read()
    if nextLine == "": 
        break
    contents.append(nextLine.split('\n') )
contents = contents[0]

output.write('Remember, there are 6 affinities at common and one fewer with every step up in rarity until just one with the legendary awakening stones\n')
output.write('Also, the name is a 40 character varchar and a plural if that of a living thing or one object\n')
output.write("Rarities and popularities are('common', 'uncommon', 'rare', 'epic', 'legendary') and if this is one of the equivalent stones for an essence than it uses that rarity and popularity\n")
output.write('Affinities are(\'special ability\', \'drain\', \'familiar\', \'ritual\', \'special attack\', \'conjuration\', \'spell\', \'summoning\', \'puppet\', \'aura\', \'execute\', \'counter-execute\', \'perception\', \'channeling\', \'dimension\', \'teleport\', \'looting\', \'combination\', \'movement\', \'instantaneous movement\') \n')
output.write('It is also worth noting that anything with a casting time over 1 action is a spell of some kind because it has an incantation. So choosing spell also increases the pool to include ritual, familiar summoning, conjuration, summoning, puppet, channeling, teleport, looting, and drain types\n')
output.write("Those other types don't necessarily have to be spells though if they only have 1 action or shorter casting times\n")
output.write('Listing movement as an affinity does also include instaneous movement as less than half the time that type as well\n')
output.write("Combination abilites have to be stacking on either special attacks, movement, or special abilities. They're 50/40/10 - respectively so combination will also be 1 of those 3\n")
output.write('Ritual abilities are usually familiar summonings, but can also be ritual-related abilities in the form of other ability types, and least likely to be dedicated ritual abilities\n')
output.write('Also, the affinites are assumed to be evenly weighted between all of them, so no need to order them from highest to rarest affinity\n\n')
output.write('Make sure to delete this line from the AwakeningStoneInfoToWrite.txt textfile when done to keep progress! \n\n\n')
linesToWrite = contents
output.write('In the order of "name - rarity - popularity - affinities"\n')
output.write(random.choice(linesToWrite).strip() )
output.write('\nAwakening Stone of \n')

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
