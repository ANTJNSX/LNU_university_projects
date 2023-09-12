from statistics import median

# take input list of salarys
# print median
# calc average
# calc gap

salaries = [21700, 28200, 26300, 25100, 22600, 22800, 19900]

# besides using the median function i could have checked the length if its even or odd
# if odd, return the middle value
# if even, return the middle values added together and divided by 2. Getting them by dividing the length by 2 rounding it with ceiling() 
# and getting the value next to it with taking the same value -1

print("Median:", median(salaries))

# add together every value in the list together
s=0
for sal in salaries:
    s += sal
print("Average:",round(s/len(salaries)))

# Round the result of subtracting the max and min value in the list
print("Gap:", round(max(salaries)-min(salaries)))
