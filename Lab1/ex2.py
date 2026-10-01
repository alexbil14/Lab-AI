list = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5]
posList = []
negList = []

for nr in list:
    if(nr >= 0):
        posList.append(nr)
    else:
        negList.append(nr)

print("Positive numbers from the list:")
print(posList)
print("\n")

print("Negative numbers from the list:")
print(negList)