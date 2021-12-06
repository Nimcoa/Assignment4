# after install request, beautiful soup package then we will able use them properly we use request package to get
# access the page after placing the url or the link inside by using get method that able bring data from given
# webpage url
# the Beautifulsoup allow us to parse in lxml pages by pulling all the different data from the website by
# making easier.

import requests
from bs4 import BeautifulSoup

# using requests package, we use the method of get in order to access the webpage or link
link = "https://www.amazon.com/gp/bestsellers/books/ref=bsm_nav_pill_print/ref=s9_acss_bw_cg_bsmpill_1c1_w?pf_rd_m" \
       "=ATVPDKIKX0DER&pf_rd_s=merchandised-search-1&pf_rd_r=JSFR919BB1373W4FETRV&pf_rd_t=101&pf_rd_p=65e3ce24-654c" \
       "-43fb-a17b-86a554348820&pf_rd_i=16857165011 "
# In order to get access or extract the webpage of Amazon's content  then we need use request by getting
page = requests.get(link)
# print(page.text)

soup = BeautifulSoup(page.content, 'lxml')  # that allow to parse the information from the page
# print(soup)
# it gives or selects each individual book
root_parent_book = soup.findAll(class_="a-column a-span12 a-text-center "
                                       "_p13n-zg-list-grid-desktop_style_grid-column__2hIsc")
# print(root_parent_book)
# create object call soup then beautifulsoup will the content from the page
soup = BeautifulSoup(page.content, 'lxml')
# print(soup)

# it finds all the books for that class since they are all the same or share one class

root_parent_book = soup.findAll(class_="a-section a-spacing-none aok-relative")

# print(root_parent_book)

popular_books = []  # here's empty list where we later put all the popular books

# check to make sure the root is not empty
if root_parent_book:

    for p in root_parent_book[1:11]:  # for each books inside parent books, selecting 10 from the books by using list
        # between the range 1 up 11 so that it excludes 11 later

        title_parent = p.find(class_="zg-text-center-align")  # this is parent title from individual class of one book
        if title_parent:  # testing if th title parent inside  class is in all class
            title = title_parent.find(class_="a-section a-spacing-small").img['alt']
        if title:
            # print(title)   # we print out title from the ten books
            popular_books.append(title)  # we add the titles in the list of the popular_books

        # finding rating
        rating = p.find("span", class_="a-icon-alt".strip())  # this finds the rating  for entire class of top ten books
        if rating:
            popular_books.append(rating.text)  # we add the rating in the list of popular_books and .text removes tags

        price = p.find(name="span",
                       class_="p13n-sc-price".strip())  # This finds the prices for all class of the ten books
        # if the price are in class
        if price:

            popular_books.append(price.text)    # add the prices in popular_books list

print(popular_books)                             # display the popular_books
