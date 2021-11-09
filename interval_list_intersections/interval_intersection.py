"""
Interval list intersections
Problem: https://leetcode.com/problems/interval-list-intersections/
Solution: https://leetcode.com/problems/merge-intervals/


You are given two lists of closed intervals, firstList and secondList, where firstList[i]= [start i, end i] and secondList[j] = [start j, end j].  Each list of intervals is pairwise disjoint and in sorted order.

Return the intersecion of htse 2 interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty
or represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3]

Example 1:
Input:
firstList = [[0,2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
Output:
[[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

Example 2:
Input:
firstList = [[1, 3], [5, 9]], secondList = []
Output: []

Example 3:
Input:
firstList = []
secondList = [[4, 8], [10, 12]]
Output: []

Example 4:
Input:
firstList = [[1, 7]]
secondList = [[3, 10]]
Output: [[3, 7]]

- 0 <= firstList.length, secondList.length <= 1000
- firstList.length + secondList.length >= 1
- 0 <= start i < end i <= 10^9
- end i < start i + 1
- 0 <= start j < end j <= 10^9
- end j < start j + 1

I: 2 lists of list, 2D array with different intervals
O: a list of list, intersection of these two intervals
C:
E:

Algo
+ main point:
- compare the "start of list 1" with "end of list 2"
- compare the "start of list 2" with "end of list 1"
=> compare the "start of one list" with "end of other list"
- have 2 pointers that point to the ending bound of 2 intervals in the 2 list
- compute the interval first, and check whether that interval is an intersection
- move the pointer foward when an interval has a bigger endding bound.

"""


def intervalIntersection(A, B):
    ans = []
    # 2 pointers
    # i is pointer for A
    # j is pointer for B
    i = j = 0

    # iterate through 2 lists at the same time
    while i < len(A) and j < len(B):
        # Let's check if A[i] intersects B[j]
        # start - the startpoint of the intersection
        # end - the endpoint of the intersection
        # computer the interval first
        start = max(A[i][0], B[j][0])
        end = min(A[i][1], B[j][1])
        # check if that interval is an intersection
        if start <= end:
            ans.append([start, end])

        # remove the interval with smaller ending bound
        # keep the one with bigger ending bound
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1

    return ans


def test():
    As = [[[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 3], [5, 9]], [], [[1, 7]]]
    Bs = [[[1, 5], [8, 12], [15, 24], [25, 26]], [], [[4, 8], [10, 12]], [[3, 10]]]
    expected = [
        [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
        [],
        [],
        [[3, 7]],
    ]
    count = 0
    for i in range(len(As)):
        actual = intervalIntersection(As[i], Bs[i])
        if actual != expected[i]:
            print("Wrong at input: {count}").format(count=count)
            temp = expected[i]
            print("Expected: {temp} but got {actual}").format(temp=temp, actual=actual)
            return
        count += 1

    print("Passed test")


test()


"""
Complexity Analysis
runtime: O(N) + O(N), to iterate through 2 list
=> O(N)
space: O(N) or O(1) for return result depends on
whether we count the space for return result
"""
