import json

with open('characterCodes.json','r') as f:
    characterCodes = json.load(f)

rem = [] 
asciiValues = []
binaryText = []

def searchCharacterCode(chars):
    global characterCodes
    global asciiValues
    for char in chars:
        for i in characterCodes:
            for k in characterCodes[i]:
                if char in k:
                    asciiValues.append(i)
    return asciiValues
def binary(x):
    global rem
    if(x<1):
        if(len(rem)<8):
            itemsRemaining = 8 - len(rem)
            i=0
            while(i<itemsRemaining):
                rem.append(0)
                i+=1
        rem = rem[::-1]        
        remString = [str(int) for int in rem]
        binaryCodes = ''.join(remString)
        return binaryCodes
    else:
        remainder = x % 2
        rem.append(remainder)
        x = int(x/2)
        return binary(x)

character = str(input("Enter a word to be converted: "))
characterCodes = searchCharacterCode(character)
for i in characterCodes:
    rem = []
    binaryText.append(binary(int(i)))
encodedText = '-'.join(binaryText)
print(encodedText)