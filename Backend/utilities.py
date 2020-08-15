from werkzeug.routing import BaseConverter



def generateListOfSources(sources):
    sources = sources[1:len(sources) - 1]
    print(sources)
    sources = sources.split(", ")
    sources = list(map(lambda source: source[2:len(source) - 1], sources))
    return sources



class ListConverter(BaseConverter):

    def to_python(self, value):
        return value.split('+')

    def to_url(self, values):
        return '+'.join(BaseConverter.to_url(value)
                        for value in values)