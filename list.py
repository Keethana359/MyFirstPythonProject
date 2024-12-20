# my_list=[100,20,30,40,500,600]
# for i in my_list:
#     if (i>500):
#         print("got vochers")
#         continue
#
#     print(i)
# emp_id=[101,102,103,104]
# print(type(emp_id))
# print(emp_id)
# list=list(input("enter the list"))
# print(list)
from operator import length_hint

# list does support to item assignment
x=[10,20,30]
# tuple does not support item assignment x[1]=50 it is not change
# x=(10,20,30)
print(type(x))
x[1]=50
print(x)


# x=eval(input("enter the list"))
# print(x)

# using append method
fruit=['apple','organe','kiwi']
print("original fruit:",fruit)
fruit.append('cherry')
print("update list:",fruit)

# using insert method
fruit=['apple','organe','kiwi']
print("original fruit:",fruit)
fruit.insert(2,  'strawberry')
print("update fruit:",fruit)

# using extend method
numbers=[1,3,5]
print("odd_number:",numbers)
even_number=[2,4,6]
numbers.extend(even_number)
print("update numbers:",numbers)

# change list
x=[100,200,300,400]
print("original list:",x)
x[1]=150
print("update list:",x)

# remove from list
x=[10,20,30,40,60,50]
x.remove(60)
print(x)

# length of list
phones=['iphone11','iphone13','iphone15']
del phones[1]
# del phones deleting entire list
# del phones[1:2] error  list does not support
print(phones)
print("total element:",len(phones))

lst=[1,2,3,4,5]
index=lst.index(3)
print(index)

x=[1,2,3,4,5,6,7,8,9]
print(x[1:2:2])

x=[1,2,3,4,5,6,7,8,9,10]
print(x[8:2:-3])


# using count method
x=('a',('a','b'),('a','b'),(3,5))
count=x.count(('a','b'))
print("count of ('a','b'):",count)
count=x.count((3,5))
print("count off (3,5):",count)

# using pop method
lang=['py','java','c++','c','.net']

print("when element is 0")
print("remove_element:",lang.pop())
print("update list:",lang)

print("/n when element is -1")
print("remove_element:",lang.pop(-1))
print("update list:",lang)

print("/n when element is -3")
print("remove_element:",lang.pop(-3))
print("update list:",lang)


my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)

my_list = [1, 2, 3]
my_list[1]=4
print(my_list)

for i in range(3, 10, 2):
    print(i)

my_list=[]
x1=int(input('enter the number1'))
my_list.append(x1)
print(my_list)



# List Manipulation: Reverse a list without using built-in functions
list=list(input('enter the number'))
reverse_list=[]
for i in range(len(list)-1,-1,-1):
        reverse_list.append(list[i])
print(reverse_list)

# def reverse_list(list):
#     reverse_list=[]
#     for i in range(len(list)-1,-1,-1):
#         reverse_list.append(list[i])
#     return reverse_list
#
# list1=list(input('enter the number'))
# print(reverse_list(list1))

# using reverse list with bulit in function
my_list=[1,2,3,4,5]
my_list.reverse()
print('reverse list:',my_list)
