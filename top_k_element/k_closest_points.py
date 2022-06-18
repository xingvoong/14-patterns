
def kClosest(points, k):

    def getDistance(x, y):
        import math
        return x**2 + y**2

    import heapq
    heap = []
    for i in range(k):
       d = getDistance(points[i][0], points[i][1])
       toAdd = [-d, points[i]]

    heapq.heapify(heap)
    toReturn = []

    # use a max heap so I can remove the max element
    for i in range(len(points)):

        d = getDistance(points[i][0], points[i][1])
        toAdd = [-d, points[i]]

        heapq.heappush(heap, toAdd)
        if len(heap) > k:
            heapq.heappop(heap)


    for h in heap:
        toReturn.append(h[1])

    return toReturn


print(kClosest([[1,3],[-2,2]], 1))
print(kClosest([[3,3],[5,-1],[-2,4]], 2))

'''
time:
space:

'''