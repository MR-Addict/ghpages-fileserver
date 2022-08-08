import os
import shutil
import datetime

src_path = './src/'
public_path = './public/'
image_path = './image/'
all_files = {}
index_head = '<!DOCTYPE html><html lang="en"><head><title>File Server</title><meta name="viewport" content="width=device-width, initial-scale=1" /><link rel="icon" type="image/png" href="favicon.png"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" /><style>table {font-family: Arial, Helvetica, sans-serif;border-collapse: collapse;width: 100%;}table td,table th {border: 1px solid #ddd;padding: 8px;}table tr:nth-child(even) {background-color: #ebebeb;}table th {padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: #5da68d;color: white;}a {color: blue;text-decoration:none;padding: 8px;}</style></head><body><h1>Index of '


# 1. Convert all directroies files into a dictionary
def get_files(path):
    all_files[path] = os.listdir(path)
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            get_files(path+file+'/')


# 2. Copy src files to public
get_files(src_path)
if os.path.exists(public_path):
    shutil.rmtree(os.getcwd()+public_path)
shutil.copytree(os.getcwd()+'/'+src_path, os.getcwd()+'/'+public_path)

# 3. Copy image favicon to public
for dir in all_files.keys():
    if not os.path.exists(dir.replace(src_path, public_path)+'favicon.png'):
        shutil.copyfile(os.getcwd()+'/'+image_path+'favicon.png',
                        os.getcwd()+'/'+dir.replace(src_path, public_path)+'favicon.png')

# 4. Generate html files
for dir in all_files.keys():
    # 4. Table header
    index = index_head + dir.replace(src_path, '/') + \
        '</h1><table><tr><th style="width:50%">Name</th><th>Last Modeified</th></tr>'

    # 4.2 Add return link
    if len(dir.split('/')) == 3:
        index += '<tr><td><a href="./index.html" '
    else:
        index += '<tr><td><a href="../index.html" '
    index += 'style="color: black"><i class="fa fa-arrow-left"></i></a></td><td>..</td></tr>'

    # 4.3 Table body
    for file in all_files[dir]:
        # 4.3.1 Add next Folder Link
        if os.path.isdir(dir+file):
            index += '<tr><td><i class="fa fa-folder"></i><a href="./'+file+'/' + \
                'index.html">'+file+'</a></td><td>'

        # 4.3.2 Add currnet file link
        else:
            index += '<tr><td><i class="fa fa-file"></i><a href="./' + \
                file+'">'+file+'</a></td><td>'

        # 4.3.3 Add modified time link
        index += str(datetime.datetime.utcfromtimestamp(
            os.path.getmtime(dir+file)).strftime('%Y-%m-%d %H:%M:%S'))
        index += '</td></tr>'

    # 4.4 Table end
    index += '</table></body></html>'

    # 4.4 Write html files
    if len(dir.split('/')) == 3:
        with open('./public/index.html', "w") as outfile:
            outfile.write(index)
    else:
        with open(dir.replace(src_path, public_path)+'index.html', "w") as outfile:
            outfile.write(index)
