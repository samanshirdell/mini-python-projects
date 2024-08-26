# Program to find largest element in an array.
print("Welcome to the find largest element in an array.")

def find_largest_element(arr):
    if not arr:
        return "Array is empty."

    largest_arr = arr[0]

    for element in arr:
        if element > largest_arr:
            largest_arr = element

    return largest_arr

arr_list = []
def status():
    should_continue = True
    make_array = 0
    while should_continue:
        make_list = int(input("Enter number: "))
        arr_list.append(make_list)
        make_array += 1
        if make_array == 5:
            again = input("Do you want continue: Type 'Yes' or 'No': ").lower()
            if again == "yes":
                make_array = 0
                continue
            elif again.isdigit():
                print("Please enter yes or no")
                continue
            elif again == "no":
                should_continue = False
    result = find_largest_element(arr_list)
    print(f"The largest element in the array is: {result}")
status()
