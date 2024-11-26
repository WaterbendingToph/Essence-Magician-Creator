import SpecificItemGenerator
''' EVENTUALLY INCLUDE CHECKING OF DESCRIPTIONS ON RETURNED ITEMS, BUT FOR NOW IGNORING THE DESCRIPTION OF EVERY ITEM WHEN TESTING FOR CORRECTNESS'''
''' FOR NOW ALWAYS MAKE SURE THAT THE DESCRIPTION IS THE LAST LINE RETURNED TO MAKE THE RETURNING INFORMATION VALID JSON WHEN IT IS PULLED OUT SO I CAN SETUP AUTOMATIC VERIFICATION IF I WANT TO'''

'''
    NOTES TO SELF ABOUT HOW THIS TEST SUITE WRITING WENT:
        NEXT TIME NEED TO PLAN FOR A runTest() METHOD'S I/O BETTER TO MAKE IT MORE UNIVERSALLY USEFUL TO ALL TESTS RUN.
            THIS ONE WASN'T *AWFUL* BUT COULD HAVE SAVED SO MANY HEADACHES W/ BETTER TEST PLANNING
            PROBABLY WOULD HAVE ELIMINATED OR SEVERELY CHANGED THE batchRunTest() FUNCTIONALITY TOO
        DECIDE ON CONSISTENT OUTPUT SCHEME FROM THE START, NOT INVENTED HALF-WAY THROUGH & KEEP PASS / FAIL EASY TO SEE @ A GLANCE, NOT INCONSISTENT VERTICALLY BTW TESTS
        DECIDE ON WHICH TESTS WOULD BE PROVEN FUNCTIONAL IN WHICH WAYS FROM THE START, THEN ITERATE THROUGH EACH ONE INDIVIDUALLY 
            TO HELP FACILITATE THE T.D.D. PROCESS BY KNOWING THE LEVEL ABOVE IT IS ALL PLANNED OUT 
                FREE UP THE MENTAL SPACE TO DRILL DOWN IN THE T.D.D. W/OUT WORRYING ABOUT OTHER TEST SUITES / ETC ABOVE IT
'''


def stripAndFormat(inputString):
    tempArray = inputString[0].split(',')
    results = tempArray[0]
    for thingLooted in tempArray[1:]:
        if thingLooted.count('"description":') == 0:
            results += '\n' + thingLooted
        else:
            results += '}'
            break
    return results

def runTest(testNumber, testType, targetName, targetRank, lootables='', lootMultiplier=1, targetMaterialRarity='common', typeWeights='', justGetItem=False, testMode=''):
    if testType == 'craftingMat':
        rawOutput = SpecificItemGenerator.generateCraftingMaterials(targetName, targetRank, lootables, lootMultiplier, targetMaterialRarity, typeWeights)
            # INCLUDE TESTING ABILITY FOR EACH OTHER METHOD TO TEST HERE
    elif testType == 'armor':
        rawOutput = SpecificItemGenerator.generateArmorPiece(targetName, targetRank, lootables, targetMaterialRarity, typeWeights)
    elif testType == 'weapon':
        rawOutput = SpecificItemGenerator.generateWeapon(targetName, targetRank, targetMaterialRarity, typeWeights)
    elif testType == 'condensedMagic':
        rawOutput = SpecificItemGenerator.generateCondensedMagic(targetRank, typeWeights, testMode)
    elif testType == 'healingItem':
        rawOutput = SpecificItemGenerator.generateHealingItem(targetRank, lootMultiplier, typeWeights, testMode)
    elif testType == 'potion':
        rawOutput = SpecificItemGenerator.generatePotion(targetRank, lootMultiplier, typeWeights, testMode)
    try:
        if justGetItem == True:
            if lootMultiplier == 1:
                return rawOutput[0]
            return rawOutput
        if lootMultiplier > 1:
            return rawOutput
        results = stripAndFormat(rawOutput)        


        assert(keys[testNumber] == results)

        return str(testNumber) + ' passed\n'
    except AssertionError:
        return str(testNumber) + ' failed with the wrong output of:\n' + results + '\n\n'
    except:
        return str(testNumber) + ' failed due to unknown error, run individually for more information\n'
    
