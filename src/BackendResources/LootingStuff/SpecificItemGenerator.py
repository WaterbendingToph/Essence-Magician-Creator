import random

'''
    NOTES TO SELF:
    - WHEN ADDING DESCRIPTIONS / EFFECTS / RARITIES EVERYTHING SPECIFIC SHOULD BE LISTED AFTER DESCRIPTION OR IT'LL FAIL TESTS
    TODO:
    - ADD DESCRIPTIONS TO EVERYTHING       --\ 
    - ADD EFFECTS TO EVERYTHING               |     HOW SHOULD THIS ALL BE ORGANIZED EFFICIENTLY?
    - ADD VALUES TO EVERYTHING                |         GENERATIVE @ RUNTIME? BANK OF POSSIBLES?
    - ADD RARITIES TO POTIONS & HEALS      --/
'''

affinitiesList = ['none', 'rigid', 'incorporeal', 'life', 'death', 'holy', 'unholy', 'astral', 'swarm', 'corruption', 'magic', 'fire', 'water',
                   'earth', 'wind', 'iron', 'lightning', 'plant', 'cold', 'light', 'dark']
armorsUnarmored = ["explorer's clothing", "gi", "scroll robes", ]
armorsLight = ["armored cloak", "armored coat", "buckle armor", "chain shirt armor", "leaf weave armor", "leather lamellar armor", "padded armor", 
               "quilted armor", "studded leather armor", ]
armorsMedium = ["breastplate armor", "ceramic plate armor", "chain mail armor", "coral armor", "hide armor", "lamellar breastplate armor", 
                "lattice armor", "scale mail armor", "wooden breastplate armor"]
armorsHeavy = ["bastion plate armor", "fortress plate armor", "full plate armor", "half plate armor", "splint mail armor", ]
armorsShields = ['buckler', 'wooden shield', "caster's targe", 'hide shield', 'steel sheild', 'heavy rondache', 'meteor shield', 'gauntlet buckler', 
                  'harnessed shield', 'razor disk', 'salvo shield', 'swordstealer shield' , 'dart shield', 'tower shield', 'fortress shield']
armorList = armorsUnarmored + armorsLight + armorsMedium + armorsHeavy + armorsShields
awakeningStonesList = ['adept', 'ape', 'armor', 'axe', 'balance', 'bat', 'bear', 'bee', 'bird', 'blight', 'blood', 'bone', 'bow', 'cage', 'cat', 
                       'cattle', 'chain', 'claw', 'cloth', 'cloud', 'cold', 'coral', 'corrupt', 'crocodile', 'crystal', 'dance', 'dark', 'death', 
                       'deep', 'deer', 'dimension', 'discord', 'dog', 'duck', 'dust', 'earth', 'echo', 'elemental', 'eye', 'feast', 'feeble', 
                       'fire', 'fish', 'flea', 'flesh', 'foot', 'fork', 'fox', 'frog', 'fungus', 'gathering', 'glass', 'goat', 'grazen', 'growth', 
                       'gun', 'hair', 'hammer', 'hand', 'harmonic', 'heidel', 'hook', 'horse', 'hunger', 'hunt', 'ice', 'iron', 'knife', 'knowledge', 
                       'life', 'light', 'lightning', 'lizard', 'locust', 'lurker', 'magic', 'malign', 'manatee', 'might', 'mirage', 'mirror', 
                       'monkey', 'moon', 'mouse', 'myriad', 'needle', 'net', 'octopus', 'omen', 'owl', 'pangolin', 'paper', 'plant', 'potent', 
                       'pure', 'rabbit', 'rake', 'rat', 'renewal', 'resolute', 'rune', 'sand', 'scepter', 'serene', 'shark', 'shield', 'shimmer', 
                       'ship', 'shovel', 'sickle', 'sin', 'skunk', 'sloth', 'smoke', 'snake', 'song', 'spear', 'spider', 'spike', 'staff', 'star', 
                       'sun', 'swift', 'sword', 'technology', 'tentacle', 'thread', 'trap', 'tree', 'trowel', 'turtle', 'vast', 'vehicle', 'venom', 
                       'visage', 'void', 'wall', 'wasp', 'water', 'whale', 'wheel', 'whip', 'wind', 'wing', 'wolf', 'wood', 'zeal', 'action', 
                       'alchemy', 'ambush', 'animate', 'anzu', 'arsenal', 'avatar', 'battlfield', 'beguiling', 'behemoth', 'boundary', 'bounty', 
                       'cataclysm', 'chaotic', 'charlatan', 'chimera', 'cyborg', 'cycle', 'cyclops', 'dawn', 'desolate', 'discordant', 'doom', 
                       'doppleganger', 'dragon', 'eclipse', 'edifice', 'effigy', 'empower', 'fertility', 'fey', 'firebird', 'force', 'forge', 
                       'fortress', 'garuda', 'gate', 'glimeron', 'gorgon', 'griffon', 'guardian', 'harpy', 'harvest', 'hydra', 'immortal', 
                       'jackalope', 'juggernaut', 'karmic', 'kraken', 'leviathan', 'lotus', 'magitech', 'manticore', 'master', 'medusa', 
                       'ministration', 'minotaur', 'mystic', 'nebula', 'nemesis', 'oasis', 'ocean', 'onslaught', 'phantasmagoria', 'pheonix', 
                       'predatory', 'prison', 'prosperity', 'refracting', 'resonating', 'roc', 'sacrafice', 'scribe', 'serpent', 'simulacrum', 
                       'skirmish', 'sky', 'soaring', 'sovereign', 'stellar', 'storm', 'succubus', 'swarm', 'talisman', 'thunderbird', 'time', 
                       'tranquil', 'transfiguration', 'transgression', 'troll', 'twilight', 'undeath', 'unity', 'verdant', 'vessel', 'vision', 
                       'volcano', 'vortex', 'weave', 'wendigo', 'wrath', 'ziz', 'focus', 'preparation', 'reach', 'wrath', 'adventure', 'judgement', 
                       'persistence', 'ruin', 'absolution', 'champion', 'moment', 'purgation', 'surge', 'inevitability', 'apocalypse', 'celestial', 
                       'reaper', 'rune touched', 'leonines', 'humanities', 'fey touched', 'celestial book', 'defiance', 'secrets', 'discovery', 
                       'wonder', 'imagination', 'ingenuity']
