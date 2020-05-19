n = int(input("Enter the no. of houses: "))
list1 = list(map(int, input("enter the values in houses separated by spaces: ").split()))
list2 = list1[::2]
list3 = list1[1::2]
value = max(sum(list2), sum(list3))
print("Maximum stolen value is: " + str(value))
