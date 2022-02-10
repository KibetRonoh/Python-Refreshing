#SETS CANNOT TAKE DUPLICATES
art_friends = {"pato", "kim"}
art_friends.add("Jen")

print(art_friends)


# Set operations
sci_friends = {"kim", "Maina"}

art_but_not_sci = art_friends.difference(sci_friends)
sci_but_not =  sci_friends.difference(art_friends)

not_in_both = art_friends.symmetric_difference(sci_friends)

art_and_csi = art_friends.intersection(sci_friends)

all_friends = art_friends.union(sci_friends)