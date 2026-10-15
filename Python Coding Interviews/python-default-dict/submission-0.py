from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    char = defaultdict(int)
    for character in s:
        char[character] += 1
    return char


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    number_dict = defaultdict(list)
    for num in nums:
        for n in num[1:]:
            number_dict[num[0]].append(n)
    return number_dict



# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