craftingRawMaterials = ['antennae', 'beak', 'bone', 'blood', 'claw', 'ectoplasm', 'elemental organ', 'feather', 'fin', 'eye', 'hair', 'heart', 'hooves', 
                        'horn', 'jelly', 'scale', 'shell', 'skin', 'skull', 'stinger', 'stomach', 'tail', 'teeth', 'vine']
damageTypes = ['astral', 'blunt', 'cautstic', 'cold', 'constriction', 'corruption', 'dark', 'death', 'disruptive force', 'earth', 'fire', 'holy', 
               'iron', 'life', 'light', 'lightning', 'magic', 'pierce' ,'plant', 'resonating force', 'retributive', 'slice', 'transcendant', 
               'unholy', 'water', 'wind']
essenceTypes = ['adept', 'ape', 'armor', 'axe', 'balance', 'bat', 'bear', 'bee', 'bird', 'blight', 'blood', 'bone', 'bow', 'cage', 'cat', 'cattle', 
                'chain', 'claw', 'cloth', 'cloud', 'cold', 'coral', 'corrupt', 'crocodile', 'crystal', 'dance', 'dark', 'death', 'deep', 'deer', 
                'dimension', 'discord', 'dog', 'duck', 'dust', 'earth', 'echo', 'elemental', 'eye', 'feast', 'feeble', 'fire', 'fish', 'flea', 
                'flesh', 'foot', 'fork', 'fox', 'frog', 'fungus', 'gathering', 'glass', 'goat', 'grazen', 'growth', 'gun', 'hair', 'hammer', 'hand', 
                'harmonic', 'heidel', 'hook', 'horse', 'hunger', 'hunt', 'ice', 'iron', 'knife', 'knowledge', 'life', 'light', 'lightning', 'lizard', 
                'locust', 'lurker', 'magic', 'malign', 'manatee', 'might', 'mirage', 'mirror', 'monkey', 'moon', 'mouse', 'myriad', 'needle', 'net', 
                'octopus', 'omen', 'owl', 'pangolin', 'paper', 'plant', 'potent', 'pure', 'rabbit', 'rake', 'rat', 'renewal', 'resolute', 'rune', 
                'sand', 'scepter', 'serene', 'shark', 'shield', 'shimmer', 'ship', 'shovel', 'sickle', 'sin', 'skunk', 'sloth', 'smoke', 'snake', 
                'song', 'spear', 'spider', 'spike', 'staff', 'star', 'sun', 'swift', 'sword', 'technology', 'tentacle', 'thread', 'trap', 'tree', 
                'trowel', 'turtle', 'vast', 'vehicle', 'venom', 'visage', 'void', 'wall', 'wasp', 'water', 'whale', 'wheel', 'whip', 'wind', 'wing', 
                'wolf', 'wood', 'zeal', 'action', 'alchemy', 'ambush', 'animate', 'anzu', 'arsenal', 'avatar', 'battlfield', 'beguiling', 'behemoth', 
                'boundary', 'bounty', 'cataclysm', 'chaotic', 'charlatan', 'chimera', 'cyborg', 'cycle', 'cyclops', 'dawn', 'desolate', 'discordant', 
                'doom', 'doppleganger', 'dragon', 'eclipse', 'edifice', 'effigy', 'empower', 'fertility', 'fey', 'firebird', 'force', 'forge', 
                'fortress', 'garuda', 'gate', 'glimeron', 'gorgon', 'griffon', 'guardian', 'harpy', 'harvest', 'hydra', 'immortal', 'jackalope', 
                'juggernaut', 'karmic', 'kraken', 'leviathan', 'lotus', 'magitech', 'manticore', 'master', 'medusa', 'ministration', 'minotaur', 
                'mystic', 'nebula', 'nemesis', 'oasis', 'ocean', 'onslaught', 'phantasmagoria', 'pheonix', 'predatory', 'prison', 'prosperity', 
                'refracting', 'resonating', 'roc', 'sacrafice', 'scribe', 'serpent', 'simulacrum', 'skirmish', 'sky', 'soaring', 'sovereign', 
                'stellar', 'storm', 'succubus', 'swarm', 'talisman', 'thunderbird', 'time', 'tranquil', 'transfiguration', 'transgression', 'troll', 
                'twilight', 'undeath', 'unity', 'verdant', 'vessel', 'vision', 'volcano', 'vortex', 'weave', 'wendigo', 'wrath', 'ziz']
