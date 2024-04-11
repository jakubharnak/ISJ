import collections

flights = [('Brno','London'), ('Ostrava', 'Split') , ('Brno','Berlin') ]

routes = collections.defaultdict(set)

for (origin, destination) in flights:
    routes[origin].add(destination)

print(routes)