#!/usr/bin/env python

str1 = str(input("Enter the Correct String :"))
str2 = str(input("Enter the Wrong String :"))

str1 = list(str1)
str2 = list(str2)

count = abs(len(str1) - len(str2))
for i in range(min(len(str1),len(str2))):
    if not str1[i] == str2[i]:
        count += 1

print("The hamming distance between the strings is :",count)

