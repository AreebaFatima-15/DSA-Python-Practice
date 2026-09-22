arr = [10, 5, 8, 20, 15]
LARG = arr[0]
second = arr[0]
for i in range(len(arr)):
    if arr[i] > LARG:
        second = LARG
        LARG = arr[i]
    elif arr[i] > second:
        second = arr[i]
print(second)
# Time Complexity: O(n)
# Space Complexity: O(1)
