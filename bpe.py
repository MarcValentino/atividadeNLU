import re, collections
from functools import reduce

def get_stats(vocab):
    pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
        symbols = word.split()
        for i in range(len(symbols)-1):
            pairs[symbols[i],symbols[i+1]] += freq
    return pairs

def merge_vocab(pair, v_in):
    v_out = {}
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
        w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out

def matchTokens(vocab, inputWords, outputf):
    numberOfRecognizedTokens = 0
    totalTokens = reduce(lambda x, y: x+y, inputWords.values())
    for inputWord in inputWords.keys():
        recognized = False
        for vocabWord in vocab.keys():
            vocabWordParts = vocabWord.split()
            print("Vocab: " + ' '.join(''.join(vocabWordParts)))
            print("Input: " + inputWord)
            if ' '.join(''.join(vocabWordParts)) == inputWord:
                numberOfRecognizedTokens+=inputWords[inputWord]
                outputf.write('Palavra reconhecida: ' + ''.join(inputWord.split()) + '; Partes: ' + str(vocabWordParts) + '\n')
                recognized = True
                break

        if not recognized: 
            
            outputf.write('Palavra não reconhecida: ' + ''.join(inputWord.split())  + '\n')
    outputf.write('Total: ' + str(numberOfRecognizedTokens) + '/' + str(totalTokens) + ' de palavras reconhecidas\n')


def intercalate(word):
    return ' '.join(word) + ' _'

def tokenizeFile(file):
    vocab = {}
    line = file.readline()
    wordCapturer = re.compile(r'([A-Z]?[a-z]+)|(’[a-z]*)|([0-9]+)')

    while line:
        wordsCaptured = wordCapturer.finditer(line)

        wordsCapturedLowerCase = map(lambda w: line[w.start():w.end()].lower(), wordsCaptured)
        for word in wordsCapturedLowerCase:
            processedWord = intercalate(word)
            if processedWord not in vocab.keys(): vocab[processedWord] = 1
            else: vocab[processedWord] += 1
        line = file.readline()
    
    return vocab



f = open('vocabulario_tokenizador', 'r')

vocab = tokenizeFile(f)


num_merges = 700

pairsFile = open('pairsObtained', 'w')
for i in range(num_merges):
    pairs = get_stats(vocab)
    best = max(pairs, key = pairs.get)
    vocab = merge_vocab(best, vocab)
    printablePair = str(best) + '\n'
    pairsFile.write(printablePair)

pairsFile.close()

testFile = open('input_tokenizador', 'r')
inputWords = tokenizeFile(testFile)
print(inputWords)
outputf = open('tokens_recognized', 'w')
matchTokens(vocab, inputWords, outputf)

# Pera ai... Eu quero usar o quê? Os pares que eu obtive só?


