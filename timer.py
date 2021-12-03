import datetime
import csv

mark_list = []

#extract the first line of the fleet.csv file to use as headers in a table [boat_name, tcf1_name, tcf2_name,...]
def get_file_headers(fleet_file):
    with open(fleet_file) as input:
        reader = csv.reader(input)
        file_headers = next(reader)
    return file_headers

#extract the ratings for each boat to a 2d list [[boat1, tcf1, tcf2, ...],[boat2, tcf1, tcf2, ...],[,,,]]
def get_file_data(fleet_file):
    with open(fleet_file) as input:
      reader = csv.reader(input)
      next(reader)
      file_data = [row for row in reader]
    return file_data

#select which tcf band to use
def select_tcf_band(hdr):
    print('Which rating band do you want to use? [enter the corresponding number, not the name]')
    is_tcf = True
    while is_tcf:
        for i in range (1,len(hdr)):
            print(str(i) +": " + hdr[i])
        itcf = int(input("Please enter a number between 1 and "+str(len(hdr)-1 )+": "))
        if itcf < len(hdr) and itcf > 0:
            is_tcf = False
    return itcf

#extract boat and rating as a dictionary
def get_race_ratings(tcf_id,data):
    race_rating = {}
    for i in range(len(data)):
        race_rating[data[i][0]] = data[i][tcf_id]
    return race_rating


# requests start time in HH:MM:SS
# adds todays date and returns a string YYYY,MM,DD,HH,MM,SS
def get_start_time():
  today = datetime.date.today()                       #get date
  today_str = str(today)                              #convert to str
  start_time_input = "10:00:00"                       #default for testing, input line below to be used in place of the 10:00:00
                      # input("Enter race start time (24 hr clock, HH:MM:SS)")
  start_t_list = start_time_input.split(":")          #convert st time str to list
  today_list = today_str.split("-")                   #convert date str to list
  start_list = today_list + start_t_list              #start date and time list
  start_time_str = start_list[0]+","                  #create start date time sting
  for i in range(1,5):
    start_time_str += (start_list[i]+",")
  start_time_str += start_list[5]

  y, m, d, h, mm, s = start_time_str.split(',')      #get elements of date and time
  start_time = datetime.datetime(int(y),int(m),int(d),int(h),int(mm),int(s))    #convert to datetime format
  return start_time

#takes start time as input, requests fin time set, returns fin time and elasped
def get_fin_el_tm(start):
  fin_tm = input("Press Enter to set mark time:")
  fin_tm = datetime.datetime.now()
  return fin_tm, fin_tm-start

#input st time and boat/rating dict, returns boat name, st,fin/el and corr times
def get_corr_time(ratings, st_tm):
  boats_list = list(ratings)
  # print(boats_list)
  print("Select boat [enter the corresponding number, not the name]: ")
  is_boat = True
  while is_boat:
    for i in range(len(boats_list)):
      print(i+1,": ", boats_list[i])
    boat = int(input("Please enter a number from 1 to "+str(len(boats_list))+": "))
    boat -= 1
    if boat <= len(boats_list) and boat >= 0:
      is_boat = False
  fin_tm, el_tm = get_fin_el_tm(st_tm)
  tcf = float(ratings.get(boats_list[boat]))
  return boats_list[boat],tcf,st_tm,fin_tm,el_tm,el_tm * tcf

#create a list of marks to time against
def get_marks():
  if len(mark_list) == 0:
    mark = input("Enter first mark name: ")
    mark_list.append(mark)
    get_marks()
  else: 
    add_mark = True
    while add_mark:
      add_new_mark = input("Add next mark [or press ENTER to exit]: ")
      if len(add_new_mark) != 0:
        mark_list.append(add_new_mark)
      else: add_mark = False

#choose the mark to score at
def select_mark():
  print("Select mark: [mark number, not name]")
  for i in range(len(mark_list)):
    print(i+1,": ",mark_list[i])
  curnt_mark = int(input("Enter mark number: "))
  if curnt_mark >= 0 or curnt_mark <= len(mark_list)-1:
    return mark_list[curnt_mark-1]
  else: select_mark




#######################################################################
results_f = input("Enter the file name to save race results to: ")
results_f_ext = results_f+".csv"
f=open(results_f_ext,'a')

rating_headers = get_file_headers('static/fleet.csv')  
rating_data = get_file_data('static/fleet.csv')
tcf_index = select_tcf_band(rating_headers)
race_ratings = get_race_ratings(tcf_index,rating_data)
start_tm = get_start_time()
get_marks()

# print("Rating band selected:",rating_headers[tcf_index],"\n Race:",rating_headers[0],"\n",race_ratings)

str_race_rating = str(rating_headers[tcf_index])
str_fleet_ratings = str(race_ratings)

#write to the file the tcf used and the column headers
f.write("Rating band: "+str_race_rating)            
f.write("\nMark,Boat,TCF,Start,Fin,Elapsed,Corrected")


racing = True
while racing:
  score_race = input("Do you want to score a mark? ENTER for yes, 'N' to exit: ")
  if len(score_race) == 0:
    mark = select_mark()
    result = get_corr_time(race_ratings,start_tm)
    str_tcf = str(result[1])
    str_st_tm = str(result[2])
    str_fin_tm = str(result[3])
    str_el_tm = str(result[4])
    str_corr_tm = str(result[5])

    # print("Mark:",mark,"\nBoat:",result[0],"\nRating:", result[1],"\nStart time:",result[2],"\nFinish time:",result[3],"\nElapsed time:",result[4],"\nCorrected time:",result[5])
    f.write("\n"+mark+","+result[0]+","+str_tcf+","+str_st_tm+","+str_fin_tm+","+str_el_tm+","+str_corr_tm)
  else: racing = False

