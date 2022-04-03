import random, copy
from functools import reduce
class Helper:
    def __init__(self, ranges):
        new_ranges = []
        for item in ranges:
            new_ranges.append(item[1] - item[0])
        self.ranges = new_ranges
    def generate_values(self, variant):
        result = []
        for i in range(len(self.ranges) - 1):
            ranges_product = reduce((lambda x, y: x * y), self.ranges[i+1:])
            if variant - ranges_product < 0:
                result.append(0)
            else:
                for j in range(1, self.ranges[i] + 1):
                    if variant %(ranges_product*self.ranges[i]) < j*ranges_product:
                        result.append(j - 1)
                        break
        result.append(variant % self.ranges[-1])
        return result


#Original Generate without using our library
# def generate(data):
#     # Sample two random integers between 5 and 10 (inclusive)
#     a = random.randint(5, 10)
#     b = random.randint(5, 10)
#     # Put these two integers into data['params']
#     data['params']['a'] = a
#     data['params']['b'] = b
#     # Compute the sum of these two integers
#     c = a + b
#     # Put the sum into data['correct_answers']
#     data['correct_answers']['c'] = c


#After using our library
def generate(data):
    helper_class = Helper([(0,5), (0,4)])
    variant_number = data['variant_number']
    a, b = helper_class.generate_values(variant_number)
    # Put these two integers into data['params']
    data['params']['a'] = a
    data['params']['b'] = b
    # Compute the sum of these two integers
    c = a + b
    # Put the sum into data['correct_answers']
    data['correct_answers']['c'] = c


#Before using helper library
# import random, copy

# def generate(data):

#     # Sample two random integers between 5 and 10 (inclusive)
#     a = random.randint(5, 10)
#     b = random.randint(5, 10)

#     # Put these two integers into data['params']
#     data['params']['a'] = a
#     data['params']['b'] = b

#     # Compute the sum of these two integers
#     c = a + b

#     # Put the sum into data['correct_answers']
#     data['correct_answers']['c'] = c
