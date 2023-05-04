def has_reversed_name(names):
    for name in names:
        if name == name[::-1]:
            return True
    return False
names = ['lidor', 'anna', 'ben', 'yossi']
print(has_reversed_name(names))  