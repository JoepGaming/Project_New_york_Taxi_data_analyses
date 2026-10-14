# from __future__ import annotations
import inquirer
import data_analyses_manager
import cleanup_tool



# start with the initialization of some variables and sets needed throughout the entirety of the analyses
Debugging = False
file_names = []
workdir = ""



# menu for everything this programme can do, and choosing which one you want to preform
options = [
    inquirer.List(
        "exercise",
        message = "What would you like to do? (navigate this menu with arrow keys)",
        choices = ["preform_analyses","delete created files", "stop programm"],
    ),
]


while True:
    answer = inquirer.prompt(options)
    match answer["exercise"]:

        case "preform_analyses":
            file_names, workdir = data_analyses_manager.manager()

        case "delete created files":
            cleanup_tool.clean(file_names, workdir )


        case "stop programm":
            print(" Have a nice day !!!")
            break