def batchRunTest(testNumber, testType, targetName, targetRank, numIterationsToCall=1, lootables='', lootMultiplier=1, targetMaterialRarity='common', typeWeights='', message=''):
    # SHOULD ONLY BE CALLED WITH EITHER lootMultiplier > 1 OR numIterationsToCall > 1
    if numIterationsToCall > 1 and lootMultiplier > 1:
        return str(testNumber) + ' has failed because it was setup incorrectly. It should only have one of lootMultiplier and numIterationsToCall above 1 to seperate independant testing variables\n'
    justGetItem = True
    if lootMultiplier > 1:
        justGetItem = False
    itemsLooted = []
    for index in range(numIterationsToCall):
        localTestNumber = testNumber
        itemsLooted.append(runTest(localTestNumber, testType, targetName, targetRank, lootables=lootables, lootMultiplier=lootMultiplier, targetMaterialRarity=targetMaterialRarity, typeWeights=typeWeights, justGetItem=justGetItem) )
        localTestNumber += 1
    if type(itemsLooted[0] ) == str and itemsLooted[0].find('failed') != -1:
        return itemsLooted[0]

    lootablesNotFoundYet = lootables
    for index in range(0, len(lootablesNotFoundYet) ):
        if type(lootablesNotFoundYet[index] ) == str:
            lootablesNotFoundYet[index] = lootablesNotFoundYet[index].capitalize()
        elif type(lootablesNotFoundYet[index] ) == list:    # GUARANTEED TO HIT EITHER CASE BY RETURN VALUES OF SpecificItemGenerator.generateCraftingMaterials()
            for secondIndex in lootablesNotFoundYet[index]:
                lootablesNotFoundYet[index][secondIndex] = lootablesNotFoundYet[index][secondIndex].capitalize()

    if numIterationsToCall > 1:
        for index in range(0, len(itemsLooted) ):
            for lootable in lootablesNotFoundYet:
                if itemsLooted[index].find(lootable) != -1:
                    lootablesNotFoundYet.remove(lootable)
                    break
        if len(lootablesNotFoundYet) > 0:
            return str(testNumber) + ' has failed to find one of its lootables! Run again to verify this is not a statistical fluke and increase number of iterations if this occurs regularly\n'    
    
    if lootMultiplier > 1:
        itemsLooted = itemsLooted[0]
        for lootedItem in itemsLooted:
            if lootedItem.find(lootablesNotFoundYet[0] ) == -1:
                return str(testNumber) + ' has returned a value that was not the lootable in one of its return values. Debug to find more detailed information\n'
    
    if message != '':
        if numIterationsToCall > 1:
            return 'test suite numbers ' + str(testNumber) + ' - ' + str(testNumber + numIterationsToCall - 1) + ' passed ' + message + '\n'
        return 'the test number ' + str(testNumber) + ' passed ' + message + '\n'
    return 'the test number ' + str(testNumber) + ' passed\n'



testKey = open('SpecificItemGeneratorTestKey.txt', 'r')
keys = []
for x in range(300):
    nextLine = testKey.read()
    if nextLine == "": 
        break
    keys.append(nextLine.split('\n\n') )
keys = keys[0]





output = open('SpecificItemGeneratorTestOutput.txt', 'w')
runningTestIndex, numTestsBeforeThisSuite = 0, 0
names = ['Magma Ant', 'Water Purlovia', 'Bone Feaster', 'Leech', 'Spotted Tree Leopard', 'Revnant', 'Cinderslinger', 'Greathawk', 'Reef-Breaker', 'Gibbering Mass', 
         'Artic Troll', 'JellyWhale', 'Centaurtaur', 'Bicorn', 'Invisible Ambush Oooze', 'Lava Crocodile', 'Rune Turtle', 'Giant Flounder Fish', 'Heidel', 
         'Demon Wasp', 'Cave Troll', 'Scorpider', 'Bullet Shark', 'Blood Root Vine']


#       TEST ARMOR GENERATION
#   ALREADY WROTE THE ARMOR GEN FUNCTION, JUST HAVE IT REPORT THE SAME WAY THE CRAFTING MAT STUFF DOES BY IMPLEMENTING IT'S RUN THROUGH runTest AND THE EQ. STUFF HERE
armors = ["armored cloak", "armored coat", "bastion plate armor", "breastplate armor", "buckle armor", "ceramic plate armor", "chain mail armor", 
             "chain shirt armor", "coral armor", "explorer's clothing", "fortress plate armor", "full plate armor", "gi", "half plate armor", 
             "half plate armor", "hide armor", "lamellar breastplate armor", "lattice armor", "leaf weave armor", "leather lamellar armor", 
             "padded armor", "quilted armor", "scale mail armor", "scroll robes", "splint mail armor", "studded leather armor", "wooden breastplate armor",
             'buckler', 'wooden shield', "caster's targe", 'hide shield', 'steel sheild', 'heavy rondache', 'meteor shield', 'gauntlet buckler', 
             'harnessed shield', 'razor disk', 'salvo shield', 'swordstealer shield' , 'dart shield', 'tower shield', 'fortress shield']
