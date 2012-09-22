"""
Given N numbers , [N<=10^5] we need to count the total pairs of numbers that have a difference of K. [K>0 and K<1e9]

Input Format:
1st line contains N & K (integers).
2nd line contains N numbers of the set. All the N numbers are assured to be distinct.
Output Format:
One integer saying the no of pairs of numbers that have a diff K.

Sample Input #00:
5 2
1 5 3 4 2

Sample Output #00:
3
"""

import sys

f = sys.stdin

k = int(f.readline().split()[1])
nums = f.readline().split()
numSet = set(nums)

count = 0
for n in nums:
    if str(int(n) - k) in numSet :
        count += 1

print count
