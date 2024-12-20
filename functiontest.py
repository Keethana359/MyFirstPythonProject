
# def find_index(lst, n):
#     return lst.index(n)
#
# index = find_index([5,6,7,8],8)
# # print(index)

# using odd number !=0 and even number ==0
#
#x=[1,2,3,4,5,6,7,8,9,100,300,500,1000,2000]
x=range(0,1000)
for num in x:
    if num%2!=0:
     print(num)

# using odd number and even number separate
x=range(0,1000)
numbers_even=[]
numbers_odd=[]
for num in x:
    if num%2==0:
        numbers_even.append(num)
    else:
        numbers_odd.append(num)
print(numbers_odd)
print(numbers_even)

#
# # using append 5 user inpuuted number
# my_list=[]
# x1=int(input('enter the number1'))
# my_list.append(x1)
# print(my_list)
# x2=int(input('enter the number2'))
# my_list.append(x2)
# print(my_list)
# x3=int(input('enter the number3'))
# my_list.append(x3)
# print(my_list)
# x4=int(input('enter the number4'))
# my_list.append(x4)
# print(my_list)
# x5=int(input('enter the number5'))
# my_list.append(x5)
# print(my_list)


set=set()
print(type(set))

x=[1,2,3,4,5,6,7,8,9,10]
print(x[8:2:-3])

# While Loop: Count the digits in a user-inputted number.
numbers=int(input('enter the number'))
count=0
while numbers!=0:
    # // number= number/10
    numbers=numbers//10
    # print(numbers)
    count=count+1
print(count)