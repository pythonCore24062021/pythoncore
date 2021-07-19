## list
#
# l1 = []
# l2 = [1, 2, 3, "test", [1, 2], (0, {"k": ["a", "b"]})]
# print(l2)
# print(l2[3])
# print(l2[4])
# print(l2[4][0])
# print(l2[5])
# print(l2[5][0], l2[5][1])
# print(l2[5][1]['k'], l2[5][1]['k'][1])
#
# l3 = list()
# print(l3)
# l3 = list("vdsjhfvsh")
# print(l3)
# # l3 = list(1)#err
# l4 = [1,2,3]
# l5 = ["a", "b", l4]
# print(l4)
# print(l5)
# l4.append(99)
# print(l4)
# print(l5)
# l5[2].append("test")
# print(l4)
# print(l5)
# l4 = l4[:]
# l4.append("test"*3)
# print(l4)
# print(l5)
#
# l4 = [1,2,3]
# l5 = ["a", "b", l4]
# del l4
# # print(l4)
# print(l5)

# l = [1,2,3]
# print(id(l), l)
# l = []
# print(id(l), l)
#
#
# l = [1,2,3]
# print(id(l), l)
# l.clear()
# print(id(l), l)
# import copy
#
# l = [1,2,3]
# l2 = [1,2,3, l]
# l3 = l2.copy()
# print(id(l), l)
# print(id(l2), l2, id(l2[3]))
# print(id(l3), l3, id(l3[3]))
# l.append("test")
# l4 = copy.deepcopy(l2)
# l.append("test")
# print(id(l), l)
# print(id(l2), l2, id(l2[3]))
# print(id(l3), l3, id(l3[3]))
# print(id(l4), l4, id(l4[3]))
# ll = l4
# print(ll, ll.count(1))
#
# l = [1,2,3,4, 1,2,3,4]
# ll = ["a", "b", 1,2,3,4]
# print(l)
# l.append(ll)
# print(l)
# l.extend(ll)
# l.insert(1, "test")
# print(l)
# print(l.pop())
# print(l)
# print(l.pop(1))
# print(l)
#
# l = [1,2,3,4, 1,2,3,400, "a"]
# def myS(element):
#     if type(element) == int:
#         return element
#     elif type(element) == str:
#         return ord(element)
# l.sort(key=myS)
# print(len(l))
# print(l)
#
# print(sum(l[:-2]))


# l = []
# for i in range(10):
#     l.append(i**2)
# print(l)
# l = [i**3 for i in range(10)]
# print(l)
# l = [i**3 for i in range(10) if i%2]
# print(l)
# l = [j*i for j in range(1, 11) for i in range(1,11) ]
# print(l)
#
# l = ["a", "b", "c", "d"]
# print(l)
# for i in range(len(l)):
#     if i%2 == 0:
#         print(l[i], end=" ")
# print()
# en = list(enumerate(l))
# print(en)
# for e in en:
#     if e[0] % 2 == 0:
#         print(e[1], end=" ")
# for i, v in en:
#     if i % 2 == 0:
#         print(v, end=" ")

# print([i for i in dir(list) if  not i[0] =="_"])
##tuple
# print([i for i in dir(tuple) if not i[0] == "_"])
# t1 = ()
# print(type(t1))
# t1 = (1, 2, 3)
# print(type(t1))
# t1 = (1,)
# print(type(t1))
# t1 = tuple()
# print(type(t1))
# t1 = tuple("sdgfvudsjh")
# print(type(t1), t1)
# print(list(t1))


# print([i for i in dir(dict) if not i[0] == "_"])
# d = {}
# print(d)
# d = {"k": 1, 33: 33, (1,2,3): "tuple"}
# # d = {"k": 1, 33: 33, [1,2,3]: "tuple"}#err
# print(d)
# d = dict()
# print(d)
# d = dict()
# print(d)
# d = {"k": 1, 33: 33, (1,2,3): "tuple", "dict": {1:2, 2:2}}
# print(d["k"])
# print(d.get("k"))
# print(d.get("kkk"))
# # print(d["kkk"])#err
# print(d.items())
# print(d.keys())
# print(d.values())
# print(d.pop("dict"))
# print(d.update({1:2, 2:2}))
# print(d)
#
# for key in d:
#     print(key, d[key])
# for key, val in d.items():
#     print(key, val)
#
# d2 = {1:2, 2:2}
# print(d.c)

print([i for i in dir(set) if not i[0] == "_"])
s = {}
print(type(s), s)
s = {1,2,3,4,12,2,1}
print(type(s), s)
s = set()
print(type(s), s)
s1 = {1,2,3}
s2 = {3,4,5}
print(s1.intersection(s2))
# print(s1.intersection_update(s2))
# print(s1, s2)
print(s1.difference(s2))
print(s1.issubset(s2))
print(s1.union(s2))

print([i for i in dir(frozenset) if not i[0] == "_"])

f = frozenset(s2)
f = f.intersection(s1)
print(type(f))
f = s1.intersection(f)
print(type(f))