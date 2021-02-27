import re

f = open('cartas_van_gogh.csv', 'r')
outputf = open('cartas_output', 'w')

bracketRemover = re.compile(r'\[.*\]')
commaRemover = re.compile(r',,+')
htmlRemover = re.compile(r'&nbsp;\d\S:\d|\#ERROR!|&nbsp;')
headerRemover = re.compile(r'"\s*,-+\s*18\d\d\s*[1-9][0-9]*\s*=*"|",\-+\s*[0-9][0-9]*\s*=*"')


line = f.readline()
while line:

    excessiveCommas = re.findall(commaRemover, line)
    wordsWithinBrackets = re.findall(bracketRemover, line)
    htmlMarkers = re.findall(htmlRemover, line)
    headers = re.findall(headerRemover, line)
    filteredLine = line

    if len(excessiveCommas) > 0 or len(wordsWithinBrackets) > 0 or len(htmlMarkers) > 0:
        newLine = ''
        for match in excessiveCommas:
            lineParts = filteredLine.split(match)
            for part in lineParts:
                newLine += part
            filteredLine = newLine
            newLine = ''

        for match in wordsWithinBrackets:
            lineParts = filteredLine.split(match)
            for part in lineParts:
                newLine += part
            filteredLine = newLine
            newLine = ''
        
        for match in headers:
            lineParts = filteredLine.split(match)
            for part in lineParts:
                newLine += part
            filteredLine = newLine
            newLine = ''

        for match in htmlMarkers:
            lineParts = filteredLine.split(match)
            for part in lineParts:
                newLine += part
            filteredLine = newLine
            newLine = ''
    
    if filteredLine != '\n': outputf.write(filteredLine)

    line = f.readline()


# print(stringao[m.start():m.end()])

