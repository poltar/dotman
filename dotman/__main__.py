#!/usr/bin/env python3

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

    wd = os.path.abspath(os.getcwd())

    #switchfile is fucked, fix it 
    switchfile = os.path.abspath(str(wd) + "/" + args.switch)
    backupdir = os.path.abspath(os.environ['HOME'] + "/.dotman/" + args.backup)

    if os.path.isfile(backupdir):
        print ("ERROR: Backup directory is file")
        exit(1)

    copyobj = copy.Copy()

    #fix this stuff too
    if not ((args.switch == "") and (args.backup == "")):
        copyobj.copy_from_config(backupdir, args.name)
        copyobj.copy_to_config(switchfile)
    elif not args.switch == "":
        copyobj.copy_to_config(switchfile)
    elif not args.backup == "":
        copyobj.copy_from_config(backupdir, args.name)


def define_args():
    parser = argparse.ArgumentParser(description="Save and swap out config files in your config directory")

    parser.add_argument('--switch', type=str, metavar="\"/path/to/file\"", help="Swap out the current config file for the file specified")

    parser.add_argument('--backup', type=str, metavar="programtobackup", help="Backup the current config file for the program given to $HOME/.dotman - must be used with --name")

    parser.add_argument('--name', type=str, metavar="newname", help="Name to use for the backup file - must be used with --backup")

    parser.add_argument('--version', action="store_true")

    return parser.parse_args()


if __name__ == "__main__":
    main()