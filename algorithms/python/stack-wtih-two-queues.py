# https://practice.geeksforgeeks.org/problems/stack-using-two-queues/1

import atexit
import io
import sys

'''
    :param x: value to be inserted
    :return: None

    queue_1 = [] # first queue
    queue_2 = [] # second queue
'''


# Function to push an element into stack using two queues.
def push(x):
    global queue_1
    global queue_2

    while queue_1:
        queue_2.append(queue_1.pop(0))

    queue_1.append(x)

    while queue_2:
        queue_1.append(queue_2.pop(0))


# Function to pop an element from stack using two queues.
def pop():
    global queue_1
    global queue_2

    return queue_1.pop(0) if queue_1 else -1


# {
#  Driver Code Starts
# Initial Template for Python 3


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


queue_1 = []  # first queue
queue_2 = []  # second queue

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        i = 0
        while i < len(a):
            if a[i] == 1:
                push(a[i + 1])
                i += 1
            else:
                print(pop(), end=" ")
            i += 1

        # clear both the queues
        queue_1 = []
        queue_2 = []
        print()
# } Driver Code Ends
