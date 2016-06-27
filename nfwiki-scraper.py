#	Copyright (C) Aparajita Haldar
#
#	Python code using BeautifulSoup
# to scrape Nerdfighteria Wiki
#	and to save top video transcripts in a neat file.
#

import urllib

nfwiki = 'https://nerdfighteria.info/channel/54/1001'
nfwikipage = urllib.urlopen(nfwiki)

savefile = open('NerdfighteriaWikiTranscripts', 'w')

from bs4 import BeautifulSoup
soup = BeautifulSoup(nfwikipage)

count = 20
count2 = count

table = soup.find('table', id="vid-table")
rows = table.findAll('tr')
for tr in rows:
    cell = tr.findAll('td')
    link = cell[0].find('a').get('href')
    
    nfvidpage = urllib.urlopen(link)
    
    crouton = BeautifulSoup(nfvidpage)
    
    transcriptbox = crouton.find('div', id="transcript")
    transcript = ' '.join(transcriptbox.findAll(text=True)).encode("ascii", "ignore")

#    print transcript
    
    titlediv = crouton.find('div', id="video-title")
    titletd = titlediv.find('td', style="padding:2px 5px;")
    title = titletd.find('h1').string
    
    print title
#    break
    
    s = "Number:" + str(count2-count+1) + "\nTitle:" + title + "\n" + transcript + "\n\n"
    savefile.write(s)
    
    count-=1
    if count==0:
    	break
