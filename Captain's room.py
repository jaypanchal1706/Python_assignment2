"""
Name = Panchal Jay Manojkumar
Id = 20CE068
Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of K members per group where K ≠ .

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists.
 The room numbers will appear K times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of K and the room number list.

Github link = https://github.com/jaypanchal1706/Python_assignment2.git
"""

# Take the input from the user
# k is the family member per group
K = int(input())
# Declare set in which room number can be inerted
set_S = set()
# sumlist set is use for sum of all the room number
sumlist = 0
# Scan the all the room number

for i in input().split():
    room_number = int(i)
    set_S.add(room_number)
    sumlist += room_number

# Print captain's room number
captain_room = int((sum(set_S) * K - sumlist) // (K - 1))
print(captain_room)
