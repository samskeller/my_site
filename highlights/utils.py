from django.conf import settings
from django.core import files
from django.core.exceptions import ValidationError

import json
import requests
import tempfile

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

def get_thumbnail(google_books_response):
    # Remove the "&edge=curl" to get rid of the curled page image on the cover
    image_url = google_books_response['volumeInfo']['imageLinks']['thumbnail'].replace('&edge=curl', '')
    response = requests.get(image_url, stream=True)

    if response.status_code != 200:
        raise ValidationError('No matching thumbnail for book')

    file_name = image_url.split('/')[-1]

    # Create a temp file to write the data to
    thumbnailTempFile = tempfile.NamedTemporaryFile()

    for block in response.iter_content(1024 * 8):
        if not block:
            break
        thumbnailTempFile.write(block)

    return file_name, files.File(thumbnailTempFile)
