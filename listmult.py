def multiplyList(mylist):

        mult=1
        for x in mylist:
            mult= mult * x
        return mult

list=[10,12,20,18,9,51,25,3]
print(multiplyList(list))