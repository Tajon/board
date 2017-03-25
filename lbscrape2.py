from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.thelongboardstore.com/search.php?mode=1&search_query_adv=carving+%2B+complete&brand=&category%5B%5D=23&searchsubs=ON&price_from=&price_to=&featured=&shipping")
bsObj = BeautifulSoup(html, "html.parser")
f = open("lb_urls.txt", 'a')

# Added: After getting all player URLs from a list page, get the
# URL of the NEXT list page, open it, run the player function again.
# The two functions call each other.

# looking at this tag to get the next page URL --
# <a title="Go to next page" href="/players?page=1">next ›</a>
# <a href="search.php?mode=1&amp;search_query_adv=carving+%2B+complete&amp;brand=&amp;category%5B%5D=23&amp;searchsubs=ON&amp;price_from=&amp;price_to=&amp;featured=&amp;shipping=&amp;page=2&amp;section=product#results" class="nav-next">Next »</a>
def get_next_page(html, bsObj):
    next_page = bsObj.find( "a", {"class":"nav-next"} )
    if next_page and ('href' in next_page.attrs):
        partial = str(next_page.attrs['href'])
        new_url = "http://www.thelongboardstore.com" + partial
        html = urlopen(new_url)
        bsObj = BeautifulSoup(html, "html.parser")
        # scrape the new page for URLs --
        get_board_pages(html, bsObj)
    else:
        print("Done!")

def get_board_pages(html, bsObj):
    tag_list = bsObj.findAll( "a", {"class":"row_link"} )
    for tag in tag_list:
        if 'href' in tag.attrs:
            f.write(str(tag.attrs['href']) + "\n")
        else:
            f.write("no href\n")
    get_next_page(html, bsObj)

get_board_pages(html, bsObj)
f.close()
