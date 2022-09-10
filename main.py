import os
import yaml
import shutil
import datetime

all_files = {}
src_path = './src/'
public_path = './public/'
pages_path = './pages/'

template = yaml.load(open("template/template.yaml"), yaml.Loader)
with open('template/template.html', 'r') as file:
    index_template = file.read()


# 1. Convert all directroies files into a dictionary
def get_files(path):
    all_files[path] = os.listdir(path)
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            get_files(path+file+'/')


# 2. Copy src files to public
get_files(src_path)
if os.path.exists(public_path):
    for dir in os.listdir(public_path):
        file_path = os.getcwd()+'/'+public_path+dir
        if os.path.isdir(file_path):
            shutil.rmtree(os.getcwd()+'/'+public_path+dir)
        else:
            os.remove(file_path)

# Only works on python 3.8+
shutil.copytree(os.getcwd()+'/'+src_path, os.getcwd() +
                '/'+public_path, dirs_exist_ok=True)

# 3. Copy images to public img folder
shutil.copytree(os.getcwd()+'/'+pages_path, os.getcwd() +
                '/'+public_path, dirs_exist_ok=True)

# 4. Generate html files
for dir in all_files.keys():
    # 4.1 Table header
    index = ''
    header_link = ''
    table_row = ''

    for dir_name_index, dir_name in enumerate(('~'+dir.replace(src_path, '/')).split('/')[0:-1]):
        link_path = ''
        for i in range(len(('~'+dir.replace(src_path, '/')).split('/')[0:-1])-dir_name_index-1):
            link_path += '../'
        header_link += template["header_link"].replace(
            "PATH", link_path).replace("NAME", dir_name)

    # 4.2 Table body
    for file in all_files[dir]:
        file_size = '..'
        if os.path.isfile(dir+file):
            size = os.path.getsize(dir+file)
            if size < 1024:
                file_size = '{:.2f} B'.format(size)
            elif size < 1024**2:
                file_size = '{:.2f} KB'.format(size/1024)
            elif size < 1024**3:
                file_size = '{:.2f} MB'.format(size/1024**2)
            else:
                file_size = '{:.2f} GB'.format(size/1024**3)
        modified_date = str(datetime.datetime.utcfromtimestamp(
            os.path.getmtime(dir+file)).strftime('%Y/%m/%d %H:%M:%S'))
        if os.path.isfile(dir+file):
            shutil.copy2(os.getcwd()+'/'+pages_path +
                         'file.svg', os.getcwd()+'/'+dir.replace(src_path, public_path))
            table_row += template["table_row_file"].replace(
                "PATH", file).replace("DATE", modified_date).replace(
                "SIZE", file_size)
        elif os.path.isdir(dir+file):
            shutil.copy2(os.getcwd()+'/'+pages_path +
                         'folder.svg', os.getcwd()+'/'+dir.replace(src_path, public_path))
            table_row += template["table_row_foler"].replace(
                "PATH", file).replace("DATE", modified_date).replace("NAME", file_size)

    previous_dots = ''
    for i in range(len((dir.split('/')))-3):
        previous_dots += '../'

    index = index_template.replace("HEADER_LINK", header_link).replace(
        "TABLE_ROW", table_row).replace(
        'style.css', previous_dots+'style.css').replace(
        'favicon.svg', previous_dots+'favicon.svg')

    # 4.4 Write html files
    if len(dir.split('/')) == 3:
        with open('./public/index.html', "w") as outfile:
            outfile.write(index)
    else:
        with open(dir.replace(src_path, public_path)+'index.html', "w") as outfile:
            outfile.write(index)

print("[INFO] Static files generated!")
