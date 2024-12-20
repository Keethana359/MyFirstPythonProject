s={10,20,30,40}
# this all method is add
s.add(50)
print(s)
l=['A','B','C']
s.update(l)
print(s)
s1=s.copy()
print(s1)
print(s)
s1.add(100)
print(s1)
# remove value method
# pop()
s.pop()
# random value remove
print(s)
s.remove(10)
# particular value remove
print(s)
# s.remove(70)
# #  getting error
# print(s)
s.discard(70)
print(s)
s.clear()
print(s)



# union()
# intersection()
# difference()
# synmetric difference()



# union() union value only taken
s={40,10,20,30}
s1={100,300,40,10,1,50}
print(s.union(s1))

s={10,20,30,40}
s1={100,400,40,200,600,500}
print(s.union(s1))

print(s.intersection(s1))


# using set is a subset of another set

a={1,2,3}
b={1,2,3,4,5}

is_subset=a.issubset(b)
print(is_subset)

is_subset_reverse = b.issubset(a)
print(is_subset_reverse)