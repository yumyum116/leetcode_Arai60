# !/usr/bin/env python3

class Solution:
	def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
		numbers = set(nums1)
		num_list = list(numbers)
		n = len(num_list)
		result = []

		for i in range(n):
			target = num_list[i]
			if target in nums2:
				result.append(target)

		return result
