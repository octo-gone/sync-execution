import os
import configparser
import json

config = configparser.ConfigParser()

if not os.path.exists("./settings.ini"):
    config["Sync Modules"] = {
        "modules": json.dumps([
            "./modules/control",
            "./modules/inout",
            "./modules/memory",
            "./modules/construction",
            "./modules/logic",
            "./modules/misc",
            "./modules/mathematic",
            "./modules/struct",
            "./modules/unit_testing",
            "./modules/user_nodes"
        ])
    }
    config["Console"] = {
        "iteration": "yes",
        "additional_info": "yes",
        "colored": "yes",
        "log_warning": "yes"
    }
    with open('./settings.ini', 'w') as configfile:
        config.write(configfile)

config.read("./settings.ini")
