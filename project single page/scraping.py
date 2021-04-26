import urllib.request
from bs4 import BeautifulSoup

address = "https://www.rottentomatoes.com/m/raya_and_the_last_dragon/reviews"

full_page_source_code = urllib.request.urlopen(address)
soup = BeautifulSoup(full_page_source_code, 'html.parser')
#print(soup.prettify())  #print full page resource file

review = soup.find_all('div', attrs={'class' : 'the_review'})


for rev in review:
    print('review: ')
    print(rev.get_text(),'\n')