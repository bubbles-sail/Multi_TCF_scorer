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
    mark_ind = []                                                          #creates mark index - would normally call/pass from timer.py?
    for i in range(len(mark_list)):
        mark_ind.append(i+1)
    return rating, ref_boat, mark_list, mark_ind, headers, race_data

def get_sorted_results(race_d, marks):
    ct_sort = sorted(race_d, key=itemgetter(6))                             #sort results by ct_sort
    ct = sorted(ct_sort, key=itemgetter(0))                                 #then sort by mark
    for i in range(len(ct)):                                                #convert strings to int/float/dateteime etc
        time_string = ct[i][3]
        ct[i][3] = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S')      #start time
        time_string = ct[i][4]
        ct[i][4] = datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S.%f')   #mark rounding time
        time_string = ct[i][5]
        ct[i][5] = datetime.strptime(time_string, '%H:%M:%S.%f')            #elapsed time
        time_string = ct[i][6]
        ct[i][6] = datetime.strptime(time_string, '%H:%M:%S.%f')            #corrected time
        mark_string = ct[i][0]
        ct[i][0] = int(mark_string)                                         #mark id
        rating_string = ct[i][2]
        ct[i][2] = float(rating_string)                                     #tcf
    temp_list = []
    d_ct = []
    for i in marks:
        for j in range(len(ct)):
            if i == int(ct[j][0]):
                temp_list.append(ct[j])
        for k in range(1,len(temp_list)):
            temp_list[k].append(temp_list[k][6] - temp_list[k-1][6])        #calc how far behind in ct to prev boat & append to boat
        temp_list[0].append(datetime.now() - datetime.now())                #append 00:00:00 to first boat
        d_ct.append(temp_list)
        temp_list=[]
    return d_ct

#####################################################################################

rating_band, ref_boat, marks, mark_id, file_headers, race_data = get_race_data()    #reference_boat
ct_rank = get_sorted_results(race_data, mark_id)

f_results = open("Results.csv","a")
f_results.write("Race results\nRating,"+rating_band+"\nMk num,Mk name")
for i in range(len(marks)):
    f_results.write("\n"+str(mark_id[i])+","+str(marks[i]))
f_results.write("\nReference boat:,"+ref_boat)

f_results.write("\n\nCorrected time rank:\nBoat,Elapsed,Corrected,dCorrected")
f_results.write("\n")
for i in mark_id:
    f_results.write("Mark "+str(i)+"\n")
    for j in ct_rank:
        for k in j:
            if k[0] == i:
                f_results.write(k[1]+","+k[5].strftime("%H:%M:%S.%f")+","+k[6].strftime("%H:%M:%S.%f")+","+str(k[7])+"\n")


#todos
    #for each boat calc gain/loss from prev mark for ref boat