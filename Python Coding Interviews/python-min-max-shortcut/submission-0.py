from typing import List


def disallow_negatives(num: int) -> int:
    value = max(0,num)
    return value


def max_difference(nums: List[int]) -> int:
    max_num = float('-inf')
    length = len(nums) - 1
    i = 0
    while i != length :
        new_num = nums[i+1] - nums[i]
        if new_num > max_num:
            max_num = new_num
        i= i + 1
    return max_num






# do not modify below this line
print(disallow_negatives(-2))
print(disallow_negatives(-1))
print(disallow_negatives(0))
print(disallow_negatives(1))
print(disallow_negatives(2))

print(max_difference([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_difference([1, 2, 3, 4, 5, 6, 8, 9]))
print(max_difference([10, 1, 3, 7]))
print(max_difference([2, 4, 7, 5, 7, 8, 4, 2]))
