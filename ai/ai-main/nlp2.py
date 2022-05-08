import nltk 
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

stop_words=set(stopwords.words('english'))
word_tokens=word_tokenize("Some sentece here./")

#Stemming
ps = PorterStemmer()
for i in word_tokens:
  print("the stemming for {} is {}".format(i,ps.stem(i)))
  
 #Lemmatization
wl = WordNetLemmatizer()
for i in word_tokens:
  print("Lemm for {} is {} ".format(i,wl.lemmatize(i))) 

#Stop words filtered sentence 
filtered_sentence=[]
for i in word_tokens:
  if i not in stop_words:
    filtered_sentence.append(i)

print("".join(word_tokens))
print("".join(filtered_sentence))
