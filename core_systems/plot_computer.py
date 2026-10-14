import matplotlib.pyplot as plt
import numpy as np


def compute_plot(_means_per_month_type, _stdevs_per_month_type, _uncertaintys_per_month_type, _means_per_class, _stdevs_per_class, _uncertaintys_per_class, lists, classes, workdir, file_names):
    print("initiating plotting computation process")

    """ 
        for the most clear representation of the data, 4 plots are created
        3 of them show a class for each month and the calculated values for it
        the forth one shows everything in one plot
    """

    # first define al months in a list for the x axis
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

    # next, the data of al classes is plotted 
    """#####################################################################################################################"""
    # initiate index number i which is used to save the plots as plt.show wil not be used, but rather al plots wil be saved
    i = 1
    for classs in classes:

        print("creating new plot")
        fig, axes = plt.subplots(figsize = (10, 6))

        # create lists containing the mean and standard deviation for every month of the current class
        means = []
        stdevs = []
        uncertaintys = []

        for month in months:
            name = month + "_" + classs

            means.append(_means_per_month_type[name])
            stdevs.append(_stdevs_per_month_type[name])
            uncertaintys.append(_uncertaintys_per_month_type[name])

        print(F"building plot{i}")

        for month, mean, stdev, uncertainty in zip(months, means, stdevs, uncertaintys):

            # determine color
            colors = {"standard":"blue", "rush":"red", "overnight":"purple"}
                  
            if "standard" in classs:
                color = colors["standard"]
            elif "rush" in classs:
                color = colors["rush"]
            elif "overnight" in classs:
                color = colors["overnight"]
                

            # put data in plot
            axes.errorbar(month, mean, stdev, fmt="o", linewidth=2, capsize=5, label = classs, color = color)
            # put values at dat points
            axes.annotate(f"{mean:.2f}\n±{uncertainty:.2f}", (month, mean), textcoords="offset points", xytext=(20, 8), ha="center" ) # line by Ai

        # configure customisables for plot
        print("applying customiziations")

        axes.set_title(f"{classs} price/kilometer over months")
        axes.set_xlabel("months")
        axes.set_ylabel("price/kilometer")
        axes.grid(True)
        plt.xticks(rotation=45) # line made by Ai

        fig.savefig(workdir / "data_new" / f"plot_{i}.png")
        file_names.append(F"plot_{i}.png")

        print(f"plot_{i} finished")

        i += 1

    
    
    
    
    
    
    
    
    
    # next create the plot with just the 3 types and the mean + stdev
    """#######################################################################"""
    
    print("creating new plot")
    fig, axes = plt.subplots(figsize = (5, 6))

    # create lists containing the mean and standard deviation for every month of the current class
    means = []
    stdevs = []
    uncertaintys = []
    
    for classs in classes:
        means.append(_means_per_class[classs])
        stdevs.append(_stdevs_per_class[classs])
        uncertaintys.append(_uncertaintys_per_class[classs])

    print(F"building plot{i}")

    for classs, mean, stdev, uncertainty in zip(classes, means, stdevs, uncertaintys):

        # set different colors for different types
        colors = {"standard":"blue", "rush":"red", "overnight":"purple"}
      
        if "standard" in classs:
            color = colors["standard"]
        elif "rush" in classs:
            color = colors["rush"]
        elif "overnight" in classs:
            color = colors["overnight"]
    
        # put data in the plot
        axes.errorbar(classs, mean, stdev, fmt="o", linewidth=2, capsize=5, color = color) # line wiyh help of Ai
        
        #display numbers by the data points
        axes.annotate(f"{mean:.2f}\n±{uncertainty:.2f}", (classs, mean), textcoords="offset points", xytext=(20, 8), ha="center" ) # line by Ai

    # configure customisables for plot
    print("applying customiziations")

    axes.set_title("price/kilometer for each class")
    axes.set_xlabel("class")
    axes.set_ylabel(" mean price/kilometer")
    axes.grid(True)
    plt.xticks(rotation=45) # line made by Ai

    fig.savefig(workdir / "data_new" / f"plot_{i}.png")
    file_names.append(F"plot_{i}.png")

    print(f"plot_{i} finished")

    i += 1














    # and create a plot with al types and moths in 1 single plot
    """####################################################################"""
    print("creating new plot")
    fig, axes = plt.subplots(figsize = (36, 16))

    # create lists containing the mean and standard deviation for every month of the current class
    means = []
    stdevs = []
    uncertaintys = []
    
    for list_name in lists: # we use list_name in this part because it otherwise interferes with the build in list functionality
        means.append(_means_per_month_type[list_name])
        stdevs.append(_stdevs_per_month_type[list_name])
        uncertaintys.append(_uncertaintys_per_month_type[list_name])


    

    print(F"building plot{i}")

    
    for list_name, mean, stdev, uncertainty in zip(lists.keys(), means, stdevs, uncertaintys):
        
        # set different colors for different types
        colors = {"standard":"blue", "rush":"red", "overnight":"purple"}
  
        if "standard" in list_name:
            color = colors["standard"]
        elif "rush" in list_name:
            color = colors["rush"]
        elif "overnight" in list_name:
            color = colors["overnight"]

        # apply data to the plot
        axes.errorbar(list_name, mean, stdev, fmt="o", linewidth=2, capsize=5, color = color) # line wiyh help of Ai

        # put the mean +- uncertainty at the data point for extra clarity
        axes.annotate(f"{mean:.2f}\n±{uncertainty:.2f}", (list_name, mean), textcoords="offset points", xytext=(20, 8), ha="center", fontsize = 14, color = color) # line by Ai

    # configure customisables for plot
    print("applying customiziations")

    axes.set_title("price/kilometer for each month and class", fontsize = 20)
    axes.set_xlabel("month_class", fontsize = 14)
    axes.set_ylabel("mean price/kilometer", fontsize = 16)
    axes.grid(True)
    axes.legend()
    plt.xticks(rotation=45) # line made by Ai
    plt.tick_params(axis = "both", labelsize = 14)

    fig.savefig(workdir / "data_new" / f"plot_{i}.png")
    file_names.append(F"plot_{i}.png")

    print(f"plot_{i} finished")

    i += 1


    print("plotting computation process complete")
    return file_names










