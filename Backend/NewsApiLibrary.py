from newsapi import NewsApiClient
import requests


# api-key: eb7394eb8fe74ed69529b9d9f22b524d


def getHTML(url):
    return requests.get(url)


class NewsAPI():

    newsapi = NewsApiClient(api_key='eb7394eb8fe74ed69529b9d9f22b524d')


    def getTopHeadlines(self, q, sources, language):
        return self.newsapi.get_top_headlines(q=q, sources=sources, language=language)

    def getEverything(self, q, sources, language):
        return self.newsapi.get_everything(q=q, sources=sources, language=language)











"""


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




"""



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









