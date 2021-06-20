'''Remove duplicate from the list'''

a=[10,20,30,20,10,50,60,40,80,50,40]
uniq_list=[]
dup_list=set()
for x in a:
    if x not in dup_list:
        uniq_list.append(x)
        dup_list.add(x)

print(dup_list)