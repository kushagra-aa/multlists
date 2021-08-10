import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from requests.compat import quote_plus
from . import models
# Create your views here.
BASE_CRAIGSLIST_URL = "https://{}.craigslist.org/search/?query={}"
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'
CITY = ''
SEARCH_TERM = ''
# FINAL_URL = BASE_CRAIGSLIST_URL.format(quote_plus(SEARCH_TERM))
# ADD FOOOTER

def home(request):
    return render(request, 'myapp/city.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


# ADD CITY ADDING FEATURE
# USER ENTERS THE CITY THEY WANT TO SEARCH
def search(request):
    global CITY
    CITY = request.POST.get('city').lower().replace(" ", "")
    return render(request, 'myapp/search.html')


def new_search(request):
    global SEARCH_TERM
    SEARCH_TERM = request.POST.get('search')
    FINAL_URL = BASE_CRAIGSLIST_URL.format(CITY, quote_plus(SEARCH_TERM))
    models.Search.objects.create(search=search)
    response = requests.get(FINAL_URL)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    post_listings = soup.find_all('li', {'class': 'result-row'})

    final_postings = []

    for post in post_listings:
        post_title = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            post_price = 'N/A'

        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(
                class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
            print(post_image_url)
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'

        final_postings.append(
            (post_title, post_url, post_price, post_image_url))

    stuff_for_frontend = {
        'search': SEARCH_TERM,
        'final_postings': final_postings,
        'city': CITY
    }

    return render(request, 'myapp/new_search.html', stuff_for_frontend)