healingItemTypes = ['unguent', 'poultice', 'healing potion', 'recovery potion', 'antidote'] # ALSO INCLUDES A MIRACLE POTION DEALT W/ IN GenHeal
potionQualities = ['lesser', 'moderate', 'greater', 'superior', 'master-crafted']
potionTypes = ['health', 'mana', 'stamina', 'miracle', 'stone skin', 'spirit', 'power', 'agility', 'recovery', 'rank increase', 'momentum', 
               'one punch', 'frenzy', 'invisibility']
quintessenceTypes = ['adept', 'ape', 'armor', 'axe', 'balance', 'bat', 'bear', 'bee', 'bird', 'blight', 'blood', 'bone', 'bow', 'cage', 'cat', 
                     'cattle', 'chain', 'claw', 'cloth', 'cloud', 'cold', 'coral', 'corrupt', 'crocodile', 'crystal', 'dance', 'dark', 'death', 
                     'deep', 'deer', 'dimension', 'discord', 'dog', 'duck', 'dust', 'earth', 'echo', 'elemental', 'eye', 'feast', 'feeble', 'fire', 
                     'fish', 'flea', 'flesh', 'foot', 'fork', 'fox', 'frog', 'fungus', 'gathering', 'glass', 'goat', 'grazen', 'growth', 'gun', 'hair', 
                     'hammer', 'hand', 'harmonic', 'heidel', 'hook', 'horse', 'hunger', 'hunt', 'ice', 'iron', 'knife', 'knowledge', 'life', 'light', 
                     'lightning', 'lizard', 'locust', 'lurker', 'magic', 'malign', 'manatee', 'might', 'mirage', 'mirror', 'monkey', 'moon', 'mouse', 
                     'myriad', 'needle', 'net', 'octopus', 'omen', 'owl', 'pangolin', 'paper', 'plant', 'potent', 'pure', 'rabbit', 'rake', 'rat', 
                     'renewal', 'resolute', 'rune', 'sand', 'scepter', 'serene', 'shark', 'shield', 'shimmer', 'ship', 'shovel', 'sickle', 'sin', 
                     'skunk', 'sloth', 'smoke', 'snake', 'song', 'spear', 'spider', 'spike', 'staff', 'star', 'sun', 'swift', 'sword', 'technology', 
                     'tentacle', 'thread', 'trap', 'tree', 'trowel', 'turtle', 'vast', 'vehicle', 'venom', 'visage', 'void', 'wall', 'wasp', 'water', 
                     'whale', 'wheel', 'whip', 'wind', 'wing', 'wolf', 'wood']
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

