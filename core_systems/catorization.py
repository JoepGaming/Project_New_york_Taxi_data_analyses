"""""" "date", "day", "month", "day_type", "pickup_time", "dropoff_time", "distance", "kost"
from datetime import datetime, time
def catogarize(workdir):
    print("initiating catagorization process")
    #initialize empty dictionary with lists representing the subcategories of months and rush hours, and a list for al entries that were flagged by the system as nonvalid
    nonvalid = []
    lists = {}
    months = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december"
    ]
    # list of months created with ai
    
    for month in months:
        lists[month + "_standard"] = []
        lists[month + "_rush"] = []
        lists[month + "_overnight"] = []

    #locate the file
    taxi_data = workdir / "data_new" / "2025_Green_Taxi_Trip_Data_used.csv"

    #open the file and turn each line into a dictionarry for easy handling
    print("starting catorization process")
    with open(taxi_data, "r") as taxi_data:
        
        # first the header of the table is coppied to be used as the names for the variables in the dictionary
        header = next(taxi_data).strip().split(";")

        #progress is also created to show up as a percentage of progress, because this step takes a while on older machines
        progress = 0
        progress_percentage = 0

        # now for the actual catagorizing part
        for line in taxi_data:

            #first the progress is calculated as a percentage
            progress_percentage_previous = progress_percentage
            progress_percentage = int((progress/591485)*100) # 591485 is the theoretical amount of lines in the taxi_data file

            # if the amount of progress has changed, this is printed to the user
            if progress_percentage != progress_percentage_previous:
                print(F"{progress_percentage}% of catagorization process completed")

            # for each line, the values are read and split, after which they are merged with the earlier determined header to make a dictionary
            values = line.strip().split(";")
            commute = dict(zip(header, values))

            # in the file, al things are strings, some things need to be floats/ intergers for further processing, and some things need to be datetime objects:
            commute["month"] = int(commute["month"])
            commute["day_type"] = int(commute["day_type"])
            commute["pickup_time"] = datetime.strptime(commute["pickup_time"],"%H:%M:%S").time()
            commute["dropoff_time"] = datetime.strptime(commute["dropoff_time"],"%H:%M:%S").time()
    
            # now that a single yourney is defined with al data points needed, the month is changed into an actual month
            match commute["month"]:
                case 1:
                    commute["month"] = "january"
                case 2:
                    commute["month"] = "february"
                case 3:
                    commute["month"] = "march"
                case 4:
                    commute["month"] = "april"
                case 5:
                    commute["month"] = "may"
                case 6:
                    commute["month"] = "june"
                case 7:
                    commute["month"] = "july"
                case 8:
                    commute["month"] = "august"
                case 9:
                    commute["month"] = "september"
                case 10:
                    commute["month"] = "october"
                case 11:
                    commute["month"] = "november"
                case 12:
                    commute["month"] = "december"

            #finally everything can be catogarized into the correct list
            # first, al yourneys started in 2024 are removed
            if "2024" in commute["date"]:
                pass

            # first see if it is a rush hour commute
            elif (time(16, 0) <= commute["pickup_time"]<= time(20, 0) and 
                    time(16, 0) <= commute["dropoff_time"] <= time(20, 0) and 
                    commute["day_type"] in range(0, 5)):

                class_name = str(commute["month"] + "_rush")
                lists[class_name].append(commute)
            
            #next, we see if it is a overnight commute
            elif ((time(20, 0) <= commute["pickup_time"]  or commute["pickup_time"] <= time(6, 0) )and
                    (time(20, 0) <= commute["dropoff_time"] or commute["dropoff_time"] <= time(6, 0)) and
                    commute["day_type"] in range(0, 7)):
                
                class_name = str(commute["month"] + "_overnight")
                lists[class_name].append(commute)

            #next, we see if it is a normal commute
            elif (time(6, 0) <= commute["pickup_time"] <= time(20, 0) and 
                    time(6, 0) <= commute["dropoff_time"] <= time(20, 0) and
                    commute["day_type"] in range(0, 7)):
                
                class_name = str(commute["month"] + "_standard")
                lists[class_name].append(commute)

            else:
                nonvalid.append(commute)

            progress += 1
    print(F"{len(nonvalid)}nonvallid commutes detected")
    print("catagorization process complete")
    return lists, nonvalid

