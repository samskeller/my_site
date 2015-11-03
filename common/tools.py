def clean_url(url):
    # Make sure the link starts with 'http://' or 'https://' so it's a valid external link
    try:
        if url.find('http://') != 0 and url.find('https://') != 0:
            url = 'http://' + url
    except ValueError:
        url = 'http://' + url
    return url
