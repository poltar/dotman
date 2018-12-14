import os
from shutil import copyfile

class Copy:
    def _get_parent_directory(self, path):
        os.chdir(path)
        return os.path.abspath(os.pardir)

    #copy config file from $HOME/.dotman to config (to swap config files)
    def copy_to_config(self, backup_file): 
        config_dir = os.path.abspath(os.environ['HOME'] + "/.config/" + str(backup_file).split('/')[-1])

        #fix this because not every program uses a file named 'config' by default
        copyfile(backup_file, os.path.abspath(str(config_dir) + "config"))

    #copy config file from config dir to $HOME/.dotman (to backup and save config files)
    def copy_from_config(self, config_file, newname):
        backup_dir = os.path.abspath(os.environ['HOME'] + "/.dotman")

        # since the parent of config_file has the name of the program at the end of the path, convert the path to string, 
        # split into a list, get the last element, concatenate onto backup_dir, and convert back to an absolute path 
        backup_prog_dir = os.path.abspath(str(backup_dir) + str(self._get_parent_directory(config_file)).split('/')[-1])

        self._make_unmade_directories(backup_dir, backup_prog_dir)
        
        copyfile(config_file, os.path.abspath(str(backup_prog_dir) + newname))

    def _make_unmade_directories(self, dirpath, prog_dir):
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)
        elif os.path.isfile(dirpath):
            os.remove(dirpath)
            os.mkdir(dirpath)

        if not os.path.exists(os.path.join(prog_dir)):
            os.mkdir(prog_dir)