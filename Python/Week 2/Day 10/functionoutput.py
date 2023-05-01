def format_name(f_name, l_name):
    form_f_name = f_name.title()
    form_l_name = l_name.title()
    return (f"{form_f_name} {form_l_name}")

format_name_final = format_name(input("First name?\n"), input("Last name?\n"))

print(format_name_final)