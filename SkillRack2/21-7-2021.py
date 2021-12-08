from fruit import Fruit

N = int(input())
fruits = []
for ctr in range(N):
    name, qunatity = input().split()
    fruit = Fruit(name, int(qunatity))
    fruits.append(fruit)

print(Fruit.count)
print(Fruit.totalQuantity)
X = int(input())
del fruits[X-1]
for fruit in fruits:
    print(fruit)
print(Fruit.count)
print(Fruit.totalQuantity)



'''
4
Apple 10
Orange 5
Mango 15
Banana 4
3

'''
