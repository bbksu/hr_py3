def mutate_string(string, position, character):
    return f"{string[:position]}{character}{string[position+1:]}"
