def mutate_string(string, position, character):
    
    str=string[:position]+ character + string[position+1:]
    return str