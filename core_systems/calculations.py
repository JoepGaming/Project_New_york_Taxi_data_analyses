"""""" "date", "day", "month", "day_type", "pickup_time", "dropoff_time", "distance", "kost"
import numpy as np
from core_systems import plot_computer
def calculate(lists, nonvalid, file_names, workdir):
    
    # first calculation is about the main research question, which is kost over distance traveled
    print("initiating calculations process")
    print("calculating price/kilometer")
    # create a list with nonvalid commutes that are detected in this next step. this list wil later be used to remove these commutes
    nonvalid_commutes = []

    # the progress bar is also used again
    progress = 0
    progress_percentage = 0
    progress_end_at = sum(len(list) for list in lists.values())

    # now actually make the calculation
    print("calculating price / kilometer")

    for list in lists.values():
       

        for commute in list:

            #calculate an optionally display the progress made:
            
            progress_percentage_previous = progress_percentage
            progress_percentage = int(progress/progress_end_at*100) # 591485 is the theoretical amount of lines in the taxi_data file

            # if the amount of progress has changed, this is printed to the user
            if progress_percentage != progress_percentage_previous:
                print(F"{progress_percentage}% of calculation process completed")
            
            # first capture al errors and put them away
            if commute["distance"] == "" or float((commute["distance"]).replace(",","")) == 0:
                nonvalid.append(commute)
                nonvalid_commutes.append(commute)
            elif commute["kost"] == "" or float((commute["kost"]).replace(",","")) == 0:
                nonvalid.append(commute)
                nonvalid_commutes.append(commute)
            else:
                # turn strings into needed type
                commute["distance"] = float((commute["distance"]).replace(",",""))
                commute["kost"] = float((commute['kost']).replace(",",""))

                # calculate the kilometer kost and at it to the commute
                commute["price/kilometer"] = float(commute["kost"]/commute["distance"])
            
            progress += 1



    # now that every commute has been checked for a distance, the ones with no distance are removed from the list
    print("removing nonvalid commutes")

    progress = 0
    progress_percentage = 0
    progress_end_at = len(lists) * len(nonvalid_commutes)

    
    for list in lists.values():
        for commute in nonvalid_commutes:
            #calculate an optionally display the progress made:
                        
            progress_percentage_previous = progress_percentage
            progress_percentage = int((progress/progress_end_at)*100) # 591485 is the theoretical amount of lines in the taxi_data file

            # if the amount of progress has changed, this is printed to the user
            if progress_percentage != progress_percentage_previous:
                print(F"{progress_percentage}% of removal process completed")
            
            if commute in list:
                list.remove(commute)

            progress += 1

    print("removal complete")

    # the rest of the data is displayed in a plot to see if there are values that are unreasonably high, and where this group starts
    i = 1
    plot_computer.data_raw_plot(lists, file_names, workdir, i)
    i += 1

    # from the plot, it can be found that some datapoints are aplicable to be considered faulty, these will first be put in the list of non_valid
    # and nonvalid_commutes, and then be removed from the dataset

    progress = 0
    progress_percentage = 0
    progress_end_at = sum(len(list) for list in lists.values())
    
    for list in lists.values():
       

        for commute in list:

            #calculate an optionally display the progress made:
            
            progress_percentage_previous = progress_percentage
            progress_percentage = int(progress/progress_end_at*100) # 591485 is the theoretical amount of lines in the taxi_data file

            # if the amount of progress has changed, this is printed to the user
            if progress_percentage != progress_percentage_previous:
                print(F"{progress_percentage}% of re-evaluating process completed")
            
            # again capture al errors and put them away
            if commute["price/kilometer"] >= 100 or commute["price/kilometer"] <= 0:
                nonvalid.append(commute)
                nonvalid_commutes.append(commute)

            progress += 1

    # and again remove the nonvalid ones
    print("removing more nonvalid commutes")

    progress = 0
    progress_percentage = 0
    progress_end_at = len(lists) * len(nonvalid_commutes)

    
    for list in lists.values():
        for commute in nonvalid_commutes:
            #calculate an optionally display the progress made:
                        
            progress_percentage_previous = progress_percentage
            progress_percentage = int((progress/progress_end_at)*100) # 591485 is the theoretical amount of lines in the taxi_data file

            # if the amount of progress has changed, this is printed to the user
            if progress_percentage != progress_percentage_previous:
                print(F"{progress_percentage}% of secondary removal process completed")
            
            if commute in list:
                list.remove(commute)

            progress += 1

    print("secondary removal complete")
    
    print(f"{len(nonvalid_commutes)} commutes were detected by the system and removed from the data set")

    # create another plot to see if the data is correct now and then continue

    plot_computer.data_raw_plot(lists, file_names, workdir, i)

    # from this point, data is actually being process-wise calculated
    """###############################################################################################################################################"""
    """###############################################################################################################################################"""
    """###############################################################################################################################################"""
    
    # next part calculates the means, stdevand uncertaintys for al month_types (example mean_januari_rush) 
    # ofcourse create the empty dictionaries first
    means_per_month_type = {}
    stdevs_per_month_type = {}
    uncertaintys_per_month_type ={}
    print("calculating means and stdevs of month_type variant")

    for name, list in lists.items():
        # first extract al the price / kilometer values from the dictionaries
        
        price_per_km_temp = []
        for commute in list:
            price_per_km_temp.append(commute["price/kilometer"])

        # turn the data into a list of subsamples
        sub_samples = np.array_split(price_per_km_temp, 100)
        

        # next calculate the mean and save this in the dictionarry of means
        _mean = np.mean([np.mean(subsample) for subsample in sub_samples ])
        means_per_month_type[str(name)] = _mean

        # for the uncertainty, take the stdev of the subsamples means

        _uncertainty = np.std([np.mean(subsample) for subsample in sub_samples ])
        uncertaintys_per_month_type[str(name)] = _uncertainty

        # next calculate the standard deviation and save 
        _stdev = np.std(price_per_km_temp)
        stdevs_per_month_type[str(name)] = _stdev

        
        
    print("calculation complete")
    # because these dictionaries are going to be used in the plot, they wil be coppied to a protect version
    # this version starts with _
    # this doesn't realy do anything literally in the sense of security, but rather is a convention
    # might be over kill, but better to be safe then sorry

    _means_per_month_type = means_per_month_type
    _stdevs_per_month_type = stdevs_per_month_type
    _uncertaintys_per_month_type = uncertaintys_per_month_type

    print("month_type data secured")

    """ now to calculate the means, stdevs etc. for the different classes (standard, night, and rush) """ 
    # first make a new version of lists called classes were the data is organized by class

    classes = {"standard": [], "rush": [], "overnight": []}    

    # put data in correct list
    print("rearranging month_type's into classes of type's")
    for name, list in lists.items():
        if "standard" in str(name):
            classes["standard"].append(list)
        elif "rush" in str(name):
            classes["rush"].append(list)
        elif "overnight" in str(name):
            classes["overnight"].append(list)
                
    # now do the necessairy calculations again to extract mean, stdev, etc.

    means_per_class = {}
    stdevs_per_class = {}
    uncertaintys_per_class = {}
   
    print("calculating means and stdevs of classs variant")
    for classs in classes:
        # first extract al the price / kilometer values from the dictionaries

        price_per_km_temp = []
        for month in classes[classs]:
            for commute in month:
                price_per_km_temp.append(commute["price/kilometer"])


        # turn the data into a list of subsamples
        sub_samples = np.array_split(price_per_km_temp, 100)

        # next calculate the mean and save this in the dictionarry of means
        _mean = np.mean([np.mean(subsample) for subsample in sub_samples ])
        means_per_class[str(classs)] = _mean

        # for the uncertainty, take the stdev of the subsamples means

        _uncertainty = np.std([np.mean(subsample) for subsample in sub_samples ])
        uncertaintys_per_class[str(classs)] = _uncertainty

        # next calculate the standard deviation and save 
        _stdev = np.std(price_per_km_temp)
        stdevs_per_class[str(classs)] = _stdev

    # again copy the data to a secure file
    _means_per_class = means_per_class
    _stdevs_per_class = stdevs_per_class
    _uncertaintys_per_class = uncertaintys_per_class
    print("classs data secured")

    print("calculation process complete")
    return _means_per_month_type, _stdevs_per_month_type, _uncertaintys_per_month_type, _means_per_class, _stdevs_per_class, _uncertaintys_per_class, classes, nonvalid, file_names