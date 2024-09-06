def input_list():
    user_list = []
    while True:
        item = input("Enter an item (or type 'done' to finish): ")
        if item.lower() == 'done':
            break
        user_list.append(item)
    return user_list


user_list = input_list()

print("The list of inputs is:")
print(user_list)
