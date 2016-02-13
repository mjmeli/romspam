from lxml import html
import requests

"""
    getquote
    Get a quote from the quote generating website and return it as a string.
"""
def getquote():
    # Request the site
    try:
        page = requests.get('http://www.romanticlovemessages.com/random/')
    except requests.exceptions.RequestException as e:
        print "Could not request website. See log file for more info."
        raise Exception("Could not request website. See log file for more info.")

    # Retrieve the quote as an array of strings
    tree = html.fromstring(page.content)
    quotearr = tree.xpath('//div[@id="hl1"]/text()')

    # Format the quote array properly into a single string
    quote = '\n'.join(quotearr).replace('`', '\'').replace("  "," ")
    return quote
