# !/usr/bin/env python3

## pattern 1

class Solution:
	def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
		result = []

		if len(nums1) < len(nums2):
			nums1_set = set(nums1)
			nums2_to_index = {i:value for i, value in enumerate(nums2)}
			for i in nums2_to_index:
				if nums2_to_index[i] in nums1_set and not nums2_to_index[i] in result:
					result.append(nums2_to_index[i])
		elif len(nums1) >= len(nums2):
			nums2_set = set(nums2)
			nums1_to_index = {i:value for i, value in enumerate(nums1)}
			for i in nums1_to_index:
				if nums1_to_index[i] in nums2_set and not nums1_to_index[i] in result:
					result.append(nums1_to_index[i])

		return result

## pattern 2
class Solution:
	def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
		return list(set(nums1) & set(nums2))
