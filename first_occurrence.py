arr = [4, 7, 2, 7, 9]
target = 7
for i in range(len(arr)):
    if arr[i] == target:
        print(i)
        break
# Time Complexity: O(n)
# Space Complexity: O(1)
