# // Two Sum — Easy

# // Input:
# // nums = [2, 7, 11, 15]
# // target = 9

# // Output:
# // [0, 1]

# // Because 2 + 7 = 9.

# // Goal: O(n) time using a hash map.

from ctypes import Array

from zmq import has


def twosum(arr, sum):
    S1 = set({})

    for i in arr:
        if (sum - i) in S1:
            return (i, sum - i)
        else : S1.add(i)

    return None

print(twosum([2, 7, 11, 15], 9))

def anagram(str1, str2):
    hash = {}

    for i in str1:
        try:
            hash[i] = hash[i] + 1
        except KeyError:
            hash[i] = 1
    for i in str2:
        try:
            hash[i] = hash[i] - 1
        except KeyError:
            hash[i] = 1

    for v in hash.values():
        if v != 0:
            return "Not"
    return "Yes"

print(anagram("anagram", "anagram"))
print(anagram("car", "bikecar"))



def groupAnagram(strArr):

    hash  = {}

    for s in strArr:
        count = [0] * 26

        for i in s:
            index = ord(i) - ord('a')
            count[index] += 1

        key = "".join(map(lambda x: str(x), count))

        if(hash.get(key)):
            hash[key].append(s)
        else: hash[key] = [s]

    for i in hash.values():
        print(i)

groupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"])


def topKFrequent(arr, k):
    freq = {}

    for i in arr:
        try:
            freq[i] += 1
        except:
            freq[i] = 1

    bucket = [[] for i in range(len(arr) + 1)]

    for (key, count) in freq.items():
        bucket[count].append(key)

    result = []
    for i in bucket[::-1]:
        print(i)
        result.extend(i)
        if len(result) >= k:
            return result

print(topKFrequent([1, 1, 1, 2, 2, 3, 3], 2))