def generateArmorPiece(targetName, targetRank, lootables='', targetLootRarity='common', typeWeights=''):
    '''     ORDER IS: Name, Rank, Rarity, Value, Description, Effects (list only as many as are used)'''
    '''     FORMAT FOR OUTPUT IS ONE ITEM WITHIN A LIST'''
    returnValue = '{"name":"' + targetName + ' '

    if lootables != '':
        lootablesToUseInArmor = ['antennae', 'bone', 'feather', 'fin', 'horn', 'hooves', 'jelly', 'scale', 'shell', 'skin', 'skull', 'stinger']
        foundUsablePart, usableLootables = False, []
        for part in lootablesToUseInArmor:
            if lootables.count(part) > 0:
                foundUsablePart = True
                usableLootables.append(part)
        if foundUsablePart == True:
            returnValue += random.choices(population=usableLootables, k=1)[0] + ' '

    armorName = ''
    if typeWeights == '':
        armorName = random.choices(population=armorList, k=1)[0]
    else:
        convertedTypeWeights = []
        for x in range(len(armorsUnarmored) ):
            convertedTypeWeights.append(typeWeights[0] )
        for x in range(len(armorsLight) ):
            convertedTypeWeights.append(typeWeights[1] )
        for x in range(len(armorsMedium) ):
            convertedTypeWeights.append(typeWeights[2] )
        for x in range(len(armorsHeavy) ):
            convertedTypeWeights.append(typeWeights[3] )
        for x in range(len(armorsShields) ):
            convertedTypeWeights.append(typeWeights[4] )
        armorName = random.choices(population=armorList, weights=convertedTypeWeights, k=1)[0]
    returnValue += armorName

    returnValue += '", "rank":"' + targetRank + '", "rarity":"' + targetLootRarity + '", "Description": This looted ' + targetName + ' ' + armorName + ' can be worn, has a description, some special magical effects, and value that will be unlocked as soon as the DM has more time."}'
    return [returnValue]

def generateCondensedMagic(targetRank, typeWeights='', testMode=''):
    '''     ORDER IS: Name, Rank, Value, Description    '''
    '''     FOR NOW MAKE A GENERIC TYPE OF: Essence, Awakening Stone, or Quintessence WITH A DESCRIPTION SAYING HEY ASK THE DM WHAT TYPE YOU JUST GOT   '''
    possibleReturnTypes, returnValue = ['essence', 'awakening stone', 'quintessence'], '{"name":"'
    if testMode == '':
        returnType = random.choices(population=possibleReturnTypes, weights=[1, 10, 100], k=1)
    else:
        returnType = testMode

    if returnType == 'essence':
        returnValue += 'Essence of unknown type", "rank":"unranked"'
    elif returnType == 'awakening stone':
        returnValue += 'Awakening Stone of unknown type", "rank":"unranked"'
    elif returnType == 'quintessence':
        returnValue += 'Quintessence of unknown type", "rank":"' + targetRank + '"'

    returnValue += ', "rarity":"varies"}'
    return [returnValue]

def generateCraftingMaterials(targetName, targetRank, lootables, lootMultiplier=1, targetMaterialRarity = 'common', typeWeights=''):
    ''' ORDER IS: Name, Rank, Rarity, Value, Description '''
    returnValue = []
    newMaterial = '{"name":"' + targetName

    if type(lootables) == list and len(lootables) >= 2:
        if typeWeights == '':
            matTypeName = random.choices(population=lootables, k=1)[0]
        else:
            matTypeName = random.choices(population=lootables, weights=typeWeights, k=1)[0]
    elif type(lootables) == list and len(lootables) == 1:
        matTypeName = lootables[0]
    elif type(lootables) == str:
        matTypeName = lootables
    else:
        return 'This test failed because  ' + targetName + ' was called to drop a crafting material and did not provide a single string crafting material or list of possible crafting materials to loot from it!!\n'
    matTypeName = matTypeName.capitalize()

    newMaterial += ' ' + matTypeName + '", "rank"="' + targetRank + '", "targetMaterialRarity":"' + targetMaterialRarity + '", '

    description = '"description":"This looted ' + targetName + ' ' + matTypeName + ' can be used in some form of crafting to make magical objects. More details (in both description and value) will be unlocked when the DM has more time."}'
    newMaterial += description

    for iteratorNum in range(lootMultiplier):
        returnValue.append(newMaterial)

    return returnValue

