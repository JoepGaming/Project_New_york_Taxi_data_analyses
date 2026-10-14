import Yes_no
import os
from pathlib import Path as path

def clean(file_names, workdir):
    print("are you sure you want to remove al files created in this analyses?")
    if Yes_no.Yes_no():
        if len(file_names) == 0:
            print("warning, there are no file names saved\n pleas run the analyeses again and then select the cleanup tool \n this wil overwrite existing files and put them in the list")

        for file in file_names:
            file_path = workdir / "data_new" / file
            if os.path.exists(str(file_path)):
                os.remove(str(file_path))
                print(F"{str(file)} succesfully deleted")
            
            else:
                print(F"{str(file)} supposedly located at {str(file_path)} could not be removed by the programm")
        return