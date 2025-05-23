import sys
import os
import logging
import time
import datetime
from src.data.model.unsplash_data import UnsplashPhoto
from src.data.remote.json_helper import parse_json
from src.data.remote.api_requests import *
from src.utils.log_helper import Log
from collections import defaultdict, Counter, deque
import heapq
import math
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import DEBUG, API_URL, API_PHOTOS

# print(f"sys.path: {sys.path}")
print(f"{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}")

filename = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
# logger = logging.getLogger('test')
# logger.setLevel(logging.DEBUG)
# logging.Formatter.default_msec_format = '%s.%03d'

# # file log
# file_handler = logging.FileHandler(f'{filename}.log', mode='w')
# formatter = logging.Formatter('%(asctime)s | %(filename)s | %(levelname)s | [%(funcName)s() - %(lineno)d]: %(message)s')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# # console log
# console_handler = logging.StreamHandler()
# console_formatter = logging.Formatter('%(asctime)s | %(filename)s | %(levelname)s |[%(funcName)s() - %(lineno)d]: %(message)s') # Include filename and name
# console_handler.setFormatter(console_formatter)
# logger.addHandler(console_handler)

class MyClass:
    def my_method(self):
        Log.d(__name__, 'This is a debug message.')
        Log.i(__name__,'This is an info message.')
        Log.w(__name__,'This is a warning message.')
        Log.e(__name__,'This is an error message.')
        Log.c(__name__, 'This is a critical message.')

def main(*args):
    print("Debug mode:", DEBUG)
    print("API URL:", API_URL)
    print("API PHOTOS:", API_PHOTOS)
    return
    Log.initialize(logging.DEBUG)
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("SDET interview questions")
    search_box.send_keys(Keys.RETURN)

    assert "SDET" in driver.title
    input("Press Enter to close the browser and exit...")
    # driver.quit()
    try:
        photos = get_photos(per_page=10)
        print(f"1th photo: {photos[0]}")

        # 記錄日誌訊息
        Log.d(__name__, 'This is a debug message.')
        Log.i(__name__,'This is an info message.')
        Log.w(__name__,'This is a warning message.')
        Log.e(__name__,'This is an error message.')
        Log.c(__name__, 'This is a critical message.')
        my_object = MyClass()
        my_object.my_method()

    except (TypeError, ValueError) as e:
        print(f"Error parsing JSON: {e}")

    # test = "python3 test"
    # print(f'{test}')
    # charIndex = [-1] * 128
    # print(f"charIndex: {charIndex}")
    # s = "abc"
    # s = '#'.join(s)
    # print(f's: {s}')
    # dp = [0 for _ in range(len(s))]
    # print(f"dp: {dp}")

def longestPalindrome(s: str) -> str:
    """
    Finds the longest palindromic substring in the given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
    """

    if not s:
        return ""

    # Preprocess the string to handle even and odd length palindromes
    T = "#" + "#".join(s) + "#"
    P = [0] * len(T)
    center, right = 0, 0

    for i in range(1, len(T) - 1):
        mirror = 2 * center - i
        P[i] = min(right - i, P[mirror])

        # Attempt to expand palindrome centered at i
        while i - 1 - P[i] >= 0 and i + 1 + P[i] < len(T) and T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expands past right,
        # adjust center based on expanded palindrome.
        if i + P[i] > right:
            center, right = i, i + P[i]

    # Find the max expansion and return the corresponding substring
    max_len, cenete_index = max((val, i) for i, val in enumerate(P))
    start = (cenete_index - max_len) // 2
    return s[start: start + max_len]


def test(value):
    value = 10
    print(f"value: {value}")
    print(f"value id: {id(value)}")

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    ans = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
    print(f"ans: {ans}")
    return ans.values()

def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

