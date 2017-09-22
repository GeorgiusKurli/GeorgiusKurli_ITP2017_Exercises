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

print("\nI can only invite two people for dinner!\n")

for x in range(0,4):
    temp = guest_list.pop(0)
    print(temp + ", Sorry I can not invite you to dinner.")

for guest in guest_list:
    print(guest + ", You are still invited")

del guest_list[0]
del guest_list[0]
print(guest_list)
