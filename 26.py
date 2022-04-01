# Suppose the count function for a string didn’t exist. Define a
# function that returns the number of non-overlapping occurrences of a substring in
# a string

def howMany(s1, s2):
    if s2 != "":
        n = 0 
        i = 0
        while i < len(s1):
            if s1[i:].startswith(s2):
                n += 1
                i = i + len(s2)
            else:
                i += 1
        return n
    else:
        return len(s1) + 1