def isPalindrome(s: str) -> bool:
    size = len(s)
    print(f"size {size}")
    start, end = 0, len(s) - 1
    # print(f"start end : {start}, {end}")
    while start < end:
        print(f"start end : {start}, {end}")
        if (not alphaNum(s[start]) and start < end):
            # print(f"s[start]: {s[start]}")
            start += 1
            continue

        if (not alphaNum(s[end]) and end > start):
            # print(f"s[end]: {s[end]}")
            end -=1
            continue
        print(f"test: {start}:{s[start]} {end}:{s[end]}")
        if (s[start].lower() != s[end].lower()):
            print("false")
            return False
        start +=1
        end -=1
    return True

def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    print(f"nums {nums}")
    result = set()
    for i in range(len(nums)):
        start, end = i + 1, len(nums)-1
        while start < end:
            sum = nums[i] + nums[start] + nums[end]
            print(f"nums[i], nums[start],nums[end]: {nums[i]}, {nums[start]}, {nums[end]}")
            if sum < 0:
                start += 1
            elif sum > 0:
                end -= 1
            else:
                temp = (nums[i], nums[start],nums[end])
                print(f"temp: {temp}")
                result.add(temp)
                start +=1
                end -=1

    print(f"result: {result}")
    return list(result)

def trap(height: list[int]) -> int:
    if not height:
        return 0

    print(f"height: {height}")
    start, end = 0, len(height)-1
    start_max, end_max = height[start], height[end]
    area = 0
    while start < end:
        if start_max < end_max:
            start += 1
            start_max = max(start_max, height[start])
            print(f"start_max: {start_max}, index: {start}")
            area += start_max - height[start]
        else:
            end -= 1
            end_max = max(end_max, height[end])
            print(f"end_max: {end_max}, index: {end}")
            area += end_max - height[end]
        print(f"area: {area}")
    return area

def productExceptSelf(nums: list[int]) -> list[int]:
        result = []
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        # [1, 1, 2, 8]
        pre = 1
        for i in range(1, len(nums)):
            pre = pre * nums[i-1]
            prefix[i] = pre
            print(f"pre: {pre}")
        print(f"prefix: {prefix}")

        # [48, 24, 6, 1]
        post = 1
        for i in range(len(nums)-2, -1, -1):
            post = post * nums[i+1]
            print(f"i: {i}")
            postfix[i] = post
        print(f"postfix: {postfix}")

        for i in range(len(nums)):
            product = prefix[i] * postfix[i]
            result.append(product)

        return result

def generateParenthesis(n: int) -> list[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                # print(f"s: {s}")
                res.append(s)
                return

            if left < n:
                print(f"left s: {s}")
                dfs(left + 1, right, s + '(')

            if right < left:
                print(f"right s: {s}")
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        print(f"res: {res}")
        return res

def lengthOfLongestSubstring(s: str) -> int:
    longest = 0
    sub = ""
    for c in s:
        print(f"sub {sub}")
        if c in sub:
            index = sub.index(c)
            remain = sub[index+1:]
            print(f"remain {remain}")
            sub = remain + c
        else:
            sub += c
        longest = max(longest, len(sub))
    return longest

def characterReplacement(s: str, k: int) -> int:
    count = {}
    max_freq = 0 # max freq
    start = 0
    for i in range(len(s)):
        count[s[i]] = 1+count.get(s[i],0)
        max_freq = max(max_freq, count[s[i]])

        if (i-start+1) - max_freq > k:
            count[s[start]] -= 1
            start += 1
    print(f"i: {i}")
    return i - start + 1

def topKFrequent(nums: list[int], k: int) -> list[int]:
        freq = {}
        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        sorteddict = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        print(f"sorteddict {sorteddict}")
        freq = dict(sorteddict)
        print(f"freq {freq}")
        print(f"type: {type(freq.values())}")
        result = list(freq.keys())[:k]
        return result

def evalRPN(tokens: list[str]) -> int:
    stack = []

    for token in tokens:
        if token == '+':
            a, b = stack.pop(), stack.pop()
            stack.append(a+b)
        elif token == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b-a)
        elif token == '*':
            a, b = stack.pop(), stack.pop()
            stack.append(a*b)
        elif token == '/':
            a, b = stack.pop(), stack.pop()
            print(f"{b}/{a}={int(b/a)}")
            stack.append(b/a)
        else:
            stack.append(int(token))
    return stack.pop()

