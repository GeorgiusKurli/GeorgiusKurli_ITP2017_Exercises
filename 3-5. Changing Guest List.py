guest_list = ["Ghandi", "Albert Einstein", "Isaac Newton"]
invitation = ", You are invited to dinner."
print(guest_list[0] + invitation)
print(guest_list[1] + invitation)
print(guest_list[2] + invitation)
print(guest_list[0] + " can not join tonight.")

guest_list[0] = "Abraham Lincoln"
for guest in guest_list:
    print(guest + invitation)
