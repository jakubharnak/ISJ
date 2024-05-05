s = { 'FORTRAN' : '1954', 'ALGOL' : '1954', 'C++'  : '1985' }
a = (c[1] for c in sorted(s, key=s.get))
for u in a:
    print(u)
    
# O
# L
# +