#-----------------------------------------------------------PhoneRatingAmazon.py-----------------------------------------------------------#
'''
Importing modules:
-plolty.figure_factory(ff)
-pandas(pd)
-csv
-time
'''
import plotly.figure_factory as ff 
import pandas as pd
import csv
import time
#Introductory lines
print("Welcome to PhoneRatingAmazon.py. We provide graphs for ratings of 8 different phone brands in Amazon.")
time.sleep(1.2)

#Displaying all the options possible
phone_choice_array=["Unusable_Element","HUAWEI","Apple","OnePlus","Samsung","Motorola","Sony","Nokia","Xiaomi"]
count=0
for phone in phone_choice_array[1:]:
  count+=1
  print(str(count)+":"+phone)

#Attaining user input
user_input=int(input("Please enter the index of the phone brand whose graphical data you desire to see from the aforementioned list:"))
user_selection=phone_choice_array[user_input]
user_selection=str(user_selection)

#Notifying nad updating the user
if(user_selection<=8):
  print("The phone brand is:"+user_selection)
  print("Processing graph...")
  time.sleep(2.3)
  print("Graph processed")
  time.sleep(0.6)
  print("Displaying graph...")
  time.sleep(1.5)

  #Opening the stipulated file
  phone_brand_selected_list=[]
  with open("Phone_data.csv") as f:
      reader=csv.reader(f)
      for row in reader:   
        if(str(row[1])==user_selection):
          phone_brand_selected_list.append(float(row[2]))
        

  #Defining arrays for the  bell graph
  combined_array=[phone_brand_selected_list]
  combined_label_array=[user_selection]

  #Displaying and mdifying the bell graph
  bell_curve_graph=ff.create_distplot([phone_brand_selected_list],[user_selection],show_hist=False)
  bell_curve_graph.show()
  print("Thank you for using PhoneRatingAmazon.py.")
else:
  print("Request Terminated.")
  print("Invalid Input.")
  print("Thank you for using PhoneRatingAmazon.py.")
#-----------------------------------------------------------PhoneRatingAmazon.py-----------------------------------------------------------#





