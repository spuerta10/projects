'''In this proyect I'll take comments from the comment section of the app Spotify
    from the App Store for making a sentiment analysis with them.    
    @author: Santiago Puerta'''


import requests #conecting to AppleStore server
from lxml import html as html #making an html document compatible with XPath
from sentiment import analysis #sentiment analysis
from sentiment import graphs #graphs


#web page where the article is taken of
PAGE = 'https://apps.apple.com/us/app/spotify-discover-new-music/id324684580#see-all/reviews'
COMMENTS = '//p/text()' #Xpath to find the comments


def get_comments():
    try:
        response = requests.get(PAGE) #response of the Apple Store server
        if response.status_code == 200: #if server gives me an OK
            doc = response.content.decode('utf-8') #the HMTL that is given I'll decode it
            x_doc = html.fromstring(doc) #I'll convert the doc to something that I can control with Xpath
            comments = x_doc.xpath(COMMENTS)
            return comments
        else: #if server gives me an error wich error is?
            raise ValueError(f'Error {response.status_code}')
    except ValueError as ve:
        print(ve)


def run():
    comments = get_comments() #get the list of the comments of the app
    #news = to_str(article) #get a single string out of the paragraphs
    ps_tuple = analysis(comments) #results from the sentiment analysis
    graphs(ps_tuple[0], ps_tuple[1])


if __name__ == '__main__':
    run()

