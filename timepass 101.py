arr = [0]
proceed = 1
stop = False
while not stop:
    proceed = input("Add numbers to your list (if finished type '.end') ")
    if proceed.lower() != ".end":
        proceed = int(proceed)
        arr.append(proceed)

    if proceed == ".end":
        break

print_result = True

# Bubble sort

swapped = True
for i in range(len(arr)):
    swapped = False
    for position in range((len(arr)) - 1):
        if arr[position] > arr[position + 1]:
            swapped = True
            storage = arr[position]
            arr[position] = arr[position + 1]
            arr[position + 1] = storage
    if not swapped:
        break

print("Here is the list you created \n", arr)

# Binary Search

search = int(input("\n\nSearch for some thing in your list "))
start = 0
end = len(arr)
result = "Your list is empty"
while (end - start) > 0:
    mid = int((end + start) / 2)
    if arr[mid] == search:
        result = mid
        break
    if arr[mid] < search:
        start = mid
    if arr[mid] > search:
        end = mid
    if search not in arr:
        print("\nThe item does not exist in your list ")
        print_result = False
        break
if print_result:
    print(" The position of the ID", search, "is in number", result)
