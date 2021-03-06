def knapsack(b, a):
    if b == 0 or len(a) == 0:
        return 0
    if len(a) == 1:
        if a[0][0] > b:
            return 0
        return a[0][1]
    if a[0][0] > b:
        return knapsack((b, a[1:]))
    return max(a[0][1] + knapsack(b - a[0][0], a[1:]), knapsack(b, a[1:]))
n =  int(input("Enter the number of items you want to enter: "))
a = []
for i in range(n):
    b = int(input("Enter the weight for item number " + str(i + 1) + ": "))
    c = int(input("Enter the value for item number " + str(i + 1) + ": "))
    a.append((b,c))
b = int(input("Enter the value of weight capacity: "))
print("The maximum value for the given weight value pair is ", knapsack(b, a))
