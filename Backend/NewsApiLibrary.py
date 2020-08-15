from newsapi import NewsApiClient
import requests


# api-key: eb7394eb8fe74ed69529b9d9f22b524d


def getHTML(url):
    return requests.get(url)

class article():
    def __init__(self, author=None, content=None, description=None, publishedAt=None, source=None, title=None, url=None, urlToImage=None):
        self.author = author
        self.content = content
        self.description = description
        self.publishedAt = publishedAt
        self.source = source
        self.title = title
        self.url = url
        self.urlToImage = urlToImage

    def Parser(self):
        pass


class NewsAPI():

    newsapi = NewsApiClient(api_key='eb7394eb8fe74ed69529b9d9f22b524d')

    def returnArticle(self, article):
        return article(article['author'], article['content'], article['description'], article['publishedAt'], article['source'],
                       article['title'], article['url'], article['urlToImage'])

    def getTopHeadlines(self, q, sources, language):
        return self.newsapi.get_top_headlines(q=q, sources=sources, language=language)

    def getEverything(self, q, sources, language):
        return self.newsapi.get_everything(q=q, sources=sources, language=language)

    def find_Trump(self, term, iterated):
        tally = 0
        if isinstance(iterated, list):
            for value in iterated:
                tally = tally + self.find_Trump(term, value)
        elif isinstance(iterated, dict):
            for value in iterated.values():
                tally = tally + self.find_Trump(term, value)
        elif isinstance(iterated, str):
            tally = tally + self.stringIteration(term, iterated)

        return tally

    # Could use findall in re module instead (re: regular expressions module)
    def stringIteration(self, term, string):
        tally = 0
        nextHop = len(term) + 1

        try:
            index = string.find(term)
            if index > -1:
                tally += 1
                string = string[nextHop:]
                tally = tally + self.stringIteration(term, string)
        except:
            print('Passed Array Bounds')
            return 0

        return tally







if __name__ == "__main__":

   pass




    # newsInstance = NewsAPI()
    # print(newsInstance.newsapi.get_everything(q='coronavirus', sources='fox-news', language='en'))




"""

    for key, value in top_headlines_Fox.items():
        print(key, '->', value)

    print('\n')

    for key, value in top_headlines_CNN.items():
        print(key, '->', value)


    Fox_Tally = newsInstance.find_Trump('coronavirus', top_headlines_Fox)
    CNN_Tally = newsInstance.find_Trump('coronavirus', top_headlines_CNN)

    print("\n", "Fox Tally:", Fox_Tally, "CNN Tally:", CNN_Tally)

"""









