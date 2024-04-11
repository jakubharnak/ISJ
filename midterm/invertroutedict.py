routes = {'Brno': {'Berlin', 'London'}, 'Ostrava': {'Split'}}

inverted_routes = {destination_set: origin for origin, 
                   destinations in routes.items() 
                   for destination_set in [frozenset(destinations)]}

print(inverted_routes)

# Pro klíče jsem použil frozenset(destinations) místo set(destinations), 
# protože frozenset je neměnná struktura, což z ní dělá vhodný kandidát pro klíče 
# slovníku. Klíče slovníku by měly být neměnné, protože neměnné objekty jsou hashovatelné
# a mohou být použity jako klíče ve slovnících, zatímco měnitelné objekty, jako je 
# obyčejná množina set, nemohou být použity jako klíče.