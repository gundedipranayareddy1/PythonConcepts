"""
Problem Statement:
Given a list/array of integers, arrange the list in descending order according to repetition
frequency of item.
In case where many integers have same repetition frequency, then put the smaller
number first.
Sample Input 1[1,4,5,6,6,5,3,5,1,6,4,6]
Sample Output 1[6,6,6,6,5,5,5,1,1,4,4,3]"""

from collections import Counter, OrderedDict

"""
author pranaya
func: This function will take input as list and give 
        output in the descending order of occurences of keys and 
            in case of same frequency of occurences for more than one key,
                the smallest keey will be appeared first followed by next
param:my_list input list
return: required format of elements
"""


def get_list(input):
    result = Counter(input)
    return result


my_list = [1,4,5,6,6,5,3,5,1,6,4,6]
output=get_list(my_list)
print(output)












