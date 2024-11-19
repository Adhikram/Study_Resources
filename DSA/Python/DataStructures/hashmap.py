def main():
    # Create a dictionary with key as String and value as Integer
    hashMap = {}

    # Insert (put)
    print("Inserting values into dictionary:")
    hashMap["One"] = 1
    hashMap["Two"] = 2
    hashMap["Three"] = 3
    print("Dictionary after insertion:", hashMap)

    # Accessing values
    print("Value for key 'One':", hashMap.get("One"))

    # Checking if a value exists
    print("Is value twelve in dictionary?", "Not found" if hashMap.get("twelve") is None else "Yes")

    # Checking if a key exists
    print("Is 'Two' in dictionary?", "Two" in hashMap)

    # Removing a key-value pair
    removed_value = hashMap.pop("Two", None)
    print("Removed value for key 'Two':", removed_value)
    print("Dictionary after removing 'Two':", hashMap)

    # Iterating over keys
    print("Keys in dictionary:")
    for key in hashMap.keys():
        print(key)

    # Iterating over values
    print("Values in dictionary:")
    for value in hashMap.values():
        print(value)

    # Iterating over key-value pairs
    print("Key-value pairs in dictionary:")
    for key, value in hashMap.items():
        print(f"{key}: {value}")

    # Updating dictionary with another dictionary
    hashMap.update({"Four": 4, "Five": 5})
    print("Dictionary after update:", hashMap)

    # Clearing the dictionary
    hashMap.clear()
    print("Dictionary after clearing:", hashMap)

if __name__ == "__main__":
    main()