#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#@markdown <pre>
#@markdown <br><center><img src="https://ptpimg.me/v83988.png" width="650px"/>
#@markdown <font size=7><code>឵឵ Generate <b><font color="DEB72C">IMDb</font></b> Template឵឵ ឵</code></center></pre>
##@markdown <font size="3"><i>Create your own OMDb API Key here: http://www.omdbapi.com/apikey.aspx</font>
import urllib.request
import json
import re
import requests
import sys
import subprocess
import os
import re
import time
import pathlib
from bs4 import BeautifulSoup
from IPython.display import clear_output

import urllib.request
AUTO_MOVE_PATH = "/home/runner/"
HOME = os.path.expanduser("~")
if not os.path.exists(f"{HOME}/.ipython/ocr.py"):
    get_ipython().system('wget https://raw.githubusercontent.com/biplobsd/OneClickRun/master/res/ocr.py')
    get_ipython().system('mkdir ~/.ipython && mv ./ocr.py $HOME/.ipython/ocr.py')



from ocr import (
    runSh,
    findProcess,
    loadingAn,
)

# Variables
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0'}
#@markdown ឵឵
#@markdown ឵឵<font size="6" color="#9FD4F3"> ឵឵឵» OMDb </font><font size="6">API Key:</font></h1>

api_key = '28ab9ae6' #@param {type:"string"}

#@markdown <h1><font size="6" color="#F1F290">឵឵ » IMDb</font><font size="6"> URL <small>or</small> ID:</font></h1>
IMDB_URL_OR_ID = 'https://www.imdb.com/title/tt3794354/' #@param {type:"string"}

#@markdown <font size="6" color="#FF5C5C"> ឵឵ ឵឵឵» YouTube</font><font size="6"> Trailer URL:</font>
YouTube_URL = 'https://www.youtube.com/watch?v=szby7ZHLnkA' #@param {type:"string"}
if YouTube_URL == "":
  youtube_enabled = False
else:
  youtube_enabled = True

#@markdown <font size="6" color="#E9A3C4"> ឵឵ ឵឵឵» Movie </font><font color="#9FA5F3" font size="4">឵឵OR឵</font><font size="6" color="#E9A3C4"> TV</font><font font size="6"> File Path:</font></center>
Path = "/home/runner/drive/2nd shift/Sweet.November.2001.720p.WEBRip.999MB.HQ.x265.10bit-GalaxyRG[TGx]/Sweet.November.2001.720p.WEBRip.999MB.HQ.x265.10bit-GalaxyRG.mkv" #@param {type:"string"}

#@markdown <font size="6" color="#98F88E"> ឵឵ ឵឵឵» Download</font><font size="6"> URL:</font>

if not os.path.exists(Path):
    clear_output()
    sys.exit("Your video filepath does not exist, please check it.")
else:
    pass

if Path == "":
  mediainfo_enabled = False
