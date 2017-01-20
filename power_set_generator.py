# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

#for i in powerSet([2,3,4,5,7,8,9]):
#	print i

# Lecture 2 exercise 1
def powerSetTwoBags(items):
    N = len(items)

    for i in range(3**N):
        base3 = convertToBase3(i)
        base3Length = len(base3)
        bags = ([], [])

        for j in range(N):
            if base3Length <= j:
                continue

            currentDigit = int(base3[base3Length - j - 1])

            if currentDigit % 3 == 1:
                bags[0].append(items[j])
            if currentDigit % 3 == 2:
                bags[1].append(items[j])

        yield bags

def convertToBase3(num):
    result = []
    
    while (num):
        result.append(str(num % 3))
        num /= 3

    return ''.join(reversed(result))

for i in powerSetTwoBags([1,2,3,4,5,6]):
   print i