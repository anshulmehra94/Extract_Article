import urllib
from bs4 import BeautifulSoup

def Find_Article_Content(url, article_name):
	article_array = article_name.split(" ")
	print article_array
	html = urllib.urlopen(url).read()
	#print html
	soup = BeautifulSoup(html)
	for script in soup(["script", "style"]):
		script.extract()

	#article = soup.find_all('article')

	#finding article heading
	if soup.find_all('h1'):
		all_heads =soup.find_all('h1')
	elif soup.find_all('h2'):	
		all_heads = soup.find_all('h2')

	#print all_heads[0].get_text()
	gg=0
	for i in all_heads:
		article=i.get_text()
		count=0
		for j in article_array:
			if j in article:
				count+=1
		if count == len(article_array):
			break
		gg+=1
	print all_heads
	print gg
	if gg<len(all_heads):
		article_heading = all_heads[gg].get_text()
		print article_heading

	else:
		print('article not found!')	


	article_text ='No Article Found'
	head_index=0
	#finding article
	if gg<len(all_heads):
		if soup.find_all('article'):
			for i in soup.find_all('article'):
				#print i.get_text()
				if article_heading in i.get_text():
					article_text = i.get_text()

		#finding parent of div in a 	
		else: 
			for i in all_heads:
				if article_heading in i.get_text():
					break
				head_index+=1

			parent_container = all_heads[head_index].parent
			while (len(parent_container.get_text())<10*len(article_heading)):
				parent_container=parent_container.parent

			article_text =parent_container.get_text()
			
		print article_text
	return article_text

	
web_url = input("Please provide the link:")
article_name = input("Please provide keyword/s from Article heading or full Article name:")

Find_Article_Content(web_url, article_name)
