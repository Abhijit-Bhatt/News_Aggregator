from flask import Flask, render_template, request, redirect, url_for, abort
from flask_cors import CORS

import utilities

app = Flask(__name__)
CORS(app)

from NewsApiLibrary import *

sourcesAndArticles = {}

@app.route("/")
def landingPageController():
    return render_template("landingPage.html")

@app.route("/options", methods=["GET", "POST"])
def options():
    if request.method == "POST":
        searchFor = request.form['searchFor']
        sources = request.form['source'].split(", ")
        language = request.form['language']
        getTopHeadline = request.form.get("topHeadlines")
        getEverything = request.form.get("getEverything")


        if not getTopHeadline:
            getTopHeadline = "off"

        if not getEverything:
            getEverything = "off"

        print(type(sources))
        print(searchFor)
        print(language)
        print(getTopHeadline)
        print(getEverything)

        return redirect(url_for('display_content', searchFor=searchFor, sources=sources, language=language, topHeadlines=getTopHeadline, getEverything=getEverything))
    else:
        return render_template("Options.html")

@app.route("/display_content/<searchFor>&<sources>&<language>&<topHeadlines>&<getEverything>", methods=["GET", "POST"])
def display_content(searchFor, sources, language, topHeadlines=None, getEverything=None):
    global sourcesAndArticles

    print("in display content")

    if request.method == "POST":
        sourceSelection = request.form.get("ChooseNewsSource")
        sources = sourcesAndArticles.keys()
        index = sources.index(sourceSelection)
        sources[0], sources[index] = sources[index], sources[0]

        return render_template('displayedContent.html', sources=sources, articlesFromAllSources=[sourcesAndArticles[sourceSelection]])

    newsInstance = NewsAPI()

    # Want to pass sources into the view fxn as a list using a ListConverter (Defined in flask documentation) --> for now using hacking method
    sources = utilities.generateListOfSources(sources)


    sourcesAndArticles.clear()

    try:
        if topHeadlines == "on":

            print("Displaying top headlines")

            sourcesAndArticles = {source:newsInstance.getTopHeadlines(searchFor, source, language)['articles'] for source in sources}
            return sourcesAndArticles
            # return render_template('displayedContent.html', sources=sourcesAndArticles.keys(), articlesFromAllSources=sourcesAndArticles.values())
        elif getEverything == "on":
            sourcesAndArticles = {source:newsInstance.getEverything(searchFor, source, language)['articles'] for source in sources}
            return render_template('displayedContent.html', sources=sourcesAndArticles.keys(), articlesFromAllSources=sourcesAndArticles.values())
    except:
        abort(404)



# @app.route("/full_content/<string:url>")
# def full_content(url):
#     print(url)
#     try:
#         fullContent = getHTML(url)
#         with open('templates/fullContent.html', 'w') as file:
#             file.write(fullContent.text)
#         return render_template('fullContent.html')
#
#     except:
#         abort(404)









"""
Filtering:

# Be able to choose between Get Everything or Get Top Headlines (cannot choose both!!)

(1) By news Source (If we select more than 1 news source)
(2) By Country
(3) By language(If we choose more than one language)
(4) Part of spectrum


Choose between Getting top headlines and everything

"""





