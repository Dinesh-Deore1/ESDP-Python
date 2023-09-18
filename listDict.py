from collections import defaultdict,Counter

ls = [10, 20, 10, 20, 30, 20, 10, 10]
# d={}
# for i in ls:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)

d = defaultdict(int)
for x in ls:
    d[x]+=1
print(d)
print(Counter(ls))
