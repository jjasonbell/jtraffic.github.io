from bs4 import BeautifulSoup as BS
import os, sys


target_file = sys.argv[1]
out_file = sys.argv[2]
with open(target_file, 'r') as f:
	soup = BS(f, 'lxml')
[tag.extract() for tag in soup('style')]
[tag.extract() for tag in soup('script')]
[tag.extract() for tag in soup('iframe')]
[tag.extract() for tag in soup('footer')]
html = soup.prettify()
with open(out_file, 'w', encoding='utf-8') as f:
	f.write(html)
