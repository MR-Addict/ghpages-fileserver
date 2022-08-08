import os
import shutil
import datetime

src_path = './src/'
public_path = './public/'
image_path = './image/'
all_files = {}
index_head = '<!DOCTYPE html><html lang="en"><head><title>File Server</title><meta name="viewport" content="width=device-width, initial-scale=1" /><link rel="icon" type="image/png" href="favicon.png"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" /><style>table {font-family: Arial, Helvetica, sans-serif;border-collapse: collapse;width: 100%;}table td,table th {border: 1px solid #ddd;padding: 8px;}table tr:nth-child(even) {background-color: #ebebeb;}table th {padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: #5da68d;color: white;}a {color: blue;text-decoration:none;padding: 8px;}</style></head><body><h1>Index of '


# Get all directroy files
def get_files(path):
    all_files[path] = os.listdir(path)
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            get_files(path+file+'/')


# Copy files
get_files(src_path)
if os.path.exists(public_path):
    shutil.rmtree(os.getcwd()+public_path)
shutil.copytree(os.getcwd()+'/'+src_path, os.getcwd()+'/'+public_path)

# Generate directories
for dir in all_files.keys():
    if len(dir.split('/')) == 3:
        if not os.path.exists(public_path):
            os.makedirs(public_path)
    else:
        if not os.path.exists(dir.replace(src_path, public_path)):
            os.makedirs(dir.replace(src_path, public_path))
    if not os.path.exists(dir.replace(src_path, public_path)+'favicon.png'):
        shutil.copyfile(os.getcwd()+'/'+image_path+'favicon.png',
                        os.getcwd()+'/'+dir.replace(src_path, public_path)+'favicon.png')

# Generate html files
for dir in all_files.keys():
    # Table header
    index = index_head + dir.replace(src_path, '/') + \
        '</h1><table><tr><th style="width:50%">Name</th><th>Last Modeified</th></tr>'

    # Add return link
    if len(dir.split('/')) == 3:
        index += '<tr><td><a href="./index.html" style="color: black"><i class="fa fa-arrow-left"></i></a></td><td>..</td></tr>'
    else:
        index += '<tr><td><a href="../index.html" style="color: black"><i class="fa fa-arrow-left"></a></td><td>..</td></tr>'

    # Table body
    for file in all_files[dir]:
        # Next Folder Link
        if os.path.isdir(dir+file):
            index += '<tr><td><i class="fa fa-folder"><a href="./'+file+'/' + \
                'index.html">'+file+'</a></td><td>'
        # Currnet file link
        else:
            index += '<tr><td><i class="fa fa-file"><a href="./'+file+'">'+file+'</a></td><td>'
        # Modified time link
        index += str(datetime.datetime.utcfromtimestamp(
            os.path.getmtime(dir+file)).strftime('%Y-%m-%d %H:%M:%S'))
        index += '</td></tr>'
    index += '</table></body></html>'
    # Write file
    if len(dir.split('/')) == 3:
        with open('./public/index.html', "w") as outfile:
            outfile.write(index)
    else:
        with open(dir.replace(src_path, public_path)+'index.html', "w") as outfile:
            outfile.write(index)
