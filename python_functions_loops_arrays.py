# Write a function that takes in an array of numbers and returns an array with all numbers multiplied by 3.
# testArr1 = [3, 9, 15, 4, 10]
# newArray = []
# def numx3(array):
#     for num in array:
#         newArray.append(num*3)
#     print(newArray)
# numx3(testArr1)
# Write a function that takes in an array of numbers and returns a new array with only odd numbers.
# testArr2 = [0, 2, -7, 3, 5, 8, 10, 13]
# oddNums = []
# def odds(array):
#     for num in array:
#         if num % 2 != 0:
#             oddNums.append(num)
#     print(oddNums)
# odds(testArr2)
# Write a function that takes in an array of numbers and letters and returns a string with only the letters. HINT: use the typeof method.
# comboArr = [
#   7,
#   "n",
#   True,
#   "i",
#   "c",
#   10,
#   "e",
#   -388,
#   "w",
#   3,
#   "o",
#   0,
#   "r",
#   False,
#   "k"
# ]
# strArray = []
# def to_string(list):
#        print("".join([elm for elm in list if isinstance(elm,str)]))
# to_string(comboArr)
# Create a function that takes in an array of numbers and returns the sum.
# addThese1 = [1, 2, 3, 4]
# # // output: 10
# addThese2 = []
# # // output: 0
# def sumList(list):
#     print(sum(list))

# sumList(addThese1)
# sumList(addThese2)
# Create a function that takes in an array of numbers and returns the index of the largest number.
# indexHighestNumber = [1, 4, 2, 3]
# # output: 1
# def maxVal(list):
#     print(max(list))
# maxVal(indexHighestNumber)
# Create a function that takes in two arrays and returns one array with no duplicate values.
# arr1 = [3, 7, 10, 5, 4, 3, 3]
# arr2 = [7, 8, 2, 3, 1, 5, 4]
# # // output: [3, 7, 10, 5, 4, 8, 2, 1]
# newList=[]
# def conCatList(list1, list2):
#     for num in list1:
#         for x in list2:
#             if num not in newList:
#                 newList.append(num)
#             if x not in newList:
#                 newList.append(x)
#     print(newList)
# conCatList(arr1, arr2)

# Create a function that takes in two numbers as arguments and returns an array the length of the first number filled with the second number.
# arrayLength = 6
# arrayValue = 0
# # output: [0, 0, 0, 0, 0, 0]
# arrayLength1 = 4
# arrayValue1 = 11
# # output: [11, 11, 11, 11]

# def create_list(num1,num2):
#     newlist = [num2]*num1
#     print(newlist)
# create_list(arrayLength,arrayValue)
# create_list(arrayLength1,arrayValue1)

# Create a function that takes a number as an argument. Add up all the numbers from 1 to the number you passed to the function.
# addUp1 = 4
# # // 1 + 2 + 3 + 4 = 10
# # // output: 10

# addUp2 = 10
# # // 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
# # // output: 55

# addUp3 = 600
# # // output: 180300

# def sumOf(num):
#     nums = list(range(1,num + 1))
#     print(sum(nums))
# sumOf(addUp1)
# sumOf(addUp2)
# sumOf(addUp3)