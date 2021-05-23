"""Given a list/array of integers, arrange the list in descending order according to repetition
frequency of item.
In case where many integers have same repetition frequency, then put the smaller
number first.
Sample Input 1[1,4,5,6,6,5,3,5,1,6,4,6]
Sample Output 1[6,6,6,6,5,5,5,1,1,4,4,3]"""
from collections import Counter

my_list_sorted_based_on_count=[]
filtered_list = []
final_sorted_list = []

def get_filtered_list(my_dict_sorted_based_on_count):
    print(my_dict_sorted_based_on_count.keys())
    print(my_dict_sorted_based_on_count.values())
    for key,value in my_dict_sorted_based_on_count.items():
        global filtered_list
        # print(key,value)
        if list(my_dict_sorted_based_on_count.values()).count(value) > 1:
            print(key,value)
            print("value",value)
            filtered_list.append({key:value})

        else:
            get_final_list(key,value)
    print(final_sorted_list)
    print(filtered_list)

def get_final_list(key,value):
    print("entered get_final list")

    global final_sorted_list

    for i in range(value):
        print("key",key)
        final_sorted_list.append(key)

def get_list(mylst):
    print(Counter(mylst))


my_list=[1,4,5,6,6,5,3,5,1,6,4,6,7]
# my_list_sorted=sorted(my_list, reverse=True)
# print(my_list_sorted)
# unique_my_list_sorted=sorted(set(my_list_sorted),reverse=True)
# print(unique_my_list_sorted)
# my_dict_sorted_based_on_count={i:my_list.count(i) for i in unique_my_list_sorted}
# print(my_dict_sorted_based_on_count)
# get_filtered_list(my_dict_sorted_based_on_count)
get_list(my_list)












