from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import os

def rename_files():
    '''
    get file names from folder secretmsg
    rename file names by removing all alphabet letters
    see the message displayed in the secretmsg folder by ordering the images
    by file name
    '''
    file_list = os.listdir(r"secretmsg")
    original_path=os.getcwd()
    os.chdir(r"secretmsg")
    print(file_list)

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None,"abcdefghijklmnopqrstuvwxyz")+".jpg")
        
        print("Old name: "+file_name)
        print("New name: "+file_name.translate(None,"abcdefghijklmnopqrstuvwxyz")+".jpg")
        
    os.chdir(original_path)
    
rename_files()




