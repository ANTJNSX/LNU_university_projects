from statistics import median

# take input list of salarys
# print median
# calc average
# calc gap

salaries = [21700, 28200, 26300, 25100, 22600, 22800, 19900]

print("Median:", median(salaries))
s=0
for sal in salaries:
    s += sal

print("Average:",round(s/len(salaries)))

print("Gap:", round(max(salaries)-min(salaries)))
