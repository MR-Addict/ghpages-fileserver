import os
import shutil
import datetime

all_files = {}
src_path = './src/'
public_path = './public/'
image_path = './images/'
site_link = 'https://mraddict.one/ghpages-fileserver/'
index_head = '<!DOCTYPE html><html lang="en"> <head> <title>File Server</title> <meta name="viewport" content="width=device-width, initial-scale=1" /> <link rel="icon" href="site_link/site_img/favicon.png" /> <style> * { margin: 0; padding: 0; box-sizing: border-box; font-family: sans-serif; } html { font-size: 62.5%; } body { padding: 2rem; font-size: 1.5rem; } table { width: 100%; border-collapse: collapse; } table td, table th { padding: 1rem; border: 0.1rem solid #ddd; } table tr:nth-child(even) { background-color: #ebebeb; } table th { text-align: left; background-color: #5da68d; color: white; } a { color: blue; text-decoration: none; padding: 1rem; } p{ font-size: 2.5rem; } td img {height: 1.4rem;} </style></head><body><p>'.replace(
    "site_link/", site_link)


# 1. Convert all directroies files into a dictionary
def get_files(path):
    all_files[path] = os.listdir(path)
    for file in os.listdir(path):
        if os.path.isdir(os.path.join(path, file)):
            get_files(path+file+'/')


# 2. Copy src files to public
get_files(src_path)
# if os.path.exists(public_path):
#     shutil.rmtree(os.getcwd()+public_path)
# shutil.copytree(os.getcwd()+'/'+src_path, os.getcwd()+'/'+public_path)
# Only works on 3.8+
shutil.copytree(os.getcwd()+'/'+src_path, os.getcwd() +
                '/'+public_path, dirs_exist_ok=True)

# 3. Copy images to public img folder
shutil.copytree(os.getcwd()+'/'+image_path+'site_img', os.getcwd() +
                '/'+public_path+'site_img', dirs_exist_ok=True)

# 4. Generate html files
for dir in all_files.keys():
    # 4. Table header
    site_rel_path = site_link
    index = index_head + '<a href="{}">~</a>'.format(site_link)
    for dir_name in ('~'+dir.replace('./src', '')).split('/')[1:-1]:
        site_rel_path += dir_name+'/'
        index += '/<a href="{}">{}</a>'.format(site_rel_path, dir_name)
    index += '</p><table><tr><th style="width:33%">Name</th><th style="width: 33%">Last Modefied</th><th>Size</th></tr>'

    # 4.2 Add return link
    if len(dir.split('/')) == 3:
        index += '<tr><td><a href="./">'
    else:
        index += '<tr><td><a href="../">'
    index += '<img src="{}site_img/arrow.svg" alt="arrow" /></a></td><td>..</td><td>..</td></tr>'.format(
        site_link)

    # 4.3 Table body
    for file in all_files[dir]:
        # 4.3.1 Add next Folder Link
        if os.path.isdir(dir+file):
            index += '<tr><td><img src="{}site_img/folder.svg" alt="folder" /><a href="{}/">{}</a></td>'.format(
                site_link, file, file)

        # 4.3.2 Add current file link
        else:
            index += '<tr><td><img src="{}site_img/download.svg" alt="download" /><a href="{}" download>{}</a></td>'.format(
                site_link, file, file)

        # 4.3.3 Add modified time link
        index += '<td>{}</td>'.format(str(datetime.datetime.utcfromtimestamp(
            os.path.getmtime(dir+file)).strftime('%Y/%m/%d %H:%M:%S')))

        # 4.3.4 Add file size
        if os.path.isfile(dir+file):
            file_size = os.path.getsize(dir+file)
            if file_size < 1024:
                index += '<td>{} B</td></tr>'.format(file_size)
            elif file_size < 1024**2:
                index += '<td>{:.2f} KB</td></tr>'.format(file_size/1024)
            elif file_size < 1024**3:
                index += '<td>{:.2f} MB</td></tr>'.format(file_size/(1024**2))
            else:
                index += '<td>{:.2f} GB</td></tr>'.format(file_size/(1024**3))
        else:
            index += '<td>..</td></tr>'

    # 4.4 Table end
    index += '</table></body></html>'

    # 4.4 Write html files
    if len(dir.split('/')) == 3:
        with open('./public/index.html', "w") as outfile:
            outfile.write(index)
    else:
        with open(dir.replace(src_path, public_path)+'index.html', "w") as outfile:
            outfile.write(index)
