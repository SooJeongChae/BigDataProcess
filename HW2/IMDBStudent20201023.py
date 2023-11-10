#!/usr/bin/python3

in_file = input()
out_file = input()

with open(in_file, "rt") as f:
    in_data = f.read()

sep_enter = in_data.split("\n")
sep_plus = ''
for s in sep_enter:
    sep_plus += s
    sep_plus += "::"

sep_colon = sep_plus.split("::")
genre = ''
i = 1
for s in sep_colon:
    if i % 3 == 0:
        genre += s
        genre += "|"
    i += 1

genre = genre[:-1]
genre_list = genre.split("|")
genre_count = {}
for s in genre_list:
    if s not in genre_count:
        genre_count[s] = 1
    else:
        genre_count[s] += 1

genre_print = list(genre_count.items())
genre_print.sort(key = lambda x:-x[1])
#for x, y in genre_print:
#    print(x, y)

out_data = ''
for x, y in genre_print:
    out_data += x + " " + str(y) + "\n"

f = open(out_file, "wt")
f.write(out_data)
f.close()
