def valide(partialSln,items):
    for i in partialSln:
        if i == items:
            return False
    return True

def Perm(inset, partialSln):
    if len(inset)== len(partialSln):
        print(partialSln)
    else:
        for items in inset :
            if valide(partialSln, items):
                partialSln.append((items))
                Perm(inset, partialSln)
                del partialSln[-1]