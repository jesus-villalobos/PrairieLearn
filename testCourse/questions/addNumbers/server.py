from functools import reduce

#Helper library
def generate_values(variant_id, keeps):
    """
    Description: a helper function that generating parameters' values
                 based on variant id and parameter constrains (keeps).
    Input:
        variant_id: id of the variant.
        keeps: a list of constrains for each parameter.
    Output:
        return a list that contains the value of each parameter.
    """
    result = []
    ranges = [len(k) for k in keeps]
    for i in range(len(keeps) - 1):
        ranges_product = reduce((lambda x, y: x * y), ranges[i+1:])
        result.append(keeps[i][(variant_id//ranges_product)%len(keeps[i])])
    result.append(keeps[-1][variant_id%ranges[-1]])
    return result

#After using our library
def generate(data):
    a, b = generate_values(data['variant_number'],[range(3,5), range(10,12)])
    # Put these two integers into data['params']
    data['params']['a'] = a
    data['params']['b'] = b
    # Compute the sum of these two integers
    c = a + b
    # Put the sum into data['correct_answers']
    data['correct_answers']['c'] = c
