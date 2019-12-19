from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
from os.path import isdir
import json
import shutil
from datetime import datetime
from time import gmtime, strftime


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            print(filename)
            i = 1
            if filename != 'Alecv':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '\\' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "\\" +year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "\\" + year + "\\" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "\\" + year)
                        folder_destination_path = extensions_folders[extension] + "\\" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "\\" + month)
                        folder_destination_path = folder_destination_path + "\\" + month


                    file_exists = os.path.isfile(folder_destination_path + "\\" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '\\' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '\\' + filename)[1]
                        new_name = new_name.split("\\")[4]
                        file_exists = os.path.isfile(folder_destination_path + "\\" + new_name)
                    src = folder_to_track + "\\" + filename

                    new_name = folder_destination_path + "\\" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)

extensions_folders = {
#No name
    'noname' : 'C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Uncategorized',
#Audio
    '.aif' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Audio",
    '.cda' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Audio",
    '.mid' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Audio",
    '.midi' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Audio",
    '.mp3' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Audio",
    '.mpa' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Audio",
    '.ogg' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Audio",
    '.wav' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Audio",
    '.wma' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Audio",
    '.wpl' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Audio",
    '.m3u' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Audio",
#Text
    '.txt' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\TextFiles",
    '.doc' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Microsoft\\Word",
    '.docx' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Microsoft\\Word",
    '.odt' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\TextFiles",
    '.pdf': "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\PDF",
    '.rtf': "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\TextFiles",
    '.tex': "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\TextFiles",
    '.wks ': "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\TextFiles",
    '.wps': "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\TextFiles",
    '.wpd': "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\TextFiles",
#Video
    '.3g2': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Video",
    '.3gp': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Video",
    '.avi': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Video",
    '.flv': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Video",
    '.h264': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Video",
    '.m4v': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Video",
    '.mkv': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Video",
    '.mov': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Video",
    '.mp4': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Video",
    '.mpg': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Video",
    '.mpeg': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Video",
    '.rm': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Video",
    '.swf': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Video",
    '.vob': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Video",
    '.wmv': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Video",
#Images
    '.ai': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Images",
    '.bmp': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Images",
    '.gif': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Images",
    '.ico': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Images",
    '.jpg': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Images",
    '.jpeg': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Images",
    '.png': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Images",
    '.PNG': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Images",
    '.ps': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Images",
    '.psd': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Images",
    '.svg': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Images",
    '.tif': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Images",
    '.tiff': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Images",
    '.CR2': "C:\\Users\\Alecv\\Desktop\\Alecv\\Media\\Images",
#Internet
    '.asp': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Internet",
    '.aspx': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Internet",
    '.cer': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Internet",
    '.cfm': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Internet",
    '.cgi': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Internet",
    '.pl': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Internet",
    '.css': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Internet",
    '.htm': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Internet",
    '.js': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Internet",
    '.jsp': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Internet",
    '.part': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Internet",
    '.php': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Internet",
    '.rss': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Internet",
    '.xhtml': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Internet",
#Compressed
    '.7z': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Compressed",
    '.arj': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Compressed",
    '.deb': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Compressed",
    '.pkg': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Compressed",
    '.rar': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Compressed",
    '.rpm': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Compressed",
    '.tar.gz': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Compressed",
    '.z': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Compressed",
    '.zip': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Compressed",
#Disc
    '.bin': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Disc",
    '.dmg': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Disc",
    '.iso': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Disc",
    '.toast': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Disc",
    '.vcd': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Disc",
#Data
    '.csv': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Database",
    '.dat': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Database",
    '.db': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Database",
    '.dbf': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Database",
    '.log': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Database",
    '.mdb': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Database",
    '.sav': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Database",
    '.sql': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Database",
    '.tar': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Database",
    '.xml': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Database",
    '.json': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Database",
#Executables
    '.apk': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Executables",
    '.bat': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Executables",
    '.com': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Executables",
    '.exe': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Executables",
    '.gadget': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Executables",
    '.jar': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Executables",
    '.wsf': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Executables",
#Fonts
    '.fnt': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Fonts",
    '.fon': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Fonts",
    '.otf': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Fonts",
    '.ttf': "C:\\Users\\Alecv\\Desktop\\Alecv\\Other\\Fonts",
#Presentations
    '.key': "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Presentations",
    '.odp': "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Presentations",
    '.pps': "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Presentations",
    '.ppt': "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Presentations",
    '.pptx': "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Presentations",
#Programming
    '.c': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\C&C++",
    '.class': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Java",
    '.dart': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Dart",
    '.py': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Python",
    '.sh': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Shell",
    '.swift': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\Swift",
    '.html': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\C&C++",
    '.h': "C:\\Users\\Alecv\\Desktop\\Alecv\\Programming\\C&C++",
#Spreadsheets
    '.ods' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Microsoft\\Excel",
    '.xlr' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Microsoft\\Excel",
    '.xls' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Microsoft\\Excel",
    '.xlsx' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Microsoft\\Excel",
#System
    '.bak' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Other\\System",
    '.cab' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Other\\System",
    '.cfg' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Other\\System",
    '.cpl' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Other\\System",
    '.cur' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Other\\System",
    '.dll' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Other\\System",
    '.dmp' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Other\\System",
    '.drv' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Other\\System",
    '.icns' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Other\\System",
    '.ico' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Other\\System",
    '.ini' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Other\\System",
    '.lnk' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Other\\System",
    '.msi' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Other\\System",
    '.sys' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Other\\System",
    '.tmp' : "C:\\Users\\Alecv\\Desktop\\Alecv\\Text\\Other\\System",
}

folder_to_track = 'C:\\Users\\Alecv\\Desktop'
folder_destination = 'C:\\Users\\Alecv\\Desktop\\Alecv'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

os.chdir('C:\\Users\\Alecv\\Desktop\\Alecv')
for x in extensions_folders.values():
    if isdir(x) == False:
        print(os.getcwd())
        os.makedirs(x)
    else:
        continue

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()