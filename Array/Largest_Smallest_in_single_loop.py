arr = [15, 8, 22, 3, 18]


smallest = arr[0]
largest = arr[0]
for i in range(0, 5):
    if arr[i] < smallest:
        smallest = arr[i]
    if arr[i] > largest:
        largest = arr[i]    
print("Smallest element:", smallest)
print("Largest element:", largest)