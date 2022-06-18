from pyrsistent import l


def topKFrequent(nums, k):
    import heapq

    freq = {}
    heap = []
    toReturn = []

    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    # a heap with k element
    items = list(freq.items())

    for i in range(k):
        value = items[i][1]
        key = items[i][0]
        toAdd = [value, (key, value)]
        heap.append(toAdd)

    heapq.heapify(heap)

    for j in range(k, len(items)):
        value = items[j][1]
        key = items[j][0]
        toAdd = [value, (key, value)]
        heapq.heappush(heap, toAdd)
        if len(heap) > k:
            heapq.heappop(heap)

    for h in heap:
        toReturn.append(h[1][0])

    return toReturn


    #     heapq.heappush(heap, ())


print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))

'''
runtime: O(N) +
- create a hash map: O(N)
- make a list of items: O(N)
- loop through items: O(N)
- while loop through items, add item to heap: O(logK)
=> O(NlogK)

- get the result: O(logK)
=> O(NlogN)

space:
- hashmap: O(N)
- items: O(N)
- heap: O(N) if k = N
=> O(N)
'''