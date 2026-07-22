arr = [10,5,4,20,56]
smallest = arr[0]
for i in range (0,5):
    if arr[i] < smallest:
        smallest = arr[i]

print(smallest)