# Two Sum

## Problem
Given an array of integers `nums` and an integer `target`,
return indices of the two numbers such that they add up to target.

### Example
Input:
nums = [2,7,11,15]
target = 9

Output:
[0,1]

---

## Approach
This solution uses a Hash Map to store previously visited numbers
and their indices.

For each number:
- calculate the complement
- check if it already exists
- return indices if found

---

## Complexity
- Time: O(n)
- Space: O(n)

---

## Solution
See `solution.js`

## Link
[LeetCode .js](https://leetcode.com/problems/two-sum/submissions/1982369140)
[LeetCode .java](https://leetcode.com/problems/two-sum/submissions/1982368810)