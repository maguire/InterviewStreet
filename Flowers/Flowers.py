"""
You and your K-1 friends want to buy N flowers. Flower number i has host ci. Unfortunately the seller does not like a customer to buy a lot of flowers, so he tries to change the price of flowers for customer who had bought flowers before. More precisely if a customer has already bought x flowers, he should pay (x+1)*ci dollars to buy flower number i.
You and your K-1 firends want to buy all N flowers in such a way that you spend the as few money as possible.

Input:

The first line of input contains two integers N and K.
next line contains N positive integers c1,c2,...,cN respectively.

Output:

Print the minimum amount of money you (and your friends) have to pay in order to buy all n flowers.

Sample onput :

3 3
2 5 6

Sample output :

13
"""
import sys

class Person :
    def __init__(self):
        self.flowersBought = 0

f = sys.stdin
firstLine = f.readline().split()
numFlowers = int(firstLine[0])
numPeople = int(firstLine[1])
flowers = f.readline().split()
flowers = [int(x) for x in flowers]
flowers.sort(reverse=True)

people = [Person() for x in range(numPeople)]

totalCost = 0
x = 0
while x < numFlowers :
    friend = people.pop(0)
    totalCost +=  (friend.flowersBought + 1) * flowers[x]
    friend.flowersBought += 1
    people.append(friend)
    x += 1

print totalCost 
