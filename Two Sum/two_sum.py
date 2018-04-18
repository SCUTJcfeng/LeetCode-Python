def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # for i in range(0, len(nums) - 1):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    # return []

    # for i in range(len(nums)):
    #     if target - nums[i] in nums:
    #         j = nums.index(target - nums[i])
    #         if i != j:
    #             return [i, nums.index(target - nums[i])]
    # return [0, 0]

    d = {}
    for i in range(len(nums)):
        if nums[i] not in d:
            d[target - nums[i]] = i
        else:
            return [d[nums[i]], i]
    return [-1, -1]

nums = [3, 7, 11, 2]
target = 9

print(twoSum(nums, target))