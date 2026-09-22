arr = [1, 2, 3, 4, 5]
new = []
for i in range(len(arr) - 1, -1, -1):
    new.append(arr[i])
print(new)
# Time Complexity: O(n)
# Space Complexity: O(n)
