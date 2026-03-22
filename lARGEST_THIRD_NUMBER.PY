# THIRD AND SECOND LARGEST NUMBER LIST AND FOR LOOP  USE
li = [10, 20, 30, 40, 50]

max = -999
sec = -999
third = -999

for i in li:
    if i > max:
        third = sec
        sec = max
        max = i
    elif i > sec and i != max:
        third = sec
        sec = i
    elif i > third and i != max and i != sec:
        third = i

print("Third largest number:", third)
print("SECOND largest number:", sec)
