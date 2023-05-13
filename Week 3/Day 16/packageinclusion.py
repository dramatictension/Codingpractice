from prettytable import PrettyTable

table = PrettyTable()
table.align = "l"
print(table.align)
table.add_column("Pokémon",["Bulbasaur", "Squirtle", "Charmander"])
table.add_column("Type",["Grass", "Water" , "Fire"])
print(table)