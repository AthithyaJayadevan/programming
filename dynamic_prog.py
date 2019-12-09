from sys import maxsize
def longest_common_subsequence_len(s1, s2):
    if s1 == '' or s2 == '':
        return 0

    if s1[-1] == s2[-1]:
        return 1 + longest_common_subsequence_len(s1[:-1], s2[:-1])
    else:
        return max(longest_common_subsequence_len(s1, s2[:-1]), longest_common_subsequence_len(s1[:-1], s2))


def maximum_sum_of_contigous_subarray(arr):
    n=len(arr)
    max_val = -maxsize -1
    max_ending_here = 0
    start=0
    rstart=0
    rend=0

    for i in range(n):
        max_ending_here += arr[i]
        if max_ending_here > max_val:
            max_val = max_ending_here
            rend=i
            rstart=start
        if max_ending_here <0:
            max_ending_here = 0
            start=i+1

    return max_val,rstart,rend


def maximum_sum_matrix(matrix):
    max_sum=0
    maxright=-1
    maxleft=-1
    maxtop=-1
    maxbottom=-1

    rows= len(matrix)
    cols = len(matrix[0])

    for l in range(cols):
        row_sum=[0]*rows
        for r in range(l, cols):
            for i in range(rows):
                row_sum[i]+=matrix[i][r]
            k_sum,regionstart,regionend = maximum_sum_of_contigous_subarray(row_sum)

            if max_sum < k_sum:
                max_sum = k_sum
                maxright=r
                maxleft=l
                maxtop=regionstart
                maxbottom=regionend



    result=[sam[maxleft:maxright+1] for sam in matrix[maxtop:maxbottom+1]]
    print(result)

    return [sam[maxleft:maxright+1] for sam in matrix[maxtop:maxbottom+1]], max_sum




matrix=[[6, -5,  -7,  4, -4 ],
    [  -9,  3,  -6,  5,  2 ],
    [ -10,  4,   7, -6,  3 ],
    [  -8,  9,  -3,  3, -7 ]]

print(maximum_sum_matrix(matrix))





print(longest_common_subsequence_len('wkjhbvkiuwk', 'aknjfhnbmi'))