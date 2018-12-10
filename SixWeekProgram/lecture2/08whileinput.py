
print("Enter names until you are done. When you are done, enter 'done'")

# This is code to teach while loops
name = None
while name != "done":
    name = input("Enter a name: ")
    # if name != "done":
    print("Hello, {}.".format(name))
