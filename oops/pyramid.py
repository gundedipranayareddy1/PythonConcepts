# [1, 4, 5] [2, 4, 6]
# i - 1,2 = 1
# ii 4,4 =0
# 5,6 =1
# [4, 4], [1,2], [5,6]
list1=[1,4,5]
list2=[2,4,6]
difflist=[]
list3=[]

for i ,j in zip(list1,list2):
    diff=abs(i-j)
    difflist.append(diff)
    list3.append([i,j])

print(difflist)
print(list3)

#
# for i ,j in zip(list1,list2):
#     diff=abs(i-j)
#     if diff not in difflist:
#         difflist.append(diff)
#         list3.append([i,j])
#     else:
#         for list in list3:
#             if (i+j) < sum(list):
#                 list3.append([i,j])
#                 list3.append(list)
#             else:
#                 pass
#
#
#
#
#
#
# print(list3)
# print(difflist)

for diff in difflist:
    pass







