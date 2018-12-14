import argparse
import os

from . import copy

#TODO: Add ability to backup to github repo

__version__ = "0.1.0"

def main():
    args = define_args()

    if args.version:
        print ("dotman v" + __version__)
        exit(0)

    wd = os.getcwd()

    if (args.switch == "") and (args.backup == ""):
        backupthencopy(args.switch, args.backup, args.name)

def backupthencopy(filetoswitch, filetobackup, nameforbackup):
    pass


def define_args():
    parser = argparse.ArgumentParser(description="Save and swap out config files in your config directory")

    parser.add_argument('--switch', type=str, metavar="\"/path/to/file\"", help="Swap out the current config file for the file specified")

    parser.add_argument('--backup', type=str, metavar="programtobackup", help="Backup the current config file for the program given to $HOME/.dotman - must be used with --name")

    parser.add_argument('--name', type=str, metavar="newname", help="Name to use for the backup file - must be used with --backup")

    parser.add_argument('--version', action="store_true")

    return parser.parse_args()


if __name__ == "__main__":
    main()