from pathlib import Path as path
from core_systems import file_converter, catorization, calculations, plot_computer
import time

"""
satppenplan voor hoe data te analyseren

- uitlezen wat ik nodig heb
- gegevens omzetten naar SI eenheden
- gegevens splisten in maanden
- gegevens splitsen in spits vs non spits vs nacht
- berekeningen maken
- mean, stdev etc. berekenen over de berekende data.
- uitzetten in een plot

"""


def manager():
    # first, record the time the analyses was initiated
    start_time = time.perf_counter()

    print("data analysis process initiated")
    # preform al steps in the correct order by calling correct functions and correct files
    # first determine were this file, and therefore al other files are located in the system
    workdir = path(__file__).resolve().parent 
    
    # start with reading the green taxi data file, and making a new file with only the coloms needed
    file_names = file_converter.convert(workdir)

    # next put each data entry in the correct list 
    lists, nonvalid = catorization.catogarize(workdir)

    # then we can make calculations over al these entries
    _means_per_month_type, _stdevs_per_month_type, _uncertaintys_per_month_type, _means_per_class, _stdevs_per_class, _uncertaintys_per_class, classes, nonvalid, file_names = calculations.calculate(lists, nonvalid, file_names, workdir)


    """##############################"""
    end_time = time.perf_counter()
    print(F"calculasion and previous completed in {(end_time-start_time):.2f} seconds or {((end_time-start_time)/60):.2f} minutes")

    """#####################"""


    # finally, everything can be desplayed in a plot
    file_names = plot_computer.compute_plot(_means_per_month_type, _stdevs_per_month_type, _uncertaintys_per_month_type, _means_per_class, _stdevs_per_class, _uncertaintys_per_class, lists, classes, workdir, file_names)

    #record the end time and calculate + show how long analyses took
    end_time = time.perf_counter()
    print(F"analyses completed in {(end_time-start_time):.2f} seconds or {((end_time-start_time)/60):.2f} minutes")

    print("data analysis process complete")

    return file_names, workdir