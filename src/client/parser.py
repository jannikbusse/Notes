

def parse_note(note): #improve parsing!
    l = note.split(":")
    if len(l) > 1:
        return l[1], l[0]
    return  l[0], "general"