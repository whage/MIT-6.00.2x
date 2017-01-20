def getMeanAndStd(list):
    mean = sum(list) / float(len(list))
    tot = 0.0

    for i in list:
        tot += (i - mean) ** 2

    std = (tot / len(list)) ** 0.5

    return mean, std

def coefficient_of_variation(tup):
    return tup[1] / tup[0]






# lecture 7 exercise 3
def getStdDevForStrings(list):
    stringLengths = [len(i) for i in list]
    mean = sum(stringLengths) / float(len(list))
    tot = 0.0

    for i in list:
        tot += (len(i) - mean) ** 2

    std = (tot / len(list)) ** 0.5

    return std

# lecture 7 exercise 3
def stdDevOfLengths(L):
    if len(L) == 0:
        return float('NaN')

    return getStdDevForStrings(L)








L = ['apples', 'oranges', 'kiwis', 'pineapples']
L2 = []

print(stdDevOfLengths(L))