arr = [2, 4, 2, 6, 2]
target = 2
c = 0
for i in range(len(arr)):
    if arr[i] == target:
        c = c + 1
print(c)
# Time Complexity: O(n)
# Space Complexity: O(1)
