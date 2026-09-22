arr = [8, 3, 6, 1, 9, 2]
m = arr[0]
for i in range(1, len(arr)):
    if arr[i] < m:
        m = arr[i]
print(m)
# Time Complexity: O(n)
# Space Complexity: O(1)
