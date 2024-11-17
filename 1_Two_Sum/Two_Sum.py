input = [3,2,4]
target = 6

def twoSum(nums, target):
    solution = []

    for i in range (0, len(nums)):
        if (target-nums[i]) in nums[i+1:]:
            solution.append(i)
            solution.append(nums[i+1:].index(target-nums[i])+i+1)
            break
    return solution

print(twoSum(input, target))