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

#LAB 2

print("---- LAB 2 ----")

#lab 2 ex 1: compute shopping list price

price = {"apples":10, "milk":12, "bread":5}
mylist = [("apples", 2), ("milk", 2)]

newlist = [price[item] * quantity for (item, quantity) in mylist]

print(f"1. {sum(newlist)}")

#lab 2 ex 2: extracting names in a set

friends = [("andrew", 10), ("george", 20), ("andrew", 5), ("ann", 10)]

friendsSet = set()

for friend in friends:
    friendsSet.add(friend[0])

print(f"2. {friendsSet}")

#lab 2 ex 3: input based console output: if n is even list from 0 to n else from 0 to n but each number squared

print("3. Give a number input: ")
number = int(input())
numberList = []

if(number % 2 == 0):
    numberList = [x for x in range(number + 1)]
else:
    numberList = [x*x for x in range(number + 1)]

print(numberList)

#lab 2 ex 4: create a dictionary

s_in = input()
num_in = int(input())
length = len(s_in)

dictionary = dict()

for i in range(num_in):
    dictionary[i] = s_in[i % length]

print(dictionary)


# lab 2 ex 5: we take a string and move each letter from it up one position in the alphabet

def shift_string(string: str):
    result = []
    for char in string:
        result.append(chr(ord(char) + 1)) # append the next character lexicographically

    return "".join(result)

str = input()
print(shift_string(str))

# lab 2 ex 6: take text from file1.txt and make them UPPERCASE and put them in file2.txt

with open("file1.txt", 'r') as file1:
    readData = file1.read()
    capitalized = readData.title()

    with open("file2.txt", 'a') as file2:
        file2.write(capitalized)