armorsUnarmored = ["explorer's clothing", "gi", "scroll robes", ]
armorsLight = ["armored cloak", "armored coat", "buckle armor", "chain shirt armor", "leaf weave armor", "leather lamellar armor", "padded armor", 
               "quilted armor", "studded leather armor", ]
armorsMedium = ["breastplate armor", "ceramic plate armor", "chain mail armor", "coral armor", "hide armor", "lamellar breastplate armor", 
                "lattice armor", "scale mail armor", "wooden breastplate armor"]
armorsHeavy = ["bastion plate armor", "fortress plate armor", "full plate armor", "half plate armor", "splint mail armor", ]
armorsShields = ['buckler', 'wooden shield', "caster's targe", 'hide shield', 'steel sheild', 'heavy rondache', 'meteor shield', 'gauntlet buckler', 
                  'harnessed shield', 'razor disk', 'salvo shield', 'swordstealer shield' , 'dart shield', 'tower shield', 'fortress shield']

#   TEST WITH NO LOOTABLES AT ALL
output.write(batchRunTest(testNumber=runningTestIndex, testType='armor', targetName='JellyWhale', targetRank='bronze', numIterationsToCall=25, lootables='', message='with all armor gen tests w/ no lootables') )
runningTestIndex += 25 # 1 lower than # times run because the index is 0 indexed and the count is not
numTestsBeforeThisSuite += 25 # the same here because it is only used to get correct index of the above

#   TEST WITH NO LOOTABLES IN THE POOL THAT WOULD BE USED IN ARMOR MAKING - NEEDS TO VERIFY THAT NO PART USED
nonArmorReadyLootables = ['antennae', 'bone', 'feather', 'fin', 'horn', 'hooves', 'jelly', 'scale', 'shell', 'skin', 'skull', 'stinger']
targetName = 'Scorpider'
testArmor = runTest(testNumber=runningTestIndex, testType='armor', targetName=targetName, targetRank='bronze', lootables=['eye'], justGetItem=True)
verifiedArmorType, verifiedTargetName, verifiedNoLootableUsed = False, False, True
for armor in armors:
    if testArmor.find(' ' + armor + '"') != -1:
        verifiedArmorType = True
if testArmor.find(targetName) != -1:
    verifiedTargetName = True
for bodyPart in nonArmorReadyLootables:
    if testArmor.count(bodyPart) > 0:
        verifiedNoLootableUsed = False
if verifiedArmorType != True or verifiedTargetName != True or verifiedNoLootableUsed != True:
    output.write(str(runningTestIndex) + ' failed one of its verifications run individually for more information\n')
else:
    output.write('the test number ' + str(runningTestIndex) + ' passed, creating an armor not using of the non-armor lootables\n')
runningTestIndex += 1
numTestsBeforeThisSuite += 1

#   TEST WITH LOOTABLES THAT WOULD BE USED IN ARMOR MAKING - NEEDS TO VERIFY THAT ONE PART WAS USED 
usedLootables = ['scale', 'stinger', 'shell']
testArmor = runTest(testNumber=runningTestIndex, testType='armor', targetName=targetName, targetRank='bronze', lootables=usedLootables, justGetItem=True)
verifiedArmorType, verifiedUsedLootable, verifiedTargetName  = False, False, False, 
for armor in armors:
    if testArmor.find(' ' + armor + '"') != -1:
        verifiedArmorType = True
if testArmor.find(targetName) != -1:
    verifiedTargetName = True
for bodyPart in usedLootables:
    if testArmor.find(bodyPart) != -1:
        verifiedUsedLootable = True
if verifiedUsedLootable != True or verifiedArmorType != True or verifiedTargetName != True:
    output.write(str(runningTestIndex) + ' failed one of its verifications run individually for more information\n')
else:
    output.write('the test number ' + str(runningTestIndex) + ' passed, creating an armor type with one of the right lootables for it\n')
runningTestIndex += 1
numTestsBeforeThisSuite += 1

