"""
There is a queue for the self-checkout tills at the supermarket. 
Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. 
Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.

Important
Please look at the examples and clarifications below, to ensure you understand the task correctly :)

Examples
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
Clarifications
There is only ONE queue serving many tills, and
The order of the queue NEVER changes, and
The front person in the queue (i.e. the first element in the array/list) 
proceeds to a till as soon as it becomes free.
N.B. You should assume that all the test input will be valid, as specified above.

P.S. The situation in this kata can be likened to the more-computer-science-related 
idea of a thread pool, with relation to running multiple processes at the same time: 
https://en.wikipedia.org/wiki/Thread_pool
"""


def queue_time(customers, n):
    if len(customers) == 0:
        return 0
    elif n == 1:
        return sum(customers)
    elif len(customers) <= n:
        return max(customers)
    else:
        cashier_queues = [0] * n
        for j in customers:
            cashier_queues.sort()
            cashier_queues[0] += j
        return max(cashier_queues)


print(queue_time([], 1), 0)
print(queue_time([5], 1), 5)
print(queue_time([2], 5), 2)
print(queue_time([1, 2, 3, 4, 5], 1), 15)
print(queue_time([1, 2, 3, 4, 5], 100), 5)
print(queue_time([2, 2, 3, 3, 4, 4], 2), 9)
print(queue_time([50, 35, 28, 14, 28, 34, 1, 33, 1, 8, 36], 6), 65)
