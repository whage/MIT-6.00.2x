def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
    subsequences = enumerate_subsequences(L)
    sums = [sum(seq) for seq in subsequences]

    return max(sums)

def enumerate_subsequences(list):
    subsequences = []

    for subLength in range(1, len(list) + 1):
        start = 0
        end = subLength

        while end <= len(list):
            seq = list[start:end]
            subsequences.append(seq)
            start += 1
            end += 1

    return subsequences