import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd

import acquire

# We don't need to install nltk, it should come with anaconda, but nltk
# does need to download some data.
nltk.download('stopwords')
nltk.download('wordnet')

def basic_clean(string):
    """ this code will lower all captioned letters, ignore specific type of codings and remove special characters"""
    string = unicodedata.normalize('NFKD', string)\
        .encode('ascii', 'ignore')\
        .decode('utf-8', 'ignore')\
        .lower()
    string = re.sub(r"[^a-z0-9'\s]", '', string)                                
    return string

# use basic_clean(string) to open work

def tokenize(string):
    #define tokenizer
    tokenizer = nltk.tokenize.ToktokTokenizer()
    # apply tokenization to the string.
    string = tokenizer.tokenize(string, return_str = True)
    #return tokenized string.
    return string

def stem(string) :
    """This function returns a string in stemmed format."""
    # create our stemming
    ps = nltk.porter.PorterStemmer()
    # split by the default
    stems = [ps.stem(word) for word in string.split()]
    # return to normal
    string = ' '.join(stems)
    return string

def lemmatize(string):
    """This function returns a string with words lemmatized"""
    # create our lemmatizer
    wnl = nltk.stem.WordNetLemmatizer()
    # use a list. comprehension to lemmatize each word
    # string.split() => output a list of every token inside of the document
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    # glue the lemmas back together by the strings we split on
    string= ' '.join(lemmas)
    #return the altered document
    return string

def remove_stopwords (string, extra_words = [], exclude_words = []):
    "This function takes in a string, optional extra_words and exclude_words parameters"
    # assian our stoowords from nltk into stooword list
    stopword_list = stopwords.words('english')
    # utilizing set casting, i will remove any excluded stopwords
    stopword_list = set(stopword_list) - set(exclude_words)
    # add in any extra words to my stopwords set using a union
    stopword_list = stopword_list.union(set(extra_words))
    #split document by spaces
    words = string.split()
    # every word in our document, as long as that word is not in our stopwords
    filtered_words = [word for word in words if word not in stopword_list]
    # glue it back together with spaces, as it was so it shall be
    string_without_stopwords =' '.join(filtered_words)
    # return the document back
    return string_without_stopwords


#importing files from acquire folder
import acquire
#categories chosen
categories = ['world', 'science', 'technology', 'entertainment']
# naming data from acquired folder
news_df = acquire.get_shorts_articles(categories, refresh = False)
# renaming column name
news_df.rename(columns={'contents':'original'},inplace=True)
#  naming data from acquired folder
codeup_df = acquire.blog_articles()
# renaming column name
codeup_df.rename(columns={'content':'original'}, inplace=True)

def prep_article_data(df, column, extra_words = [], exclude_words = []):
    """This function take in a df and the string name for a text column with
    option to pass lists for extra words and exclude words and
    returns a df with the text article title, original text, stemmed text,
    lemmatized text, cleaned, tokenized, & lemmatized text with stopwords removed."""
    df['clean'] = df[column].apply(basic_clean)\
                            .apply(tokenize)\
                            .apply(remove_stopwords, extra_words = extra_words, exclude_words= exclude_words)
    df['stemmed' ] = df['clean'].apply(stem)
    df['lemmatized'] = df['clean'].apply(lemmatize)
    return df[['title', column, 'clean', 'stemmed','lemmatized']]


# example for news df
#prep_article_data(news_df, 'original', extra_words = ['ha'], exclude_words = ['no'])
# example ford codeup_df
# prep_article_data(codeup_df, 'original', extra_words = ['ha'], exclude_words = ['no'])
