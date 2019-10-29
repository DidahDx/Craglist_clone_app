import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus
from . import models

# Create your views here.
# Are used to return the web pages (Add extra information to and get info from web pages)
BASE_CRAIGSLIST_URL = 'https://kenya.craigslist.org/search/?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


def home(request):
    return render(request, 'base.html')


def new_search(request):
    search = request.POST.get('search')  # gets what is being searched for
    models.Search.objects.create(search=search)  # creates search object to be added to database
    final_url = BASE_CRAIGSLIST_URL.format(quote_plus(search))  # completes the url with the searched item
    response = requests.get(final_url)
    data = response.text  # gets the html page
    soup = BeautifulSoup(data, features='html.parser')  # create a soup object

    post_listings = soup.find_all('li', {'class': 'result-row'})  # get all items

    final_postings = []

    for post in post_listings:
        # looping through to get the details per item
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        #  check if it has a price
        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
            print(post_image_url)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'

        final_postings.append((post_title, post_url, post_price, post_image_url))  # it contains an array of tuples

    send_to_frontend = {
        'search': search,
        'final_postings': final_postings,
    }
    return render(request, 'my_app/new_search.html', send_to_frontend)
