""" Christian Gower / Lab#10 / 4.20.2023 """

#Generating Random Numbers and Random list
import random
def selection_sort(numbers):
    for i in range(len(numbers) - 1):
       index_smallest = i
       for j in range(i + 1, len(numbers)):
          if numbers[j] < numbers[index_smallest]:
            index_smallest = j

    #Swap numbers[i] and numbers[index_smallest]
       temp = numbers[i]
       numbers[i] = numbers[index_smallest]
       numbers[index_smallest] = temp
    return numbers

#Binary Search function
def binarySearch(array, key, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == key:
            return mid
        elif array[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#Sorted list
SortList = []
for j in range(30):
    i = random.randint(40, 100)
    SortList.append(i)
print('Random list:', SortList)
Sorted = selection_sort(SortList)
print('Sorted List:', Sorted)
key = int(input())

#Search for value
print('Search for value', str(key) +':')
high = len(Sorted) - 1
low = 0

index = binarySearch(Sorted, key, low, high)

if index != -1:
    print('The value', key, 'is present at the list location: ' + str(index))
else:
    print('The value', key, 'is not on the list')
