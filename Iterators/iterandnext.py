my_list=[1,2,3,4,5]
iter_list=iter(my_list)
print(next(iter_list))
print(iter_list.__next__())
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))