#   TEST LOOTING ARMOR WITH typeWeights
errorFound, verifiedArmorType, unarmoredWeights, lightArmorWeights, mediumArmorWeights, heavyArmorWeights, shieldArmorWeights, targetName= False, False, [100, 1, 1, 1, 1], [1, 100, 1, 1, 1], [1, 1, 100, 1, 1], [1, 1, 1, 100, 1], [1, 1, 1, 1, 100], 'Atom Shadow Boxer'
unarmoredArmorTest = runTest(testNumber=runningTestIndex, testType='armor', targetName=targetName, targetRank='bronze', typeWeights=unarmoredWeights, justGetItem=True)
for armor in armorsUnarmored:
    if unarmoredArmorTest.find(armor) != -1:
        verifiedArmorType = True
        break
if verifiedArmorType == False:
    errorFound = True
    output.write(str(runningTestIndex) + ' failed to be of the unarmored armor type, run again to verify this is not a mathematic anomaly\n' )
verifiedArmorType = False
runningTestIndex += 1

lightArmorTest = runTest(testNumber=runningTestIndex, testType='armor', targetName=targetName, targetRank='bronze', typeWeights=lightArmorWeights, justGetItem=True)
for armor in armorsLight:
    if lightArmorTest.find(armor) != -1:
        verifiedArmorType = True
        break
if verifiedArmorType == False:
    errorFound = True
    output.write(str(runningTestIndex) + ' failed to be of the light armor type, run again to verify this is not a mathematic anomaly\n' )
verifiedArmorType = False
runningTestIndex += 1

mediumArmorTest = runTest(testNumber=runningTestIndex, testType='armor', targetName=targetName, targetRank='bronze', typeWeights=mediumArmorWeights, justGetItem=True)
for armor in armorsMedium:
    if mediumArmorTest.find(armor) != -1:
        verifiedArmorType = True
        break
if verifiedArmorType == False:
    errorFound = True
    output.write(str(runningTestIndex) + ' failed to be of the medium armor type, run again to verify this is not a mathematic anomaly\n' )
verifiedArmorType = False
runningTestIndex += 1

heavyArmorTest = runTest(testNumber=runningTestIndex, testType='armor', targetName=targetName, targetRank='bronze', typeWeights=heavyArmorWeights, justGetItem=True)
for armor in armorsHeavy:
    if heavyArmorTest.find(armor) != -1:
        verifiedArmorType = True
        break
if verifiedArmorType == False:
    errorFound = True
    output.write(str(runningTestIndex) + ' failed to be of the heavy armor type, run again to verify this is not a mathematic anomaly\n' )
verifiedArmorType = False
runningTestIndex += 1

shieldArmorTest = runTest(testNumber=runningTestIndex, testType='armor', targetName=targetName, targetRank='bronze', typeWeights=shieldArmorWeights, justGetItem=True)
for armor in armorsShields:
    if shieldArmorTest.find(armor) != -1:
        verifiedArmorType = True
        break
if verifiedArmorType == False:
    errorFound = True
    output.write(str(runningTestIndex) + ' failed to be of the shields armor type, run again to verify this is not a mathematic anomaly\n' )
verifiedArmorType = False
runningTestIndex += 1

if errorFound == False:
    output.write('test suite numbers ' + str(runningTestIndex - 5) + ' - ' + str(runningTestIndex) + ' passed finding all of the correct armor types with weights\n')
numTestsBeforeThisSuite += 5


#       TEST LOOTING CRAFTING MATS
#   TEST EVERY INDIVIDUAL CRAFTING MAT ON THEIR OWN
materials = ['antennae', 'beak', 'bone', 'blood', 'claw', 'ectoplasm', 'elemental organ', 'feather', 'fin', 'eye', 'hair', 'heart', 'hooves', 'horn', 'jelly', 
                        'scale', 'shell', 'skin', 'skull', 'stinger', 'stomach', 'tail', 'teeth', 'vine']
individualCraftingMatTests, errorFound = [], False
for index in range(len(materials) ):
    individualCraftingMatTests.append(runTest(testNumber=runningTestIndex, testType='craftingMat', targetName=names[index], targetRank='bronze', lootables=materials[index] ) )
    if individualCraftingMatTests[runningTestIndex - numTestsBeforeThisSuite].count('passed') != 1:
        output.write('Test Number ' + str(runningTestIndex) + ' of the individualCraftingMatTests has failed, run idividually for more information\n')
        errorFound = True
    runningTestIndex += 1
