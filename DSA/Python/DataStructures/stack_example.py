def main():
    # Initialize stack
    stack = []

    # Push
    print("Pushing element onto the stack: 1")
    stack.append(1)

    # Pop
    if stack:
        popped_element = stack.pop()
        print(f"Popped element from the stack: {popped_element}")
    else:
        print("Stack is empty. Cannot pop.")

    # Peek
    if stack:
        top_element = stack[-1]
        print(f"Top element of the stack: {top_element}")
    else:
        print("Stack is empty. No top element to peek.")

    # Add more elements
    stack.append(2)
    stack.append(3)
    print(f"Stack size: {len(stack)}")

    # Different ways to iterate
    print("\nIterating through Stack using for loop:")
    for element in stack:
        print(f"Element: {element}")

    print("\nIterating using enumerate:")
    for i, element in enumerate(stack):
        print(f"Element: {element}")

    print("\nIterating using list comprehension:")
    [print(f"Element: {element}") for element in stack]

if __name__ == "__main__":
    main()
