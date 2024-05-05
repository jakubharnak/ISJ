s = {"Python": 1991, "Perl": 1987, "Ruby": 1995}

print("".join(c[1] for c in sorted(s, key=s.get)))

# What is the output of this code? - eyu