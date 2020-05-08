"""
用for循环实现1~100之间的偶数求和


Date: 2018-03-01
"""

sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)
