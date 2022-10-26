import random

def birthday(interp, people_count=23):
    count = 0
    for i in range(interp):
        c = []
        for j in range(people_count):
            age = random.randint(1,365)
            if age in c:
                count += 1
                break
            c.append(age)
    return count/(interp/100)


