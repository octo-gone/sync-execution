import os
import configparser
import json

config = configparser.ConfigParser()

if not os.path.exists("./settings.ini"):
    config["Sync Modules"] = {
        "folders": json.dumps([
            "./modules",
            "./scripts/nodes/modules"
        ]),
        "files": json.dumps([])
    }
    config["Console"] = {
        "colored_console": "yes",
        "show_iteration": "yes",
        "show_additional_info": "yes",
        "show_warning": "yes",
        "use_fileopen_dialog": "yes"
    }
    with open('./settings.ini', 'w') as configfile:
        config.write(configfile)

config.read("./settings.ini")
