import configparser
import importlib.util
from scripts.utils import logger
from scripts.nodes import base
import json
import os
import inspect

node_aliases = {}
config = configparser.ConfigParser()
config.read("./settings.ini")
modules = json.loads(config.get("Sync Modules", "modules"))

for module in modules:
    module = module if module.endswith(".py") else module + ".py"

    if not os.path.exists(module):
        logger.log_warning(f"module \"{module}\" not found")
        continue

    spec = importlib.util.spec_from_file_location(".".join(module.split(".py")[0].split("/")), module)
    loaded_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded_module)
    m = inspect.getmembers(loaded_module, inspect.isclass)
    for node_class_name, node_class in m:
        if base.Node in node_class.__bases__:
            for alias in node_class.aliases:
                node_aliases[alias] = node_class
