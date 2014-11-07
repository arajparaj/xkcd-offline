#!/usr/bin/python
# Script to download all the comic from xkcd
#
import urllib,os,json,re

print "Welcome to xkcd comic downloader"
if not os.path.isdir("xkcd_downloaded"):
	print "Creating folder xkcd_downloaded"
	os.mkdir("xkcd_downloaded")

raw_homepage=urllib.urlopen("http://xkcd.com/info.0.json")
homepage=json.load(raw_homepage)

print "Enter the range of comics to download between 1 to",homepage[u'num']
rangeinput=raw_input("eg: 10,10-100 \t ")

comiclist=list()

for (num_left,num_right,num_single) in re.findall(r'(\d+)-(\d+)|(\d+)',rangeinput):
   if num_single is not '':
      comiclist.append(int(num_single))
   if num_left is not '' and num_right is not '':
      for i in range(int(num_left),int(num_right)+1):
         comiclist.append(i)

for comic in comiclist:
	try:
		comic_url="http://xkcd.com/"+str(comic)+"/info.0.json"
		comic_meta=json.load(urllib.urlopen(comic_url))

		print "Downloading ", comic_meta[u'img']
		image_file="./xkcd_downloaded/"+str(comic)+".jpg"
		urllib.urlretrieve(comic_meta[u'img'], image_file)

		#writing the 
		ftext=open("./xkcd_downloaded/"+str(comic)+".txt",'w')
   		ftext.write(comic_meta[u'alt'])
   		ftext.write("\n=============================================================================\n")
   		ftext.write(comic_meta[u'transcript'])
   		ftext.write("\n=============================================================================\n")
   		ftext.flush()

		pass
	except Exception, e:
		pass
	else:
		pass
	finally:
		pass



print "finished"