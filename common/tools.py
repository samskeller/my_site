def clean_url(url):
    # Make sure the link starts with 'http://' so it's a valid external link
    try:
        if url.index('http://') != 0:
            url = 'http://' + url
    except ValueError:
        url = 'http://' + url
    return url
