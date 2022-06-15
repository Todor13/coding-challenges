# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1

class Solution:

    # Function to find the maximum number of meetings that can
    # be performed in a meeting room.
    def maximumMeetings(self, n, start, end):
        meetings = []
        total = 0
        for i in range(n):
            meetings.append([start[i], end[i]])

        meetings = sorted(meetings, key=lambda x: x[1])
        prev_end = -1
        for time in meetings:
            if time[0] > prev_end:
                total += 1
                prev_end = time[1]

        return total


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        start = list(map(int, input().strip().split()))
        end = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maximumMeetings(n, start, end))
# } Driver Code Ends