def generatePotion(targetRank, lootMultiplier, typeWeights='', testMode=''):
    '''     ORDER IS: Name, Rank, Rarity, Description, Value, Effects (list only as many as are used) '''
    '''     TODO:   INCLUDE LOOTING RANDOM RARITY FOR EACH HEALING ITEM, EACH W/ ITS OWN PARTICULAR DESCRIPTION 
    '''
    results, returnType = '{"name":"', ''
    
    if typeWeights == '':
        typeWeights = [500, 500, 500, 1, 50, 100, 100, 100, 100, 50, 50, 100, 50, 50]
            # THIS LINE IS NECESSARY WHEN potionTypes HAS NO MIRACLE POTION OPTION
        if len(typeWeights) > len(potionTypes):
            typeWeights.pop(3)
    if potionTypes.count('miracle') > 0 and (targetRank == 'lesser' or targetRank == 'iron' or targetRank == 'bronze'):
        typeWeights.pop(potionTypes.index('miracle') )
        potionTypes.remove('miracle')
    if testMode != '':
        returnType = testMode
    else:
        returnType = random.choices(population=potionTypes, weights=typeWeights, k=1)[0]
    
    results += returnType + ' potion", "rank":"' + targetRank + '", "rarity":"varies", "description":"'
    results += 'This looted ' + returnType + '  can be drunk or applied, has a description, some special magical effects, and value that will be unlocked as soon as the DM has more time."}'
    
    returnValue = []
    for iteratorNum in range(lootMultiplier):
        returnValue.append(results)
    return returnValue

def generateHealingItem(targetRank, lootMultiplier, typeWeights='', testMode='', testRarity=''):
    '''     ORDER IS: Name, Rank, Rarity, Description, Value, Effects (list only as many as are used) '''
    '''     TODO:   INCLUDE LOOTING RANDOM RARITY FOR EACH HEALING ITEM, EACH W/ ITS OWN PARTICULAR DESCRIPTION 
                    MAKE LOOTING POTIONS OF ANY KIND CALL THE POTION CRAFTING METHOD
                    UPDATING THE TEST KEY TO FIT ANY CHANGES MADE OF COURSE - USE testRarity 4 IT
    '''
    returnType, results = '', '{"name":"'
    
    if testMode != '':
        returnType = testMode
    else:
        if typeWeights == '':
            typeWeights = [10, 10, 2, 1, 1]
        if targetRank == 'lesser':
            typeWeights = typeWeights[:2]
            healingItemTypes = healingItemTypes[:2]
        elif targetRank == 'silver' or targetRank == 'gold' or targetRank == 'diamond':
            for index in range(len(typeWeights) ):
                typeWeights[index] = typeWeights[index] * 100
            typeWeights.append(1)
            healingItemTypes.append('miracle potion')
            #   FOR ANY OF THE POTIONS WHEN CREATED BY THIS METHOD MAKE THE 'JUST GIVE IT TO ME' VERSION OF GENERATE POTION TO CALL FOR THE ITEM
            #   LESSER MONSTERS LOOTED SHOULD NOT BE ABLE TO GIVE ANYTHING BUT HEALING POULTICE OR UNGUENT
        returnType = random.choices(population=healingItemTypes, weights=typeWeights, k=1)[0].title()

    results += returnType + '", "rank":"' + targetRank + '", "rarity":"varies", "' + 'description":"'
    results += 'This looted ' + returnType + ' potion can be used to heal, has a description, some special magical effects, and value that will be unlocked as soon as the DM has more time."}'

    returnValue = []
    for iteratorNum in range(lootMultiplier):
        returnValue.append(results)

    return returnValue

def generateRandomItem(targetName, targetRank, targetLootRarity='common', lootMultiplier=2):
    possibilities = ['armor', 'potion', 'weapon']
    selection = random.choices(population=possibilities, k=1)[0]
    if selection == 'armor':
        return generateArmorPiece(targetName, targetRank, targetLootRarity)
    if selection == 'potion':
        return generatePotion(targetRank, lootMultiplier)
    ''' selection == weapon '''       
    return generateWeapon(targetName, targetRank, targetLootRarity)

def generateWeapon(targetName, targetRank, targetLootRarity='common', typeWeights=''):
    '''     ORDER IS: Name, Rank, Rarity, Value, Description, Effects (list only as many as are used) '''
    returnValue = '{"name":"' + targetName + ' '

    if typeWeights == '':
        weaponName = random.choices(population=weaponList, k=1)[0].capitalize()
    else:
        convertedTypeWeights = []
        for x in range(len(weaponsSimple) ):
            convertedTypeWeights.append(typeWeights[0] )
        for x in range(len(weaponsMartial) ):
            convertedTypeWeights.append(typeWeights[1] )
        for x in range(len(weaponsAdvanced) ):
            convertedTypeWeights.append(typeWeights[2] )
        weaponName = random.choices(population=weaponList, weights=convertedTypeWeights, k=1)[0]
    returnValue += weaponName + '", "rank":"' + targetRank + '", "rarity":"' + targetLootRarity + '", ""description": This looted ' + targetName + ' ' + weaponName + ' can be weilded, has a description, some special magical effects, and value that will be unlocked as soon as the DM has more time."}'

    return [returnValue]

