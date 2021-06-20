"""count the no. of strings where the length of the string is 2 or more and first
and last digit of the string are same"""
def count(list):
    ctr=0
    for x in list:
        if len(x) > 1 and x[0] == x[-1]:
            ctr=ctr+1
    return ctr

print(count(["abc","aba","anaconda","121","1221"]))