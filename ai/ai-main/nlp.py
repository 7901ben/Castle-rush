import re 
# import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def convert_pdf_to_txt():
    my_str="String goes here "
    stopwords1 = set(stopwords.words("english"))
    words = word_tokenize(my_str)
    freqTable = dict()
    for word in words:
        word = word.lower ()
        if word in stopwords1:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1
    sentences = sent_tokenize(my_str)
    sentenceValue = dict()
    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[ sentence]
    # Average value of a sentence from the original text
    average = int (sumValues / len(sentenceValue))
    summary=''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[ sentence] > (1.2 * average)) :
            summary+= " "+sentence
    return summary

print(convert_pdf_to_txt())