# input = open('temp.txt', 'r')
# stuffToSort = []
# for x in range(300):
#     nextLine = input.read()
#     if nextLine == "": 
#         break
#     stuffToSort.append(nextLine.split('\n\n') )
# stuffToSort = stuffToSort[0]
output = open('tempOutput.txt', 'w')

armorTypes = ['armored coat', 'bastion plate armor', 'buckle armor', 'ceramic plate armor', 'coral armor', 'fortress plate armor', 'gi', 
              'half plate armor', 'lamellar breastplate armor', 'lattice armor', 'leaf weave armor', 'leather lamellar armor', 'quilted armor', 
              'scroll robes', 'wooden breastplate armor', 'armored cloak', "explorer's clothing", 'padded armor', 'studded leather armor', 
              'chain shirt armor', 'hide armor', 'scale mail armor', 'chain mail armor', 'breastplate armor', 'splint mail armor', 'half plate armor', 
              'full plate armor']
armorTypes.sort()

results = '['
for item in armorTypes:
    results += '"' + item + '", '
output.write(results[:-2] + ']')