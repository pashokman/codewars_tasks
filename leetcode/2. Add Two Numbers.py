"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1 = [], l2 = []):
        l1.reverse()
        l2.reverse()

        new_l1 = [str(i) for i in l1]
        new_l2 = [str(i) for i in l2]

        sum = int(''.join(new_l1)) + int(''.join(new_l2))

        res_list = []
        for i in str(sum):
            res_list.append(int(i))

        res_list.reverse()
            
        return res_list


obj = Solution()

print(obj.addTwoNumbers([2,4,3], [5,6,4]) == [7, 0, 8])

print(obj.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]) == [8,9,9,9,0,0,0,1])
