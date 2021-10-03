def threeSum(nums):
  res, dups = set(), set()
  seen = {}

  for i, val1 in enumerate(nums):
    if val1 not in dups:
      dups.add(val1)
      for j, val2 in enumerate(nums[i+1:]):
        complement = -(val1+val2)
        if complement in seen and seen[complement] == i:
          res.add(tuple(sorted((val1, val2, complement))))

        seen[val2] = i

  return list(res)

print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([]))
print(threeSum([0]))

'''
time: O(n^2).  we have outer and inner loops, each going through n elements
While the asymptotic complexity is the same, this algorithm is noticeably slower than the previous approach.  Lookups in a hashset, through requiring a constant time, are expensive compared to the direct memeory access

space: O(n) for the hashset/hashmap
For the purpose of complexity analysis, we ignore the memory required
for the output.
'''
