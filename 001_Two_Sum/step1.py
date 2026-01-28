# !/usr/bin/env python3

class Solution:
	def twoSum(self, nums, target):
		for i in range(len(nums) - 1, 0, -1):
			temp = target - nums[i]
			if temp in nums:
				position = nums.index(temp)
				if not position == i:
					return position, i
