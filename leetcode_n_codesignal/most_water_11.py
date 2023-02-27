# 11. Container With Most Water
# Given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i])
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# link: https://leetcode.com/problems/container-with-most-water/
def maxArea(height: List[int]) -> int:
    l, r, ar = 0, len(height) - 1, 0
    while l < r:
        ar = max(ar, (r - l) * min(height[l], height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return ar
