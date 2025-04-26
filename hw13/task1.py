#1.
#https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

def is_isogram(string):
    cleaned = string.lower()
    return len(set(cleaned)) == len(cleaned)

# 2.
# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(sequence):
    result = []
    prev = object()
    for item in sequence:
        if item != prev:
            result.append(item)
            prev = item
    return result


# 3.
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

def persistence(num):
    count = 0
    while num >= 10:
        product = 1
        for digit in str(num):
            product *= int(digit)
        num = product
        count += 1
    return count
