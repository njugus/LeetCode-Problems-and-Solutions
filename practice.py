# Hashing
# find the first unique character in a string

my_string = "kelvin njuguna"
character_list = [ c for c in my_string if c != ' ']
character_freq = {}

print(character_list)
for character in character_list:
    if character in character_freq:
        character_freq[character] += 1
    else:
        character_freq[character] = 1

# loop through and get the first unique element
for element in character_freq:
    if character_freq[element] == 1:
        print(f"{element} is the first unique character in the string")
        break

else:
    print("No unique character found")
