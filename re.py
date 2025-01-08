# def calculator():
#     print("Select operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")

#     choice = input("Enter choice (1/2/3/4): ")

#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     if choice == '1':
#         print(f"{num1} + {num2} = {num1 + num2}")
#     elif choice == '2':
#         print(f"{num1} - {num2} = {num1 - num2}")
#     elif choice == '3':
#         print(f"{num1} * {num2} = {num1 * num2}")
#     elif choice == '4':
#         print(f"{num1} / {num2} = {num1 / num2}")
#     else:
#         print("Invalid Input")

# calculator()

# def lengthOfLongestSubstring(s: str) -> int:
#     char_set = set()
#     left = 0 
#     max_length = 0
    
#     for right in range(len(s)): 
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#     char_set.add(s[right])
#     max_length = max(max_length, right - left + 1)
#     return max_length

# def length_of_longest_substring(s):
#     char_index = {}
#     start = 0
#     max_length = 0

#     for i, char in enumerate(s):
#         if char in char_index and char_index[char] >= start:
#             start = char_index[char] + 1

#         char_index[char] = i
#         # Calculate the maximum length
#         max_length = max(max_length, i - start + 1)

#     return max_length
# s = "abcabcbb
# print("Length of the longest substring:", length_of_longest_substring(s))


# def two_sum(nums, target):
#     # Create a dictionary to store the complement and its index
#     complement_map = {}
    
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in complement_map:
#             return [complement_map[complement], i]
#         complement_map[num] = i

# # Example Usage
# nums = [2, 7, 11, 15]
# target = 9
# print(two_sum(nums, target))  # Output: [0, 1]

# def solve(str: str) -> int:
#     if len(str) == 0:
#         return 0
#     maxans = -1
#     for i in range(len(str)):  # outer loop for traversing the string
#         set = {}
#         # nested loop for getting different string starting with str[i]
#         for j in range(i, len(str)):
#             if str[j] in set:  # if element if found so mark it as ans and break from the loop
#                 maxans = max(maxans, j - i)
#                 break
#             set[str[j]] = 1
#     return maxans


# if _name_ == "_main_":
#     str = "takeUforward"
# #     print("The length of the longest substring without repeating characters is",solve(str))

# def longest_unique_substring(s):
#     start, max_length, char_index = 0, 0, {}
#     for end, char in enumerate(s):
#         if char in char_index and char_index[char] >= start:
#             start = char_index[char] + 1
#         char_index[char] = end
#         max_length = max(max_length, end - start + 1)
#     return max_length

# # Test the function
# input_string = "abcabcbb"
# print(longest_unique_substring(input_string))

# def twoSum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 return [i,j]
#     return[]
# nums = [2,7,11,15]
# target = 9
# print(twoSum(nums,target))



print('SKYLLX'[::-1])


