import csv
from operator import itemgetter
from datetime import datetime

def get_race_data():
    with open("RACE 1.csv","r") as input:
        reader = csv.reader(input)
        rating = next(reader)
        rating = str(rating[1])
        ref_boat = next(reader)
        ref_boat = str(ref_boat[1])
        mark_list = next(reader)
        mark_list.remove("Marks: ")
        headers = next(reader)
        race_data = [row for row in reader]
    mark_ind = []                     #creates mark index - would normally call/pass from timer.py?
    for i in range(len(mark_list)):
        mark_ind.append(i+1)
    return rating, ref_boat, mark_list, mark_ind, headers, race_data

# def get_time_deltas():
#     temp_list = []
#     for i in mark_id:
#         for j in range(len(race_d)):
#             if i == race_d[0]:
#                 temp_list.append(race_d[j])
            #calulate each time delta to be added to race_d[]
            #append time deltat to race_d[][] as appropriate
        

def get_sorted_results(race_d, mark_ids):
    et_sort = sorted(race_d, key=itemgetter(5))
    et = sorted(et_sort, key=itemgetter(0))
    ct_sort = sorted(race_data, key=itemgetter(6))
    ct = sorted(ct_sort, key=itemgetter(0))
    return et, ct



#####################################################################################
#Write results to file

rating_band, ref_boat, marks, mark_id, file_headers, race_data = get_race_data()    #reference_boat
et_rank, ct_rank = get_sorted_results(race_data, mark_id)

#convert race data to datetime format
for j in range(len(ct_rank)):
        time_string = ct_rank[j][3]
        ct_rank[j][3] = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')
        time_string = ct_rank[j][4]
        ct_rank[j][4] = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S.%f')
        time_string = ct_rank[j][5]
        ct_rank[j][5] = datetime.strptime(time_string, '%H:%M:%S.%f')
        time_string = ct_rank[j][6]
        ct_rank[j][6] = datetime.strptime(time_string, '%H:%M:%S.%f')


print(ct_rank)

temp_list = []
d_ct_rank = []
for i in mark_id:
    for j in range(len(ct_rank)):
        if i == int(ct_rank[j][0]):
            temp_list.append(ct_rank[j])
    for k in range(1,len(temp_list)):
        temp_list[k].append(temp_list[k][-1] - temp_list[k-1][-1])
    d_ct_rank.append(temp_list)        
print(d_ct_rank)

f_results = open("Results.csv","a")
f_results.write("Race results\nRating,"+rating_band+"\nMk num,Mk name")
for i in range(len(marks)):
    f_results.write("\n"+str(mark_id[i])+","+str(marks[i]))
f_results.write("\nReference boat:,"+ref_boat)
f_results.write("\n\nElapsed time rank:\n")
for i in range(len(file_headers)):
    f_results.write(file_headers[i]+",")
f_results.write("\n")

for i in et_rank:
    for j in i:
        f_results.write(str(j)+",")
    f_results.write("\n")

f_results.write("\n\nCorrected time rank:\n")
for i in range(len(file_headers)):
    f_results.write(file_headers[i]+",")
f_results.write("\n")

for i in ct_rank:
    for j in i:
        f_results.write(str(j)+",")
    f_results.write("\n")