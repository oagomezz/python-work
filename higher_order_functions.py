
###Map Method

# arr1 = [3, 9, 15, 4, 10]
# output: [30, 90, 150, 40, 100]

# def multiplyBy10(n):
#     return n * 10

# result = map(multiplyBy10, arr1)

arr2 = [2, 7, 3, 5, 8, 10, 13]
# output: [7, 3, 5, 13]
# Filter Method (Higher Order Function)
# def checkNumbers(num):
#     if num % 2 != 0:
#         return True
#     return False

# odd_num_iterator = filter(checkNumbers, arr2)

# odd_nums = list(odd_num_iterator)

# print(odd_nums)

comboArr = [7, "n", "i", "c", 10, "e", False, "w", 3, "o", "r", "k"]
# output: "nicework"

def isString(elm):
    if isinstance(elm,str) == True:
        return elm
    return False

str_iterator = filter(isString,comboArr)
print(str_iterator)
string_list = list(str_iterator)

print("".join(string_list))

