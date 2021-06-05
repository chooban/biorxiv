from requests_html import HTMLSession

def search(s):
    session = HTMLSession()
    request = session.get(s)
    request.html.render()

    title = request.html.find('h1#page-title')[0].text
    element = request.html.find('.pub_jnl')

    if len(element) == 0:
        return (title,"No publication found")

    return (s, title, element[0].text)
    