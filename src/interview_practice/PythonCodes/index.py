# # // Two Sum — Easy

# # // Input:
# # // nums = [2, 7, 11, 15]
# # // target = 9

# # // Output:
# # // [0, 1]

# # // Because 2 + 7 = 9.

# # // Goal: O(n) time using a hash map.

# from ctypes import Array

# from zmq import has


# def twosum(arr, sum):
#     S1 = set({})

#     for i in arr:
#         if (sum - i) in S1:
#             return (i, sum - i)
#         else : S1.add(i)

#     return None

# print(twosum([2, 7, 11, 15], 9))

# def anagram(str1, str2):
#     hash = {}

#     for i in str1:
#         try:
#             hash[i] = hash[i] + 1
#         except KeyError:
#             hash[i] = 1
#     for i in str2:
#         try:
#             hash[i] = hash[i] - 1
#         except KeyError:
#             hash[i] = 1

#     for v in hash.values():
#         if v != 0:
#             return "Not"
#     return "Yes"

# print(anagram("anagram", "anagram"))
# print(anagram("car", "bikecar"))



# def groupAnagram(strArr):

#     hash  = {}

#     for s in strArr:
#         count = [0] * 26

#         for i in s:
#             index = ord(i) - ord('a')
#             count[index] += 1

#         key = "".join(map(lambda x: str(x), count))

#         if(hash.get(key)):
#             hash[key].append(s)
#         else: hash[key] = [s]

#     for i in hash.values():
#         print(i)

# groupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"])


# def topKFrequent(arr, k):
#     freq = {}

#     for i in arr:
#         try:
#             freq[i] += 1
#         except:
#             freq[i] = 1

#     bucket = [[] for i in range(len(arr) + 1)]

#     for (key, count) in freq.items():
#         bucket[count].append(key)

#     result = []
#     for i in bucket[::-1]:
#         print(i)
#         result.extend(i)
#         if len(result) >= k:
#             return result

# print(topKFrequent([1, 1, 1, 2, 2, 3, 3], 2))




# def longestSeq(arr):
#     s1 = set(arr)

#     longest = 0

#     for i in s1:
#         if (i-1) not in s1:
#             curr = i
#             count = 1

#         while (curr+1) in s1:
#             curr +=1
#             count +=1

#         longest = max(longest, count)

#     return longest

# print(longestSeq([100,200,201,202,203, 1,2,3]))


# def mxpProfit(arr):
#     # Input:  [7, 1, 2, 5, 3, 6, 14]
#     minPrice = arr[0]
#     profit = 0

#     for i in arr:
#         if i < minPrice:
#             minPrice = i

#         tempProfit = i - minPrice

#         if tempProfit > profit: profit = tempProfit

#     return profit


# print(mxpProfit([7, 1, 5, 3, 6, 14]))


# from curses.ascii import isalnum


# def validaPalindrom(str1):
#     left = 0
#     right = len(str1) -1

#     while(left < right):
#         while(left < right and (not isalnum(str1[left]))):
#             left +=1
#         while(left < right and (not isalnum(str1[right]))):
#             right -=1

#         print(str1[left].lower() , str1[right].lower())

#         if(str1[left].lower() == str1[right].lower()):
#             left +=1
#             right -=1

#         else: return "NOT"

#     return "YES"

# print(validaPalindrom("A man, a plan, a canal: Panama"))


# def max2(arr):
#     m1 =0
#     m2 =0

#     for i in arr:
#         if i > m1:
#             m2 = m1
#             m1 = max(i, m1)
#         elif i > m2:
#             m2 = i
    

#     print(m1, m2)

# max2([20,21,32,23,36])

# def mostWaterContent(arr):
#     left = 0
#     right = len(arr) -1
    
#     area = 0

#     while(left < right):
#         temparea = (right - left) * min(arr[left], arr[right])

#         area = max(temparea, area)

#         if arr[left] > arr[right]:
#             right -= 1
#         else:
#             left += 1

#     print(area)

# mostWaterContent([1, 8, 6, 2, 5, 4, 8, 3, 7])
    

# def longestSubstring(str1):
#     left = 0
#     hash = {}
#     w = 0

#     for right in range(len(str1)):

#         char = str1[right]
#         try:
#             if hash[char] >= left:
#                 left = hash[char] + 1
#         except KeyError:
#             ""

#         hash[char] = right

#         w = max(w, right - left + 1)

#     return w

# print(longestSubstring("abcaabcd"))


def func():
    func()

func()