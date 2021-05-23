"""
Problem Statement:
Given an array containing unsorted positive or negative integers with repeated
    values, you must arrange the array in such a way that all non-zeroes should be on the left-
hand side of an array, and all zeroes should be on the right side of the array. Order of non-
zero elements does not matter. You are not allowed to use any sorting approach.
Expect time complexity – O(n)
Sample Input:1, 2, -4, 0, -1, 0, 3, 7, 0, 5, 0, 1, -1, 0
Sample Output1, 2, -4, -1, -1, 1, 3, 7, 5, 0, 0, 0, 0, 0"""


"""
author pranaya
func: This function will take input as list and give 
        output such that all integers(non-zeroes) are on the left side of list order not being considered
         and zeroes are on the right of the list
param:my_list input list
return: required format of ordered list
"""


def get_list(input):
    filtered_list = []
    filtered_list_for_zeroes = []
    for i in input:
        if i != 0:
            filtered_list.append(i)
        else:
            filtered_list_for_zeroes.append(i)
    return filtered_list+filtered_list_for_zeroes


my_list = [1, 2, -4, 0, -1, 0, 3, 7, 0, 5, 0, 1, -1, 0]
output = get_list(my_list)
print(output)


