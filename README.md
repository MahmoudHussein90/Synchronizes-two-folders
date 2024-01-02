# Synchronizes-two-folders
Synchronizes two folders by using Python
# Folder Synchronization Script

## Overview
This Python script synchronizes files between two folders, ensuring that the replica folder is an exact mirror of the source folder. It uses MD5 checksums to detect changes in files and includes logging for tracking operations.

## Features
- *File Synchronization*: Keeps two directories in sync.
- *MD5 Checksum Validation*: Identifies file changes.
- *Logging*: Documents operations like file copying, updating, and deletion.
- *Periodic Sync*: Runs at specified intervals to maintain synchronization.

## Installation
Clone the repository:

git clone https://github.com/MahmoudHussein90/Synchronizes-two-folders.git

Navigate to the script's directory.

## Usage
Run the script from the command line:
python sync_folders.py <source_folder> <replica_folder> --interval <seconds> --log <log_file>
- <source_folder>: Path of the source folder.
- <replica_folder>: Path of the replica folder.
- <seconds>: Sync interval in seconds.
- <log_file>: Path to the log file.

Example:
python Sync two folders-one way.py /path/to/source /path/to/replica --interval 5 --log sync.log


## Functionality
- Replicates the structure and files of the source directory in the replica directory.
- Compares files based on MD5 checksum.
- Removes files and directories from the replica that are no longer in the source.
- Logs all operations.
