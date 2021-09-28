def max_subarray(numbers):
  best_sum = numbers[0]
  current_sum = numbers[0]
  for i in range(1, len(numbers)):
    current_sum = max(numbers[i], current_sum + numbers[i])
    best_sum = max(best_sum, current_sum)
  return best_sum

def test():
  input = [[-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8]]
  expected = [6, 1, 23]
  for i in range(len(input)):
    actual = max_subarray(input[i])
    if (actual != expected[i]):
      print('Wrong at input: {i}').format(i = i)
      temp = expected[i]
      print('Expected: {temp} but got {actual}').format(temp=temp,actual=actual)
      return

  print('Passed test')

test()