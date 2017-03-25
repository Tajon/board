from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.thelongboardstore.com/search.php?mode=1&search_query_adv=carving+%2B+complete&brand=&category%5B%5D=23&searchsubs=ON&price_from=&price_to=&featured=&shipping")

bsObj = BeautifulSoup(html, "html.parser")

f = open("lb_urls.txt", "a")


# findNext('',{'':''})
# tag_list = father.findNext('div',{'class':'SearchContainer'}).findNext('ul',{'class':'ProductList  clear'}).findNext('li',{'class':'even'}).findNext('div',{'class':'ProductDetails'})findAll('a')



tag_list = bsObj.findAll( "a", {"class":"TrackLink"} ) [72::4]
# tag_list2 = bsObj.findAll( "a", {"class":"TrackLink"} )

for tag in tag_list:
    if "href" in tag.attrs:
            f.write(str(tag.attrs["href"]) + "\n")
    else:
            f.write("no href\n")

# for tag in tag_list2:
#      if "href" in tag.attrs:
#              f.write(str(tag.attrs["href"]) + "\n")
#      else:
#              f.write("no href\n")

f.close()
