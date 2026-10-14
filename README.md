# New_york_Taxi_data_analyses

This programm looks into New_York_taxi's open data set to answer 2 research question


## Research quetion

- question 1: When is it most expensive to take a taxi in New york, and by how much?
- question 2: Does the price/kilometer depend on the month?


## Features

- in terminal build menu to choose specific features to run
- programm that analyses the data from New_york_taxi's open data set in order to answer both research questions
- cleanup_tool that removes al new files created during the analyses


## Installation and Setup

### Prerequisites
To run this code, you will need:
- Python
- pip (Python package manager)
- inquirer 3.4.1
- matplotlib 3.11.2
- numpy 2.5.4
- pandas 3.0.6

__--> python packages used in the code include__ 
- numpy
- ABC imported from abc
- datetime, time imported from datetime
- pandas
- matplotlib.pyplot
- os
- Path imported from pathlib
- inquirer
- time

### Setup
**__1. Clone the repository__**

   git clone https://github.com/JoepGaming/Project_New_york_Taxi_data_analyses.git

   cd Physics-coding-project
   
**__2. install external packages__**
   
   run pip install -r requirements.txt in the terminal to install al external packages needed to run the programm
   
**__3. upload data to programm__**

   (This step may be skipped because the data is already available in the data_og folder)

   visit the New York city open data website (NYC Open Data) and look for 2025 Green Taxi Trip Data. This can also be found using the link provided in the sources part below.
   export the data without applying any filters, the programm does this automatically
   save the data in the data_og folder as:
   2025_Green_Taxi_Trip_Data_20260930.csv

**__4. run programm__**
   
   in visual studio code (or other used programm), navigate to the file called controll_desk.py and run this file. you should see a option menu pop up in the terminal after a few seconds. Navigate to the option preform_analyses using the arrow keys. next press enter. the analyses should now begin

**__5. were to find the results__**

   When the programm says "data analysis process complete", navigate to the data_new folder. In here, a filtered version of the input data, and 7 plots are found of which 5 can be used for answering the research questions

**__6. cleanup (optional)__**

   when the analyses is finished, you wil be represented with the option menu again. If you want to clean up your device from al created files, navigate to the option "delete created files" and press enter, after a question to check if you are sure you want to delete al created files, the programm wil delete al created files from your device. if the programm could not succeed at this, it wil tell in the terminal

**__7. stop programm__**

   Finally to stop the programm, in the option menu, navigate to "stop programm" and press enter. the programm wil now be stopped


## Sources:
data used in the analyses can be found at:
https://data.cityofnewyork.us/Transportation/2025-Green-Taxi-Trip-Data/nkud-f3se/about_data



## Authors:
Joep Drugmand

## Contact:
j.drugmand@student.maastrichtuniversity.nl
