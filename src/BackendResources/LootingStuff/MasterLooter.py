import random
import SpecificItemGenerator
'''
targetMagicLevel    = placement of target in power scale along that rank, lowest = freshly minted user of rank / swarm monster 
targetRank          = 'lesser', 'iron', 'bronze', 'silver', 'gold', 'diamond' of the thing looted
looterRank          = same as above 4 essence user doing the looting
lootMultiplier      = chance for ability to give extra loot for its own reason
isMonster           = True if a monster 2 get crafting mats from it & False 4 people 2 not give hair rope from the guy you killed
typeWeights         = [ EquipmentChance, [1 / Equipment Type], [1 / Consumable Type] ]
'''
def getGoodies(numberOf, type, rank):
    resultString = '"' + rank
    if type == 'coins':
        resultString += ' spirit ' 
    elif type == 'cores':
        resultString += ' monster '
    resultString += type + '":"' + str(numberOf)+ '"'
    if type == 'coins':
        resultString += ','
    return resultString

def generateCoinsAndCores(targetRank, monetaryMultiplier):
    resultString, coinCount, coreCount = '', 10 * monetaryMultiplier, 1 * monetaryMultiplier

    if targetRank == 'lesser':
        resultString += getGoodies(coinCount, 'coins', targetRank) + getGoodies(coreCount, 'cores', targetRank)

    elif targetRank == 'iron':
        resultString += getGoodies(coinCount, 'coins', targetRank) + getGoodies(coinCount * 10, 'coins', 'lesser')
        resultString += getGoodies(coreCount, 'cores', targetRank)        

    elif targetRank == 'bronze':
        resultString += getGoodies(coinCount, 'coins', targetRank) + getGoodies(coinCount * 10, 'coins', 'iron')
        resultString += getGoodies(coreCount, 'cores', targetRank)

    elif targetRank == 'silver':
        resultString += getGoodies(coinCount, 'coins', targetRank) + getGoodies(coinCount * 10, 'coins', 'bronze')
        resultString += getGoodies(coinCount * 100, 'coins', 'iron') + getGoodies(coreCount, 'cores', targetRank)

    elif targetRank == 'gold':
        resultString += getGoodies(coinCount, 'coins', targetRank) + getGoodies(coinCount * 10, 'coins', 'silver')
        resultString += getGoodies(coinCount * 100, 'coins', 'bronze') + getGoodies(coinCount * 1000, 'coins', 'iron')
        resultString += getGoodies(coreCount, 'cores', targetRank)

    elif targetRank == 'diamond':
        resultString += getGoodies(coinCount, 'coins', targetRank) + getGoodies(coinCount * 100, 'coins', 'gold')
        resultString += getGoodies(coinCount * 1000, 'coins', 'silver') + getGoodies(coinCount * 10000, 'coins', 'bronze')
        resultString += getGoodies(coinCount * 100000, 'coins', 'iron') + getGoodies(coreCount, 'cores', targetRank)

    return resultString   

def generateEquipmentPiece(targetRank, equipmentTypeWeights=''):
    return ''

def generatePotion(targetRank, consumableTypeWeights=''):
    return ''

def generateHealingItem(targetRank, healingTypeWeights=''):     # CALL POTION IF MAKING A HEALING POTION
    return ''

def generateCraftingMats(targetRank, craftingMatTypeWeights=''):
    return ''

def generateCondensedMagic(targetRank, magicItemsTypeWeights=''):
    return ''

def numericalTargetRankConversion(targetRank):
    rankStringToNumberKey = {'lesser':1, 'iron':2, 'bronze':3, 'silver':4, 'gold':5, 'diamond':6}
    return rankStringToNumberKey.get(targetRank.strip().lower() )

def lootTarget(targetRank, targetMagicLevel, typeWeights, lootables='', isMonster=False, looterRank=0, lootMultiplier=1):
    resultString = "{"
    resultString += generateCoinsAndCores(targetRank, lootMultiplier)

    targetRank = numericalTargetRankConversion(targetRank)
    if looterRank == 0:
        looterRank = targetRank
    
    lootedMagicLevelCost = {"coinsAndCores" : 15, "potion": 50, "craftingMat": 15, "healingItem": 10, "condensedMagic": 75, "equipmentPiece": 100   }
    coinsAndCoresCostAdjustment, allOtherCategoriesCostAdjustment = pow(5, (max(0, targetRank - 2) ) ), pow(5, (max(0, targetRank - 3) ) )

    currentMagicLevel = targetMagicLevel - lootedMagicLevelCost.get('coinsAndCores') * coinsAndCoresCostAdjustment
    itemCategoryNames = ['potion', 'craftingMat', 'healingItem', 'condensedMagic', 'equipmentPiece']
    numLootedSoFar = 1
    while currentMagicLevel > 0:
        itemsThatCouldBeLootedNext = itemCategoryNames.copy()
        nextLootItemProbabilityWeights, nextLootItemProbailities = [], []
        for item in itemsThatCouldBeLootedNext:
            if lootedMagicLevelCost.get(item) > currentMagicLevel:
                itemsThatCouldBeLootedNext.remove(item)
        if itemsThatCouldBeLootedNext.count('healingItem') == 0:
            itemsThatCouldBeLootedNext.append('healingItem')
        convertItemNameToWeigthtsIndex, itemWeights = {'potion':4, 'craftingMat':0, 'healingItem':3, 'condensedMagic':1, 'equipmentPiece':2}, []
        # for item in itemsThatCouldBeLootedNext:


        




    return resultString + '}'
    

