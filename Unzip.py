import os, zipfile, time

dir_name = r"\\yourpath"
extension = ".zip"

print(dir_name)
os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        file_name = os.path.abspath(item) # get full path of files
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object
        zip_ref.extractall(dir_name) # extract file to dir
        zip_ref.close() # close file
        os.remove(file_name) # delete zipped file
        time.sleep(10)

#Rename the files
for item in os.listdir(dir_name):
    if item.startswith("creative-view"):
        old_file_name = os.path.abspath(item)
        print(old_file_name)
        new_file_name = r"\\yourpath\per-creative-view.csv"
        os.rename(old_file_name, new_file_name)

for item in os.listdir(dir_name):
    if item.startswith("social-view"):
        old_file_name = os.path.abspath(item)
        print(old_file_name)
        new_file_name = r"\\yourpath\social-support-view.csv"
        os.rename(old_file_name, new_file_name)

for item in os.listdir(dir_name):
    if item.startswith("support-view"):
        old_file_name = os.path.abspath(item)
        print(old_file_name)
        new_file_name = r"\\yourpath\support-system-view.csv"
        os.rename(old_file_name, new_file_name)


for item in os.listdir(dir_name):
    if item.startswith("url-view"):
        old_file_name = os.path.abspath(item)
        print(old_file_name)
        new_file_name = r"\\yourpath\url-management-view.csv"
        os.rename(old_file_name, new_file_name)

for item in os.listdir(dir_name):
    if item.startswith("video-view"):
        old_file_name = os.path.abspath(item)
        print(old_file_name)
        new_file_name = r"\\yourpath\video-control-view.csv"
        os.rename(old_file_name, new_file_name)

for item in os.listdir(dir_name):
    if item.startswith("web-view"):
        old_file_name = os.path.abspath(item)
        print(old_file_name)
        new_file_name = r"\\yourpath\web-co-view.csv"
        os.rename(old_file_name, new_file_name)
