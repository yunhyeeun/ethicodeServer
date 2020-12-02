import csv
import re
import kss

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from konlpy.tag import Okt

okt = Okt()

def morpheme(sentence):
    morphemes = okt.pos(sentence, norm=True, stem=False)
    list = [x[0] for x in morphemes if x[1] not in ['Josa', 'Punctuation']]
    target = " ".join(list)
    
    return target

def cos_similarity(sent_list):
    result = []
    tfidf_vectorizer = TfidfVectorizer()
    corpus_morpheme = [morpheme(x) for x in sent_list]
    for i in range(len(sent_list)):
        for j in range(i + 1, len(sent_list)):
            tmp = [corpus_morpheme[i], corpus_morpheme[j]]
            tfidf_matrix = tfidf_vectorizer.fit_transform(tmp)
            similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
            result.append(similarity[0][0] * 100)
    return result

