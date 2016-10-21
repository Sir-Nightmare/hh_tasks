def reverse_number(number):
    s = str(number)
    return int(s[::-1])


def is_palindrome(number):
    s = str(number)
    if s == s[::-1]:
        return True
    return False


num_of_pal = 0
# uncomment everything if you want to see all non palindromes
# non_pal = 0
for i in range(12259):
    a = i;
    for j in range(50):
        a += reverse_number(a)
        if is_palindrome(a):
            num_of_pal += 1
            break
            # else:
            #     print(i)
            #     non_pal += 1
print()
print('ANSWER Number of palindromes ', num_of_pal)
# print('Number of non palindromes:', non_pal)
# print('Whole number', num_of_pal + non_pal)
