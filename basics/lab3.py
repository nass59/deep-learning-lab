# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
print(out2)

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second
print(full)

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)

# Print out the index of the element 20.0
print(full_sorted.index(10.75))

# Print out how often 14.5 appears in areas
print(full_sorted.count(18.0))

# Use append twice to add poolhouse and garage size
full_sorted.append(24.5)
full_sorted.append(15.45)


# Print out areas
print(full_sorted)

# Reverse the orders of the elements in areas
full_sorted.reverse()

# Print out areas
print(full_sorted)

# string to experiment with: room
room = "poolhouse"

# Use upper() on room: room_up
room_up = room.upper()

# Print out room and room_up
print(room)
print(room_up)

# Print out the number of o's in room
print(room.count("o"))