if errorFound == False:
    output.write('test suite numbers ' + str(runningTestIndex - len(materials) ) + ' - ' + str(runningTestIndex) + ' passed finding all the correct individual crafting mats\n')
numTestsBeforeThisSuite += len(materials)

#   TEST HAVING MULTIPLE POSSIBLE CRAFTING MATS FOR ONE LOOTED THING
output.write(batchRunTest(testNumber=runningTestIndex, testType='craftingMat', targetName='Magma Ant', targetRank='bronze', numIterationsToCall=25, lootables=materials[:5], message='with all tests with multiple poss crafting mats' ) )
runningTestIndex += 25
numTestsBeforeThisSuite += 25

#   TEST HAVING A HIGHER LOOT MULTIPLIER THAN 1
output.write(batchRunTest(testNumber=runningTestIndex, testType='craftingMat', targetName='Bone Feaster', targetRank='bronze', numIterationsToCall=1, lootables=materials[2:3], lootMultiplier=5, message='the test with multiple looted crafting mats') )
runningTestIndex += 1
numTestsBeforeThisSuite += 1


#       TEST LOOTING WEAPONS
weaponsSimple = ['atlatl', 'battle lute', 'blowgun', 'club', 'dagger', 'frying pan', 'hand cannon', 'hand crossbow', 'javelin', 'katar', 'knuckle duster', 
                 'light mace', 'longspear', 'sickle', 'sling', 'spear', 'mace', 'morningstar', 'nightstick', 'staff', 'throwing knife']
weaponsMartial = ['backpack ballista', 'bastard sword', 'battle axe', 'bayonet', 'bladed gauntlet', 'blunderbuss', 'bo staff', 'bola', 'boomerang', 
                  'chakram', 'claw blade', 'composite longbow', 'composite shortbow', 'crossbow', 'dart umbrella', 'dueling spear', 'earthbreaker', 
                  'falchion', 'fighting fan', 'fighting stick', 'flail', 'flyssa', 'glaive', 'greataxe', 'greatclub', 'greatpick', 'greatsword', 'halberd', 
                  'harpoon', 'hatchet', 'heavy crossbow', 'injection spear', 'katana', 'khopesh', 'kukri', 'lance', 'light hammer', 'light pick', 'longbow', 
                  'longsword', 'machete', 'maul', 'meteor hammer', 'nunchaku', 'piranha kiss', 'rapier', 'repeating crossbow', 'repeating hand crossbow', 
                  'repeating heavy crossbow', 'rope dart', 'rotary bow', 'scimitar', 'scorpion whip', 'scourge', 'scythe', 'shortbow', 'shortsword', 'shuriken', 
                  'sun sling', 'sword cane', 'tonfa', 'thorn whip', 'trident', 'war flail', 'warhammer', 'whip', 'wrist launcher']
weaponsAdvanced = ['backpack catapult', 'bladed hoop', 'broadspear', 'butchering axe', 'chain sword', 'daikyu', 'hook sword', 'karambit', 'spiral rapier']
weaponList = weaponsSimple + weaponsMartial + weaponsAdvanced
#   TEST LOOTING ONE WEAPON WITH NO typeWeights
numTestsInSuite, errorFound, targetName = 10, False, 'Siege Golem'
for x in range(numTestsInSuite):
    lootedWeapon = runTest(testNumber=runningTestIndex, testType='weapon', targetName=targetName, targetRank='bronze', justGetItem=True)
    verifiedTargetName, verifiedWeaponType = False, False
    for weapon in weaponList:
        if lootedWeapon.find(weapon.capitalize() ) != -1:
            verifiedWeaponType = True
            break
    if lootedWeapon.find(targetName) != -1:
        verifiedTargetName = True
    if verifiedTargetName != True or verifiedWeaponType != True:
        errorFound = True
        output.write(str(runningTestIndex) + ' failed to verify something with output:\n' + lootedWeapon + '\n')
    runningTestIndex += 1
if errorFound == False:
    output.write('test suite numbers ' + str(numTestsBeforeThisSuite - 1) + ' - ' + str(numTestsBeforeThisSuite - 1 + numTestsInSuite) + ' passed and created weapons without weights\n')
numTestsBeforeThisSuite += numTestsInSuite

#   TEST LOOTING ONE WEAPON WITH typeWeights
errorFound, verifiedWeaponType, simpleWeights, martialWeights, advancedWeights, targetName= False, False, [100, 1, 1], [1, 100, 1], [1, 1, 100], 'Clockwork King'
simpleWeaponTest = runTest(testNumber=runningTestIndex, testType='weapon', targetName=targetName, targetRank='bronze', typeWeights=simpleWeights, justGetItem=True)
for weapon in weaponsSimple:
    if simpleWeaponTest.find(weapon) != -1:
        verifiedWeaponType = True
        break
