from collections import Counter

def unique(string):
    elements= list(string)
    for i in range(len(elements)):
        elem = elements[i]
        new_list=elements[i+1:]
        if elem in new_list:
            return False
    return True

def check_permutation(string1, string2):
    s1 = list(set(list(string1)))
    s2 = list(set(list(string2)))

    return sorted(s1) == sorted(s2)

def replace(string1, elem, rep):
    string = list(string1)
    print('Iterative method')
    for item in string:
        if item == elem:
            ind = string.index(item)
            string[ind]=rep
    print(''.join(string))
    print('Pythonic method')
    string1 = string1.replace(elem, rep)
    print(string1)
    return ''.join(string)


def permutation_palindrome(string):
    string = string.replace(' ', '').lower()
    num_odd = sum(f%2 for f in Counter(string).values())
    return num_odd < 2

def one_way(string1, string2):
    if abs(len(string1)-len(string2)) > 1:
        return False
    m=len(string1)
    n=len(string2)
    i=0
    j=0
    count=0
    while i < m and j < n:
        if string1[i] != string2[j]:
            if count == 2:
                return False

            if m > n:
                i+=1
            elif m < n:
                j+=1
            else:
                i+=1
                j+=1
            count+=1
        else:
            i+=1
            j+=1

    return count == 2

def string_compression(string):
    result=[]
    print('Counter method')
    for k, v in Counter(string).items():
        result.append(k)
        result.append(str(v))
    print(''.join(result))

    print('Normal Dictionary method')
    s = list(string)
    dic = {}
    for i in range(len(s)):
        elem = s[i]
        for j in range(i+1, len(s)):
            if s[i] == s[j] and s[i] not in dic.keys():
                dic[s[i]] = str(1)
            elif s[i] == s[j] and s[i] in dic.keys():
                val = int(dic[s[i]])
                dic[s[i]] = str(val+1)
    result2=[]
    for k, v in dic.items():
        result2.append(k)
        result2.append(v)
    print(''.join(result2))


def reverse_words(string):
    words = string.split(" ")
    results=[]
    for item in words:
        results.append(item[::-1])
    return " ".join(results)

def reverse_String(string):
    return string[-1::-1]


def remove_consecutive_duplicates(string):
    if len(string)==0 or len(string) == 1:
        return string

    if string[0] == string[1]:
        while len(string) > 1 and string[0] == string[1]:
            string=string[1:]
        string = string[1:]

        return remove_consecutive_duplicates(string)

    rem_string = remove_consecutive_duplicates(string[1:])


    return string[0]+rem_string


def max_occur_charc(string):
    return max(Counter(string))


def remove_duplicates(s):
    processed=[]
    s = list(s)
    for item in s:
        if item in processed:
            item=''
        else:
            processed.append(item)
    return "".join(processed)

def print_dup(s):
    s = Counter(s)
    result=[]
    for k,v in s.items():
        if v > 1:
            result.append(k)

    return result

def first_unique_string(s):
    for i in range(len(s)-1):
        ch = s[i]
        if ch not in s[i+1:]:
            return i

    return -1

def longest_palindromic_substring(s):
    n=len(s)
    p_string=''
    high=0
    low=0
    max_len=0
    start=0

    for i in range(1,n):
        low = i - 1
        high = i
        while low >= 0 and high < n and s[low] == s[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1

        # Find the longest odd length palindrome with center
        # point as i
        low = i - 1
        high = i + 1
        while low >= 0 and high < n and s[low] == s[high]:
            if high - low + 1 > max_len:
                start = low
                max_len = high - low + 1
            low -= 1
            high += 1

    print("Longest palindrome substring is:"+s[start:start+max_len])




print(first_unique_string('leetcode'))