else:
  mediainfo_enabled = True
  tmp = subprocess.Popen('mediainfo --Logfile=/home/runner/.nfo "{}"'.format(Path), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
  time.sleep(5) # Wait 5s for the nfo file to populate properly
  with open('/home/runner/.nfo', 'r', encoding='utf-8') as nfo_file:
    nfo = nfo_file.readlines()
    del nfo[1]
    nfo[1] = "Complete name                            : {}\n".format(os.path.basename(Path))
    nfo = ''.join(nfo)

for i in range(10):
    clear_output()
    loadingAn()

get_ipython().run_line_magic('cd', "'/dev/shm'")
get_ipython().system('ffmpeg -hide_banner -ss 00:56.0 -i "$Path" -vframes 1 -q:v 2 -y "frame1.png"')
get_ipython().system('curl --insecure -F "reqtype=fileupload" -F "fileToUpload=@frame1.png" https://catbox.moe/user/api.php -o frame1.txt')
f1 = open('frame1.txt', 'r')
file_content1 = f1.read()
f1.close()
time.sleep(2)
get_ipython().system('ffmpeg -hide_banner -ss 02:26.0 -i "$Path" -vframes 1 -q:v 2 -y "frame2.png"')
get_ipython().system('curl --insecure -F "reqtype=fileupload" -F "fileToUpload=@frame2.png" https://catbox.moe/user/api.php -o frame2.txt')
f2 = open('frame2.txt', 'r')
file_content2 = f2.read()
f2.close()
time.sleep(2)
get_ipython().system('ffmpeg -hide_banner -ss 04:10.0 -i "$Path" -vframes 1 -q:v 2 -y "frame3.png"')
get_ipython().system('curl --insecure -F "reqtype=fileupload" -F "fileToUpload=@frame3.png" https://catbox.moe/user/api.php -o frame3.txt')
f3 = open('frame3.txt', 'r')
file_content3 = f3.read()
f3.close()

imdb_pattern = re.compile('(tt\d{7,8})')
imdb_id = re.findall(imdb_pattern, IMDB_URL_OR_ID)[0]

get_ipython().run_line_magic('cd', "'/content'")
def get_imdb_template(imdb_id):
  imdb_url = f'http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}&r=json&plot=short'
  Screenshot1 = file_content1
  Screenshot2 = file_content2
  Screenshot3 = file_content3
  Path = "$Path"
  Lock = False #@param {type:"boolean"}
  Lock_Credits = "150" #@param {type:"string"}
  Link = "https://drive.google.com/open?id=1VGIiLrTuGbs6IqQ8EySvjX19dDWD1e4m" #@param {type:"string"}
  #@markdown </div> 
  if Link == "":
    print("You forgot putting in the link to download!")
    sys.exit()

  def get_story_line(imdb_id):
    url = 'https://www.imdb.com/title/{}'.format(imdb_id)
    r = requests.get(url, headers=headers)
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')
    story_line = soup.find_all('div', class_='inline canwrap')[0].find('span').text.lstrip()
    return story_line

  # Fetch data
  with urllib.request.urlopen(imdb_url) as imdb_url:
    imdb_data = json.loads(imdb_url.read().decode())

  LQ_poster = "{}".format(imdb_data['Poster'])
  HQ_poster = re.sub("[._V1_SX300]{10}", "", LQ_poster)

  # Process data
  text_dump = "[align=center][size=x-large]{} ({})[/size]\n".format(imdb_data['Title'], imdb_data['Year'])
  text_dump += "\n"
  text_dump += "[img=400x1200]{}[/img][/align]\n".format(HQ_poster)
  text_dump += "\n"
  text_dump += "[size=medium][b][color=#BD9710]IMDb:[/color][/b][/size]\n"
  text_dump += "[code]\n"
  text_dump += "{}\n".format(imdb_data['Genre'])
  text_dump += "\n"
  text_dump += "{}\n".format(imdb_data['Plot'])
  text_dump += "\n"
  text_dump += "https://www.imdb.com/title/{}\n".format(imdb_id)
  text_dump += "[/code]\n"
  if youtube_enabled:
    text_dump += "[align=center][b][color=#c586c0][size=large]Trailer:[/size][/color][/b]\n"
    text_dump += "\n"
    text_dump += "[video=youtube]{}[/video]\n".format(YouTube_URL)
    text_dump += "[/align]\n"
  if mediainfo_enabled:
    text_dump += "\n"
    text_dump += "[color=#83A8CE][size=medium][b]MediaInfo:[/b][/size][/color]\n"
    text_dump += "[mediainfo]\n"
    text_dump += "{}".format(nfo)
    text_dump += "[/mediainfo]\n"
  text_dump += "\n"
  text_dump += "[b][color=#D5A6D5][size=medium]Screenshots:[/size][/color][/b]\n"
  text_dump += "[spoiler][align=center]\n"
  text_dump += "[img]{}[/img]\n".format(Screenshot1)
  text_dump += "\n"
  text_dump += "[img]{}[/img]\n".format(Screenshot2)
  text_dump += "\n"
  text_dump += "[img]{}[/img]\n".format(Screenshot3)
  text_dump += "[/align][/spoiler]\n"
  text_dump += "\n"
  text_dump += "[align=center][color=#39B73C][size=large][font=Trebuchet MS][b]Download Link:[/b][/font][/size][/color]\n"
  text_dump += "[size=xx-small]឵឵ ឵[/size]\n"
  if Lock == False:
    text_dump += "[hide][url={}]{}[/url][/hide][/align]".format(Link, Link)
  if Lock == True:
    text_dump += "[lock={}][url={}]{}[/url][/lock][/align]".format(Lock_Credits, Link, Link)
  return text_dump

clear_output()
print(get_imdb_template(imdb_id))

