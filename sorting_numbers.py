def bubble_sort(arr, ascending=True):
    """Sort using bubble sort algorithm"""
    n = len(arr)
    sorted_arr = arr.copy()
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascending:
                if sorted_arr[j] > sorted_arr[j + 1]:
                    sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
            else:
                if sorted_arr[j] < sorted_arr[j + 1]:
                    sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
    
    return sorted_arr

def selection_sort(arr, ascending=True):
    """Sort using selection sort algorithm"""
    n = len(arr)
    sorted_arr = arr.copy()
    
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if ascending:
                if sorted_arr[j] < sorted_arr[idx]:
                    idx = j
            else:
                if sorted_arr[j] > sorted_arr[idx]:
                    idx = j
        sorted_arr[i], sorted_arr[idx] = sorted_arr[idx], sorted_arr[i]
    
    return sorted_arr

def quick_sort(arr, ascending=True):
    """Sort using Python's built-in sort"""
    sorted_arr = arr.copy()
    sorted_arr.sort(reverse=not ascending)
    return sorted_arr

def display_menu():
    print("\n===== Number Sorting Program =====")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Quick Sort (Built-in)")
    print("4. Exit")
    print("===================================")

def get_numbers():
    """Get numbers from user input"""
    while True:
        try:
            numbers_input = input("\nEnter numbers separated by spaces: ")
            numbers = [float(x) for x in numbers_input.split()]
            
            if len(numbers) == 0:
                print("Please enter at least one number!")
                continue
            
            return numbers
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

def get_order():
    """Get sorting order from user"""
    while True:
        order = input("Sort in (1) Ascending or (2) Descending order? Enter 1 or 2: ")
        if order in ['1', '2']:
            return order == '1'
        print("Invalid choice! Please enter 1 or 2.")

def sorting_program():
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '4':
            print("Thank you for using the sorting program. Goodbye!")
            break
        
        if choice not in ['1', '2', '3']:
            print("Invalid choice! Please select a valid option.")
            continue
        
        numbers = get_numbers()
        ascending = get_order()
        
        print(f"\nOriginal numbers: {numbers}")
        
        if choice == '1':
            sorted_numbers = bubble_sort(numbers, ascending)
            print(f"Bubble Sort Result: {sorted_numbers}")
        elif choice == '2':
            sorted_numbers = selection_sort(numbers, ascending)
            print(f"Selection Sort Result: {sorted_numbers}")
        elif choice == '3':
            sorted_numbers = quick_sort(numbers, ascending)
            print(f"Quick Sort Result: {sorted_numbers}")

if __name__ == "__main__":
    sorting_program()
