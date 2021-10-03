var twoSum = function(i, nums, result) {
  var seen = new Set()
  var j = i + 1
  while (j < nums.length) {
    complement = - (nums[i] + nums[j])
    if (seen.has(complement)) {
      result.push([nums[i], nums[j], complement])
      while (j + 1 < nums.length && nums[j] == nums[j+1]) {
        j += 1
      }
    }
    seen.add(nums[i])
    j += 1
  }
  return result
}

var threeSum = function(nums) {
  var n = nums.length
  nums.sort((a, b) => a - b)
  var result = []

  for (var i = 0; i < n; i++) {
    if (nums[i] > 0) {
      break
    }
    if (i == 0 || nums[i] != nums[i-1]) {
      twoSum(i, nums, result)
    }
  }
  return result
}

console.log(threeSum([-1,0,1,2,-1,-4]))