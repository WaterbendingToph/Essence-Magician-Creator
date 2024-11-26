import MasterLooter

'''
        SET THIS UP WITH THE THINGS NOTED FROM COMPLETING SpecificGeneratorTest.py 
            CONSULT THE NOTES IN THIS ONE FOR SPECIFIC CHANGES AND THINGS 2 KEEP IN MIND
'''

# ITEM WEIGHTS OF 0,0,0, ... ,0 ARE JUST FOR TESTING PURPOSES IN TESTS THAT WILL NOT TEST FOR THAT SECTION WORKING CORRECTLY
def runTest(testNumber, targetRank, testType, targetMagicLevel=10, typeWeights='', lootables='', isMonster=False, looterRank=0, lootMultiplier=1, message=''):
    try:
        if testType == 'lootTargetSpecificKey' or testType == 'lootTargetFull':
            rawOutput = MasterLooter.lootTarget(targetRank, targetMagicLevel, typeWeights, lootables, isMonster, looterRank, lootMultiplier)
        if testType == 'equipment':
            rawOutput = MasterLooter.generateEquipmentPiece(targetRank)
        if testType == 'potion':
            rawOutput = MasterLooter.generatePotion(targetRank)
        if testType == 'healingItem':
            rawOutput = MasterLooter.generateHealingItem(targetRank)
        if testType == 'craftingMat':
            rawOutput = MasterLooter.generateCraftingMats(targetRank)
        if testType == 'condensedMagic':
            rawOutput = MasterLooter.generateCondensedMagic(targetRank)

        tempArray = rawOutput.split(',')
        results = tempArray[0]
        for thingLooted in tempArray[1:]:
            results += '\n' + thingLooted
    
        if testType == 'lootTargetSpecificKey':
            assert(keys[testNumber] == results)
            return str(testNumber) + ' passed ' + message + '\n'
    
        else:
            # TEST HERE EVERYTHING IS CATEGORICALLY WHAT WE EXPECT
            return ''
    
    except AssertionError:
        return str(testNumber) + ' failed with the wrong output of:\n' + results + ' ' + message + '\n\n'
    except:
        return str(testNumber) + ' failed due to unknown error, run individually for more information ' + message + '\n' 



testKey = open('MasterLooterTestKey.txt', 'r')
keys = []
for x in range(300):
    nextLine = testKey.read()
    if nextLine == "": 
        break
    keys.append(nextLine.split('\n\n') )
keys = keys[0]

allPossibleLootables = ['claw', 'eye', 'fang', 'scale', 'carapace', 'pincers', 'skull', 'spines', 'head', 'tail', 'horn', 'shell', 'hide', 'beak', 'teeth', 'hide', 'blood', 'venom', 'scales', 'heart', 'elemental organ', 'horn', 'bone', 'jelly', 'antennae', 'fin', 'vine', 'ectoplasm', 'stomach acid', 'stinger', 'horn', 'feather', 'mucous', 'hooves', 'claws']
output = open('MasterLooterTestOutput.txt', 'w')

#   TEST LOOTING GOODIES (CORES AND COINS)
output.write( runTest(0, 'lesser', 'lootTargetSpecificKey', message='looting target goodies in lesser rank') )
output.write( runTest(1, 'lesser', 'lootTargetSpecificKey', message='looting target goodies in lesser rank with a higher loot multiplier', lootMultiplier=3) )
output.write( runTest(2, 'iron', 'lootTargetSpecificKey', message='looting target goodies in iron rank') )
output.write( runTest(3, 'bronze', 'lootTargetSpecificKey', message='looting target goodies in bronze rank') )
output.write( runTest(4, 'silver', 'lootTargetSpecificKey', message='looting target goodies in silver rank') )
output.write( runTest(5, 'gold', 'lootTargetSpecificKey', message='looting target goodies in gold rank') )
output.write( runTest(6, 'diamond', 'lootTargetSpecificKey', message='looting target goodies in diamond rank') )

#   TEST LOOTING CRAFTING MATS
output.write( runTest(7, 'bronze', 'craftingMat', message='looting crafting mats with no weights') )

output.write( runTest(8, 'bronze', 'craftingMat', message='looting crafting mats with weights') )






# CHANGE THIS WHOLE TEST FILE TO USE TRY EXCEPT BLOCKS AND ASSERTS TO RUN ALL TESTS WRITTEN IN DEVELOPMENT IN A SUITE AND REPORT ON ALL OF THEM AT ONCE AFTERWARDS - MAKE IT A STD 4 TESTING MOVING 4WARD
