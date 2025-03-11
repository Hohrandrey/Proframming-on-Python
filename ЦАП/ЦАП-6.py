import math


def main(input_set):
    lambda_set = set(input_set)
    e_set = {elem for elem in lambda_set if -89 < elem <= 21}
    i_set = {elem for elem in lambda_set if elem <= -31 or elem >= 93}
    o_set = i_set.union(e_set)
    union_size = len(e_set.union(o_set))
    sum_pairs = sum(math.ceil(e / 2) + o for e in e_set for o in o_set)
    omega = union_size - sum_pairs
    return omega


print(main((-96, 33, -93, -89, -56, -23, 42, 9, -2)))
print(main([97, -95, 4, -55, 74, 75, -44, 88, 29, -33]))