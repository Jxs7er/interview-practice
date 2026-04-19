# Add Two Numbers

## Problem

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two `numbers` and return the sum as a `linked list`.

### Example
Input:
l1 = [2,4,3], l2 = [5,6,4]

Output:
[7,0,8]

Explanation:
342 + 465 = 807.

---

## Approach
This solution simulates manual addition of two numbers represented as linked lists.

For each node:

- extract values from both lists (or 0 if null)
- add them with carry
- compute new digit and updated carry
- build the result list using a dummy head node

---

## Complexity
- Time: O(max(n, m))
- Space: O(max(n, m))
---

## Solution
See `solution.py`

## Link
```bash
https://leetcode.com/problems/add-two-numbers/submissions/1982359651
```