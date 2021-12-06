import csv
from operator import itemgetter

f_results = open("sort test.csv","r")

with open("sort test.csv","r") as input:
    reader = csv.reader(input)
    rating = next(reader)
    marks = next(reader)
    headers = next(reader)
    race_data = [row for row in reader]

# print(rating)
print(marks)
# print(headers)
# print(race_data)

#reduce data into mark, boat, el and cor times
race_data_sht = race_data
for i in range(len(race_data)):
    del race_data_sht[i][3:5]

# print(race_data_sht)
race_mk_sort = []
#sort data into mark roundings
for i in range(len(race_data_sht)):
    for j in range(1,len(marks)):
        if race_data_sht[i][0] == marks[j]:
            race_mk_sort.append(race_data_sht[i])
# print(race_mk_sort,"\n\n")

#sort race markings by elap t

#need to extract list of lists that have same mark, then sort by et and ct

# race_mk_el_sort = []
# single_mk_list = []
# temp_list = []
# for i in range(len(race_mk_sort)):
#     for j in range(len(marks)):
#         if race_mk_sort[i][0] == marks[j]:
#             for k in range(len(race_mk_sort[i]))
#             single_mk_list.append(race_mk_sort[i])
#             # print(single_mk_list)
#     sorted(single_mk_list, key=itemgetter(4))
#     print(single_mk_list)
#     race_mk_el_sort.append(single_mk_list)
# print(race_mk_el_sort,"\n\n")

# race_mk_cor_sort = []
# single_mk_list = []
# for i in range(len(race_mk_sort)):
#     for j in range(len(marks)):
#         if race_mk_sort[i][0] == marks[j]:
#             single_mk_list.append(race_mk_sort[i])
#     sorted(single_mk_list, key=itemgetter(4))
#     race_mk_cor_sort.append(single_mk_list)
# print(race_mk_cor_sort)