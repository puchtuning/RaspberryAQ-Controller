#--- Check for Blanks
def is_not_blank(mystring, length):
    if(len(mystring) == length):
        print("")
    else:
        # Erstellt einen Error der durch die try Funktion gewertet erden kann
        raise ValueError('No Value specified')
