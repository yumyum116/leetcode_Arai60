# !/usr/bin/env python3

class Solution:
	def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
		numbers = set(nums1)
		result = []

		for num in nums2:
			if num in numbers:
				result.append(num)
				numbers.remove(num)

		return result
