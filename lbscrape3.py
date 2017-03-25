from urllib.request import urlopen
from bs4 import BeautifulSoup
import time


html = urlopen("http://www.thelongboardstore.com/search.php?mode=1&search_query_adv=carving+%2B+complete&brand=&category%5B%5D=23&searchsubs=ON&price_from=&price_to=&featured=&shipping")
bsObj = BeautifulSoup(html, "html.parser")
p = open("lb_boards.txt", 'a')
board_list = []

def get_next_page(html, bsObj):
    next_page = bsObj.find( "a", {"class":"nav-next"} )
    if next_page and ('href' in next_page.attrs):
        partial = str(next_page.attrs['href'])
        new_url = "http://www.thelongboardstore.com" + partial
        html = urlopen(new_url)
        bsObj = BeautifulSoup(html, "html.parser")
        get_board_pages(html, bsObj)
    else:
        print("Finished")

# run this on each page to get player detail page links
def get_board_pages(html, bsObj):
    global board_list
    tag_list = bsObj.findAll( "a", {"class":"TrackLink"} )
    for tag in tag_list:
        if 'href' in tag.attrs:
            board_list.append(str(tag.attrs['href']))
        else:
            f.write("no href\n")

    time.sleep(1)


def get_board_details(player_list):
    for board in board_list:
        new_url = "http://www.thelongboardstore.com" + board
        html = urlopen(new_url)
        bsObj = BeautifulSoup(html, "html.parser")
        board_details = []

        name = bsObj.find( "div", {"class":"DetailRow product-heading small--text-center "} )

        price = bsObj.find( "span", {"class":"ProductPrice VariationProductPrice"} )

        function = bsObj.find( "em", {"class":"Function:&nbsp;"} )

        material = bsObj.find( "em", {"class":"Material:&nbsp;"} )

        length = bsObj.find( "em", {"class":"Length:&nbsp;"} )

        width = bsObj.find( "em", {"class":"Width:&nbsp;"} )

        hole = bsObj.find( "div", {"class":"Hole Pattern:&nbsp;"} )

        grip = bsObj.find( "div", {"class":"Grip:&nbsp"} )

        board_details = [name, price, function, material, length,
        width, hole, grip]
        for detail in board_details:
            try:
                print( detail.get_text() )
            except AttributeError:
                print( "None" )

        # delay program for 2 seconds
        time.sleep(2)

get_board_pages(html, bsObj)
get_board_details(board_list)
p.close()
