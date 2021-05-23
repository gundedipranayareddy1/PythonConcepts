#instabase interview questions
class InfIter:
    """Infinite iterator to return all
        odd numbers"""
    def __init__(self,my_list):
        self.my_list=my_list

        self.num = 0
        #return self

    # def __iter__(self):
    #
    #     self.num = 0
    #     return self

    def __next__(self):
        num = self.my_list[self.num]
        self.num += 1
        return num
    def hasNext(self):
        if len(self.my_list)==self.num:
            return False
        else:
            return True
a=InfIter([3,4])
# ir=iter(a)
print(a.__next__())
print(a.hasNext())
print(a.__next__())
# print(ir.hasNext())