# here is the plot that shows the raw data
"""###############################################################################"""
def data_raw_plot(lists, file_names, workdir, i):
    # this plot is not part of the final analyses but an inbetween plot to test something
    print("creating new plot")

    fig, axes = plt.subplots(figsize=(36,15))

    # again initiate a progress bar since the progress takes a while

    progress = 0
    progress_percentage = 0
    progress_end_at = sum(len(list) for list in lists.values())
    #show al price/kilometer values in a scatter plot
    print(F"building plot_raw_data_{i} data")

    # initialise empty lists for the data for the plot to be stored in
    x_values = []
    y_values = []
    for key, commutes in lists.items():
        for commute in commutes:
            #calculate an optionally display the progress made:
                        
            progress_percentage_previous = progress_percentage
            progress_percentage = int(progress/progress_end_at*100) 

            # if the amount of progress has changed, this is printed to the user
            if progress_percentage != progress_percentage_previous:
                print(F"{progress_percentage}% of plotting process completed")

            x_values.append(key)
            y_values.append(commute["price/kilometer"])

            progress += 1

    print("applying data to the plot")
    axes.scatter(x_values, y_values, marker="o")
    
    # configure customisables for plot
    print("applying customiziations")

    plt.title("price/kilometer for each month and class", fontsize = 20)
    plt.xlabel("month_class", fontsize = 14)
    plt.ylabel("price/kilometer", fontsize= 16)
    plt.grid(True)
    plt.xticks(rotation=45) # line made by Ai
    plt.tick_params(axis = "both", labelsize = 14)
    plt.savefig(workdir / "data_new" / f"plot_raw_data{i}.png")
    
    file_names.append(F"plot_raw_data{i}.png")

    print(f"plot_raw_data_{i} finished")

    return file_names