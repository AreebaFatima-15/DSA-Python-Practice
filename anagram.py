string1 = input("Enter first string: ")
string2 = input("Enter second string: ")
if len(string1) != len(string2):
    print(False)
else:
    frequency1 = {}
    frequency2 = {}
    for i in string1:
        if i in frequency1:
            frequency1[i] = frequency1[i] + 1
        else:
            frequency1[i] = 1
    for i in string2:
        if i in frequency2:
            frequency2[i] = frequency2[i] + 1
        else:
            frequency2[i] = 1
    if frequency1 == frequency2:
        print(True)
    else:
        print(False)
# Time Complexity: O(n)
# Space Complexity: O(n)
