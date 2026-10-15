print("--- LAB 1 ---")

#lab 1 ex 1: average of a list

list = [1, 2, 3, 4, 5] 

print(f"1. ", sum(list) / len(list))

#lab 1 ex 2: separating positive and negative elems in two separate lists

list = [-1, -2, -3, -4, -5, 1, 2, 3, 4, 5]
posList = []
negList = []

for nr in list:
    if(nr >= 0):
        posList.append(nr)
    else:
        negList.append(nr)

print("2. Positive numbers from the list:")
print(posList)
print("Negative numbers from the list:")
print(negList)

#lab 1 ex 3: sum of elements from 0 to len(list) - 2

list = [1, 2, 3, 4, 5]
sum = 0

for i in range(0, len(list) - 2):
    sum += list[i]

print(f"3. ", sum)

#lab 1 ex 4: show every even number from the list

list = [1, 2, 3, 4, 5]

print("4. ")

for i in range(len(list)):
    if i % 2 == 1:
        print(list[i])

#lab 1 ex 5: find the minimum element

list = [5, 4, 3, 2, 1]
min = 999

for nr in list:
    if nr < min:
        min = nr

print(f"5. ", min)