def findDuplicate(nums: list[int]) -> int:
    print(f"nums {nums}")
    for num in nums:
        idx = abs(num)
        if nums[idx] < 0:
            return idx
        nums[idx] = -nums[idx]
        print(f"nums {nums}")
    return 0

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def heapify(array,size,i):
    largest=i
    left_children=2*i+1
    right_children=2*i+2

    if left_children<size and array[left_children]>array[largest]:
        largest=left_children
    if right_children<size and array[right_children]>array[largest]:
        largest=right_children

    if largest!=i:
        array[i],array[largest]=array[largest],array[i]
        heapify(array,size,largest)

def heapSort(array):
    # construct max heap:
    n=len(array)
    for i in range(n//2,-1,-1):
        heapify(array,n,i)

    # swap the root(index=0) to the end of the array and delete it
    for i in range(n-1,0,-1):
        array[i],array[0]=array[0],array[i]
        #heapify root element:
        heapify(array,i,0)

if __name__ == "__main__":
    print(f"{__name__}")
    main()
    # nums = [4,3,4,3,2]
    # # heapq.heappop(nums)
    # # print(f"heap_nums {nums}")
    # heapq.heapify(nums)
    # print(f"heap_nums {nums}")
    # print(f"heap_nums type {type(nums)}")
    # a = 5^3^5 #101 xor 011 = 110
    # print(f"a: {a}")
    # b = [[5,10],[6,8],[1,5],[2,3],[1,10]]
    # c = sorted(b)
    # b.sort()
    # print(f"b {b} and c {c}")

    # print(f"result {math.ceil(10//3)}")

    # team1 = Counter({'BlackTea': 3, 'GreenTea': 2, 'MilkTea': 1})
    # print(f"team1 {team1}")
    # print(f"most_common(2): {team1.most_common(2)}")
    # d = set(((1,0), (0, 1)))
    # print(f"d: {d}")
    # n = 10
    # size = 10
    # num = ~size
    # ans = size + num
    # print(f"size: {num}, {bin(num)}")
    # print(f"ans: {ans}")

    # a = -123
    # b = 123
    # print(f"{a % 10}")
    # print(f"{math.fmod(a, 10)}")
    # print(f"{b % 10}")
    # print(f"{b//10}")
    # print(f"{int(b//10)}")
    # print(f"{math.ceil(b/10)}")

    # a = 7
    # b =6
    # a &= 6
    # print(f"a {a}")

    # a = 120 & 0x7
    # print(f"a {a}")

    # a = 29
    # b = 13
    # a = a >> 1
    # bin(0)
    # print(f"a: {a}")
    # a &= b
    # print(f"a: {a}")

    # a = 310 & 38
    # a = math.sqrt(4)
    # a.bit_length()
    # b = float("inf")
    # print(f"{b}")
    # print(f"{a}")

    # a = ["1", "2", "3", "10", "7"]
    # b = ".".join(a)
    # print(f"b {b}")
    # a.sort()
    # print(f"a {a}")
    # d = deque()
    # d.popleft()

    # a = [1,0, 0]
    # b = 1 - a
    # print(f"b {b}")
    # a = {0}
    # print(f"a {type(a)}")

    # arr = [16,25,39,27,12,8,45,63]
    # pq = []
    # events = [[1,3,2],[4,5,2],[2,4,3]]
    # events.sort(key = lambda x:x[0])
    # for event in events:
    #     heapq.heappush(pq, (event[1], event[2]))ㄌ

    # print(f"pq {pq}")
    # tasks = ["A","A","A","B","B","B"]
    # counts = Counter(tasks)
    # task_heap = [-count for count in counts.values()]
    # print(f"task_heap {task_heap}")
    # heapq.heapify(task_heap)
    # print(f"task_heap {task_heap}")
    # gifts = [25,64,9,4,100]

    # print(f"gifts {gifts}")
    # for i in range(100):
    #     print(f"{i}th {chr(i)}")
    # a = 6* 3
    # print(f"{float(a)}")
