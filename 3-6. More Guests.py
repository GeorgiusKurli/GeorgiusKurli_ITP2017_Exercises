guest_list = ["Ghandi", "Albert Einstein", "Isaac Newton"]
invitation = ", You are invited to dinner."
print(guest_list[0] + invitation)
print(guest_list[1] + invitation)
print(guest_list[2] + invitation)

print("\nI found a bigger table!\n")

guest_list.insert(0, "Abraham Lincoln")
guest_list.insert(2, "Nikola Tesla")
guest_list.append("Winston Churchill")
for guest in guest_list:
    print(guest + invitation)
