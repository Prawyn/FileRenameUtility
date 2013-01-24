import os, sys, re


class Folder(object):
    """docstring for Folder"""
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def exists(self):
        return os.path.exists(self.folder_path)

    def kill(self):
        #Not sure about this implementation. Idea is to delete the unwanted instance.
        del self

    def append_filename(self):
        """ This method append a specific string at the end of each file name in the folder. """
        append_string = raw_input("Please enter the string you want to append: ")
        for filename in os.listdir(self.folder_path):
            if re.match(r"^.+\..+$", filename):
                file_extension = os.path.splitext(filename)[1]
                new_filename = "%s%s%s"%(filename.rstrip(file_extension), append_string, file_extension)
                os.rename("%s%s%s" % (self.folder_path, "/", filename), "%s%s%s" % (self.folder_path, "/", new_filename))

    def insert_filename(self, insert_string):
        pass

    def begin_filename(self, begin_string):
        pass

    def change_file(self, new_string):
        pass

def get_option():
    change = raw_input("How you want to change the file name (Append/ Insert/ Startwith/ Change) ?")
    if change not in ['Append', 'Insert', 'Startwith', 'Change']:
        print 'Please enter proper input.'
        get_option()
    else:
        return change    

def rename_folder():

    method_dict = {'Append': 'append_filename', 'Insert': 'insert_filename', 'Startwith': 'begin_filename', 'Change': 'change_file' }
    folder_path = raw_input("Please enter path:")
    folder = Folder(folder_path)

    if folder.exists():
        print "Folder exists in the correct path..."
        change = get_option()
        getattr(folder,  method_dict[change])()
    else:
        print "Please enter a valid path..."
        folder.kill() 
        rename_folder()     
    print "Successfully File names have been modified !. "  

if  __name__ == "__main__":
    rename_folder()








