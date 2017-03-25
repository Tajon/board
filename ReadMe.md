My scraping project was for a longboard store. Initially, I wanted to scrape the urls of the longboards using  tag_list but ran in to trouble finding the links. When I did find the links I was able to scrape them but but instead if the 72 expected links I found 200+.

After looking through the individual links I was able to find out that just about all the links were printed to the text file but some had copies of two, three, and four. However, I did research and found on stackoverflow and a way to make the links stop making copies.

Eventually, I got close to by number but realized that the there were two differnt classes and that would make it harder to scrape. One was TrackLink and the other was btn TrackLink.

Then after that I tried to get the link to go to the next page but to no avail. Finally, I tried to scrape the pages for the information that represent my columns. But I realized that the informationI would need was in em tags and was not sure how to access it from the div parent. 
