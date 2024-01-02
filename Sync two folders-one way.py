import hashlib
import os
import argparse
import logging
import shutil
import time
from hashlib import md5
from shutil import copy2, rmtree


def calc_md5(file_path):
    """
    Function to calculate the MD5 checksum of a file.
    :param file_path: str - Path of the file.
    :return: str - MD5 checksum of the file.
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def sync_folders(source, replica):
    """
    Function to synchronize two directories
    :param source: str - Path of the source folder.
    :param replica: str - Path of the replica folder.
    :return: none
    """
    source = os.path.abspath(source)
    replica = os.path.abspath(replica)

    for src_dir, dirs, files in os.walk(source):
        # This code is making replica directory in case if it doesn't exist.
        replica_dir = src_dir.replace(source, replica)
        if not os.path.exists(replica_dir):
            os.makedirs(replica_dir)

        # Copy/update files
        for file in files:
            src_file = os.path.join(src_dir, file)
            replica_file = os.path.join(replica_dir, file)
            if not os.path.exists(replica_file) or calc_md5(src_file) != calc_md5(replica_file):
                shutil.copy2(src_file, replica_file)
                logging.info(f"File copied/updated: {src_file}")
                print(f"File copied/updated: {src_file}")

        # Remove files not present in source
        for file in os.listdir(replica_dir):
            replica_file = os.path.join(replica_dir, file)
            src_file = os.path.join(src_dir, file)
            if not os.path.exists(src_file):
                os.remove(replica_file)
                logging.info(f"File removed: {replica_file}")
                print(f"File removed: {replica_file}")

        # Clean up directories that no longer exist in source
        for dir in dirs:
            replica_subdir = os.path.join(replica, dir)
            src_subdir = os.path.join(src_dir, dir)
            if not os.path.exists(src_subdir):
                shutil.rmtree(replica_subdir)
                logging.info(f"Directory removed: {replica_subdir}")
                print(f"Directory removed: {replica_subdir}")


# Set up argument parser
parser = argparse.ArgumentParser(description="Synchronize two folders.")
parser.add_argument("source", help="Source folder path")
parser.add_argument("replica", help="Replica folder path")
parser.add_argument("--interval", type=int, required=True, help="Synchronization interval in seconds")
parser.add_argument("--log",required=True, help="Log file path", default="sync.log")

# Parse arguments
args = parser.parse_args()

# Set up logging
logging.basicConfig(filename=args.log, level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger("").addHandler(console)

# Main loop to periodically sync folders
while True:
    sync_folders(args.source, args.replica)
    time.sleep(args.interval)
