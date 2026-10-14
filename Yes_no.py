import inquirer

def Yes_no():
    Yes_no_run = [
        inquirer.List(
            "YN",
            message = "",
            choices = ["yes", "no"],
        ),
    ]

#debugging option chooser function caller
    yes_or_no = inquirer.prompt(Yes_no_run)
    match yes_or_no["YN"]:
        case "yes":
            return True
        case "no":
            return False