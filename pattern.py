pattern = input("Enter the pattern: ")
index = pattern.count('L') + pattern.count('l') + 1

print(index, end="")
index, taken = index + 1 if pattern[0] in "mM" else index - 1, [index]

for ch in pattern:
    if ch in 'mM':
        while index in taken:
            index += 1
    else:
        while index in taken:
            index -= 1
    print(index, end='')
    taken.append(index)