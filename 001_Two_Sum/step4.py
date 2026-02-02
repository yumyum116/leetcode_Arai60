# !/usr/bin/env python3

class Solution:
	def twoSum(self, nums: list[int], target: int) -> list[int]:
		num_to_index = {}

		for i in range(len(nums)):
			complement = target - nums[i]
			if complement in num_to_index:
				return [num_to_index[complement], i]
			num_to_index[nums[i]] = i

		return []
