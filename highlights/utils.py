from django.conf import settings
from django.core.exceptions import ValidationError

import json
import requests

def query_google_books(title, author):
    url = '{}?q={}+inauthor:{}&key={}'.format(
        settings.GOOGLE_BOOKS_URL_BASE,
        title.replace(' ', '+'),
        author.replace(' ', '+'),
        settings.GOOGLE_BOOKS_API_KEY
    )

    response = requests.get(url)
    if response.status_code != 200:
        raise ValidationError('Error from Google Books API: {}, response: {}'.format(response.status_code, response.text))

    parsed_response = json.loads(response.text)
    if parsed_response['totalItems'] == 0:
        raise ValidationError('No matching books from Google Books API')

    return parsed_response['items'][0]
