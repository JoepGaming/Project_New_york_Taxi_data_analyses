import pandas as pd


def convert(workdir):
    print("initiating convertion process")
    # set the location of the input data and output data first
    input_data = workdir / "data_og" / "2025_Green_Taxi_Trip_Data_20260930.csv"
    output_data = workdir / "data_new" / "2025_Green_Taxi_Trip_Data_used.csv"
    print("all files found and created")
    # prepare the index for the new file
    header = pd.DataFrame(columns=["date", "day", "month", "day_type", "pickup_time", "dropoff_time", "distance", "kost"])
    header.to_csv(output_data, sep=";", index=False)

    #also put the name of this new file in the file_names lists so it can ebe found and deleted easily afterwards
    file_names = ["2025_Green_Taxi_Trip_Data_used.csv"]

    # now that the file has been located, read the data from it and do necessery customizations
    data_frame = pd.read_csv(input_data, sep=",", low_memory=False)

    # first, split up the pickup dates and times and make extra statements for later use ( AI was used in this part for sertain commands around pandas)
    #statements for days
    print("converting dates")
    data_frame["lpep_pickup_datetime"] = pd.to_datetime( data_frame["lpep_pickup_datetime"], format="%m/%d/%Y %I:%M:%S %p" )
    data_frame["date"] = data_frame["lpep_pickup_datetime"].dt.date
    data_frame["day"] = data_frame["lpep_pickup_datetime"].dt.day
    data_frame["month"] = data_frame["lpep_pickup_datetime"].dt.month

    data_frame["day_type"] = data_frame["lpep_pickup_datetime"].dt.dayofweek
                
    #statements for times
    print("converting times")
    data_frame["lpep_dropoff_datetime"] = pd.to_datetime( data_frame["lpep_dropoff_datetime"], format="%m/%d/%Y %I:%M:%S %p" )
    data_frame["pickup_time"] = data_frame["lpep_pickup_datetime"].dt.time
    data_frame["dropoff_time"] = data_frame["lpep_dropoff_datetime"].dt.time

    # translate the distance from miles to kilometers
    print("converting distance")
    data_frame["distance"] = (pd.to_numeric(data_frame["trip_distance"],errors="coerce"))*1.60934

    # copy the cost
    print("converting kosts")
    data_frame["kost"] = data_frame["total_amount"]

    # keep only created coloms in data_frame
    final_output = data_frame[["date", "day", "month", "day_type", "pickup_time", "dropoff_time", "distance", "kost"]]

    # and write this to the newly created file which is first wiped clean to speed up the process
    print("creating new data file")
    final_output.to_csv(output_data, sep=";", index=False, header = False, mode = "a")

    print("convertion process complete")
    return file_names