if verifiedWeaponType == False:
    errorFound = True
    output.write(str(runningTestIndex) + ' failed to be of the simple weapon type, run again to verify this is not a mathematic anomaly\n' )
verifiedWeaponType = False
runningTestIndex += 1

martialWeaponTest = runTest(testNumber=runningTestIndex, testType='weapon', targetName=targetName, targetRank='bronze', typeWeights=martialWeights, justGetItem=True)
for weapon in weaponsMartial:
    if martialWeaponTest.find(weapon) != -1:
        verifiedWeaponType = True
        break
if verifiedWeaponType == False:
    errorFound = True
    output.write(str(runningTestIndex) + ' failed to be of the martial weapon type, run again to verify this is not a mathematic anomaly\n' )
verifiedWeaponType = False
runningTestIndex += 1

advancedWeaponTest = runTest(testNumber=runningTestIndex, testType='weapon', targetName=targetName, targetRank='bronze', typeWeights=martialWeights, justGetItem=True)
for weapon in weaponsMartial:
    if advancedWeaponTest.find(weapon) != -1:
        verifiedWeaponType = True
        break
if verifiedWeaponType == False:
    errorFound = True
    output.write(str(runningTestIndex) + ' failed to be of the advanced weapon type, run again to verify this is not a mathematic anomaly\n' )
verifiedWeaponType = False
runningTestIndex += 1
numTestsBeforeThisSuite += 3
if errorFound == False:
    output.write('test suite numbers ' + str(runningTestIndex - 3) + ' - ' + str(runningTestIndex) + ' passed and created weapons of the correct types using weights\n')


#       TEST LOOTING CONDENSED MAGIC
#   TEST ESSENCE
testResults = runTest(testNumber=runningTestIndex, testType='condensedMagic', targetName='filler string', targetRank='bronze', testMode='essence')
output.write('the test number ' + testResults[:-1]+ ' testing looting an unspecified type essence\n')
runningTestIndex += 1

#   TEST AWAKENING STONE
testResults = runTest(testNumber=runningTestIndex, testType='condensedMagic', targetName='filler string', targetRank='bronze', testMode='awakening stone')
output.write('the test number ' + testResults[:-1] + ' testing looting an unspecified type awakening stone\n')
runningTestIndex += 1

#   TEST QUINTESSENCE
testResults = runTest(testNumber=runningTestIndex, testType='condensedMagic', targetName='filler string', targetRank='bronze', testMode='quintessence')
output.write('the test number ' + testResults[:-1] + ' testing looting an unspecified type quintessence\n')
runningTestIndex += 1
numTestsBeforeThisSuite += 3


#       TEST LOOTING HEALING ITEMS
healingItemTypes = ['healing poultice', 'healing unguent', 'healing potion', 'recovery potion', 'antidote', 'miracle potion']
for healingItem in healingItemTypes:
    testResults = runTest(testNumber=runningTestIndex, testType='healingItem', targetName='filler string', targetRank='gold', testMode=healingItem)
    output.write('the test number ' + testResults[:-1] + ' testing looting an unspecified type ' + healingItem + ' from genHealingItem()\n')
    runningTestIndex += 1
numTestsBeforeThisSuite += len(healingItemTypes)


#       TEST LOOTING POTIONS
potionTypes = ['health', 'mana', 'stamina', 'stone skin', 'spirit', 'power', 'agility', 'recovery', 'rank increase', 'momentum', 
               'one punch', 'frenzy', 'invisibility']

for potion in potionTypes:
    testResults = runTest(testNumber=runningTestIndex, testType='potion', targetName='filler string', targetRank='bronze', testMode=potion)
    output.write('the test number ' + testResults[:-1] + ' testing looting an unspecified type ' + potion + ' potion from genPotion()\n')
    runningTestIndex += 1
numTestsBeforeThisSuite += len(potionTypes)

testResults = runTest(testNumber=runningTestIndex, testType='potion', targetName='filler string', targetRank='gold', testMode='miracle')
output.write('the test number ' + testResults[:-1] + ' testing looting an unspecified type miracle potion from genPotion()\n')
runningTestIndex += 1
numTestsBeforeThisSuite += 1


