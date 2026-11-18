# # # # Second Maximum in an Array: Given an array of integers, 
# # # # find the second-largest distinct element. If it does not exist, print -1.
# # # lst = [10, 100, 20, 80, 70, 60]
# # # a = lst[0]
# # # b = lst[-1]
# # # for i in range(len(lst)):
# # #     if a < lst[i]:
# # #         a = lst[i]
# # # for j in range(len(lst)):
# # #     if a == lst[i]:
# # #         pass
# # #     elif b < lst[i]:
# # #         b = lst[i]
# # # print("2nd Maximum", b)
# # lst = [-9999,-67,-69,-80,-99999999,-19,0, 1, 2,-999]
# # a=lst[0]
# # for i in range(len(lst)):
# #     if  lst[i] > a and lst[i] < 0:
# #         a = lst[i]
# # print('minimum neg', a)

# # 12. Filter Even Numbers: Given an array of integers, print all the even elements in their original order.
# # lst = [1,2,3,4,5,6,7,8,9,10]
# # even = []
# # for i in range(len(lst)):
# #     if lst[i]%2 == 0:
# #         even.append(lst[i])
# # print(even)

# # 13. Maximum Negative Number: Given an array of integers, 
# # find the negative number closest to zero. If there are no negative numbers, print -1.
# # lst = [1,2,10,-90,-76,-100,-3,-2, 100, -11]
# # a = float('-inf')
# # for i in range(len(lst)):
# #     if lst[i] > a and lst[i] < 0:
# #         a = lst[i]
# # print("Maximum", a)


# # def call_names(lst, s):
# #     for i in range(len(lst)):
# #         if lst[i] == s:
# #             return True
# #     return -1        
# # lst =['vijay', 'kumar', 'kamal', 'ajith', 'vasanth']
# # s = 'kumar'
# # print(call_names(lst, s))

# # Count Vowels: Given a string, count the total number of vowels (a, e, i, o, u) in it, ignoring case.
# vowels = ['a', 'e', 'i', 'o', 'u']
# s = input().lower()
# count = 0
# for i in range(len(s)):
#     for j in range(len(vowels)):
#         if s[i] == vowels[j]:
#             count += 1
# print(count)    


# Binary Search: Given an array of positive integers sorted in ascending order and a target element, 
# implement the binary search algorithm to find the index of the target. If the target is not present, print -1.

# lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# target = 100
# start = 0
# end = len(lst) - 1
# if target in lst:
#     while True:
#         mid = (start + end) // 2
#         if lst[mid] == target:
#             print(mid)
#             break
#         elif lst[mid] > target:
#             end -= 1
#             start = mid
#         elif lst[mid] < target:
#             end = mid
#             start += 1
# else:
#     print(-1)

# Count Maximum Occurrences: Given an array of integers, 
# find the maximum element and count how many times it occurs.

lst = [10,20,30,405,163, 198]
lar = lst[0]
for i in range(len(lst)):
    if 