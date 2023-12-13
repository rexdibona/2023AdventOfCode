#!/usr/bin/python3
import sys

nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0
for line in sys.stdin:
    num1 = ''
    num2 = ''
    for i in range(len(line)):
        if line[i:i+1] in "0123456789":
            n = line[i:i+1]
            if num1 == '':
                num1 = n
            num2 = n
        else:
            for j in range(len(nums)):
                n = nums[j]
                if line[i:i+len(n)] == n:
#                    print(j)
                    if num1 == '':
                        num1 = str(j)
                    num2 = str(j)
#    print(f"{num1},{num2}")
    sum += int(num1)*10 + int(num2)
print(f"{sum}")

