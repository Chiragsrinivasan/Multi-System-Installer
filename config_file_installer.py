import datetime
import glob
import json
import logging
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from file_transfer import *

pool = ThreadPoolExecutor(10)
def install_files(filenames):
    
    success = True
    for filename in filenames:
        try:
            pool.submit(send, filename)
            logging.info(f"Installed {filename} successfully")
        except subprocess.CalledProcessError:
            logging.error(f"Error installing {filename}")
            success = False
    return success


def schedule_installation(config):
   
    system_name = config.get("system_name", "unknown")
    action = config.get("action", "unknown")
    filenames = config.get("filenames", [])
    scheduled_time = datetime.datetime.fromisoformat(config["datetime"])
    
    logging.info(f"Scheduling {action} of {len(filenames)} files on {system_name} at {scheduled_time}")
    
    while datetime.datetime.now() < scheduled_time:
        # Wait until the scheduled time is reached
        time.sleep(1)
    
    success = install_files(filenames)
    if success:
        logging.info(f"{action} of {len(filenames)} files on {system_name} completed successfully")
    else:
        logging.error(f"Error during {action} of {len(filenames)} files on {system_name}")


if __name__ == "__main__":
    logging.basicConfig(filename="install.log", level=logging.INFO)
    
    config_folder = "/path/to/config/folder"
    done_folder = "/path/to/done/folder"
    
    if not os.path.exists(done_folder):
        os.makedirs(done_folder)
    
    while True:
        config_files = glob.glob(os.path.join(config_folder, "*.json"))
        
        for config_file in config_files:
            with open(config_file) as f:
                config = json.load(f)
            
            try:
                schedule_installation(config)
                shutil.move(config_file, os.path.join(done_folder, os.path.basename(config_file)))
            except Exception as e:
                logging.exception(f"Unhandled exception during installation: {e}")
        
        # Wait for a certain amount of time before checking for new config files again
        time.sleep(10)
