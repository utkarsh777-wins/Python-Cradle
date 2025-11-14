#Write a recursive function to print all elements in a list.
def pli(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    pli(list, idx + 1)

heh =("looser", "defeated", "pathetic", "disapointment")

pli(heh)


