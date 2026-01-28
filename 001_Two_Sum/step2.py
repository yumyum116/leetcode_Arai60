# !/usr/bin/env python3

class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		numberMap = {}
		n = len(nums)

		for i in range(n):
			complement = target - nums[i]
			if complement in numberMap:
				return [numberMap[complement], i]
			numberMap[nums[i]] = i

		return []
