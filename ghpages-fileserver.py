import os
import shutil
import datetime

src_path = './src/'
public_path = './public/'
all_files = {}
index_head = '<!DOCTYPE html><html lang="en"><head><title>File Server</title><meta name="viewport" content="width=device-width, initial-scale=1" /><style>table {font-family: Arial, Helvetica, sans-serif;border-collapse: collapse;width: 100%;}table td,table th {border: 1px solid #ddd;padding: 8px;}table tr:nth-child(even) {background-color: #f2f2f2;}table th {padding-top: 12px;padding-bottom: 12px;text-align: left;background-color: #5da68d;color: white;}a {color: blue;text-decoration:none}</style></head><body><h1>Index of '


# Get all directroy files
def get_files(path):
    all_files[path] = os.listdir(path)
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            get_files(path+file+'/')


get_files(src_path)
if os.path.exists(public_path):
    shutil.rmtree(os.getcwd()+public_path)
shutil.copytree(os.getcwd()+src_path, os.getcwd()+public_path)

# Generate directories
for dir in all_files.keys():
    if len(dir.split('/')) == 3:
        if not os.path.exists(public_path):
            os.makedirs(public_path)
    else:
        if not os.path.exists(dir.replace(src_path, public_path)):
            os.makedirs(dir.replace(src_path, public_path))

# Generate html files
for dir in all_files.keys():
    # Table header
    index = index_head + dir.replace(src_path, '/') + \
        '</h1><table><tbody><tr><th style="width:50%">Name</th><th>Last Modeified</th></tr>'

    # Add return link
    if len(dir.split('/')) == 3:
        index += '<tr><td><a href="./index.html">..</a></td><td>..</td></tr>'
    else:
        index += '<tr><td><a href="../index.html">..</a></td><td>..</td></tr>'

    # Table body
    for file in all_files[dir]:
        # Next Folder Link
        if os.path.isdir(dir+file):
            index += '<tr><td><a href="./'+file+'/' + \
                'index.html">'+file+'</a></td><td>'
        # Currnet file link
        else:
            index += '<tr><td><a href="./'+file+'">'+file+'</a></td><td>'
        # Modified time link
        index += str(datetime.datetime.utcfromtimestamp(
            os.path.getmtime(dir+file)).strftime('%Y-%m-%d %H:%M:%S'))
        index += '</td></tr>'
    index += '</tbody></table></body></html>'
    # Write file
    if len(dir.split('/')) == 3:
        with open('./public/index.html', "w") as outfile:
            outfile.write(index)
    else:
        with open(dir.replace(src_path, public_path)+'index.html', "w") as outfile:
            outfile.write(index)
