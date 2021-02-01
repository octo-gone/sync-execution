import json
import os
import inspect
import importlib.util
from scripts.utils import logger
from scripts.nodes import base
from scripts.config import config

node_aliases = {}
module_files = []
module_folders = []
try:
    module_files = json.loads(config.get("Sync Modules", "files"))
except json.decoder.JSONDecodeError as e:
    logger.log_warning("wrong 'files' setting syntax in 'settings.ini'")
try:
    module_folders = json.loads(config.get("Sync Modules", "folders"))
except json.decoder.JSONDecodeError as e:
    logger.log_warning("wrong 'folders' setting syntax in 'settings.ini'")


def add_module(module_file):
    if not os.path.exists(module_file):
        logger.log_warning(f"module \"{module_file}\" not found")
    else:
        spec = importlib.util.spec_from_file_location(".".join(module_file.split(".py")[0].split("/")), module_file)
        loaded_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(loaded_module)
        m = inspect.getmembers(loaded_module, inspect.isclass)
        for node_class_name, node_class in m:
            if base.Node in node_class.__bases__:
                for alias in node_class.aliases:
                    node_aliases[alias] = node_class


folder_module_files = []
for folder in module_folders:
    for dir_path, dir_names, filenames in os.walk(folder):
        py_files = filter(lambda x: x.endswith(".py"), filenames)
        for filename in py_files:
            folder_module_files.append(os.path.join(dir_path, filename))

for file in module_files + folder_module_files:
    file = file if file.endswith(".py") else file + ".py"
    add_module(file)
