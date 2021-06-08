from requests_html import HTMLSession

def search(s):
    session = HTMLSession()
    request = session.get(s)

    # We need this module rather than just 'requests' as the
    # part of the page which shows the publication status is
    # rendered after the initial page load, using JavaScript.
    # requests_html allows us to execute that JS if we call render().
    request.html.render()

    title = request.html.find('h1#page-title')[0].text
    element = request.html.find('.pub_jnl')

    if len(element) == 0:
        return (title,"No publication found")

    return (s, title, element[0].text)

