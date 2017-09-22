current_users = ["Jim", "Bob", "Raymond", "admin", "Joe"]
new_users = ["Ralph", "JIM", "joe", "Zulu", "Romeo"]

for user in new_users:
    if user.title() in current_users:
        print("This name has been taken!")
    else:
        print("The name is available.")
