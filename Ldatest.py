# -*- coding:utf-8 -*-
# import codecs
from gensim import corpora
from gensim.models import LdaModel
from gensim import models
from gensim import similarities
from gensim.corpora import Dictionary
import gensim
import operator
fr = open('/home/zengxiaosen/storesplitfile/part0001')
train=[]
s = 0
for line in fr.readlines():
    # line = str(list(line)[0:-1])
    line.replace('\n','')
    line.replace('|', '')
    print line
    try:
        line = unicode(line, 'utf-8')
    except:
        continue
    line = line.split(' ')
    # counter[w if isinstance(w, unicode) else unicode(w, 'utf-8')] += 1
    s += len(line)
    train.append(line)
print len(train)
print 'all words number: ', s
dictionary = corpora.Dictionary(train)
print 'dictionary: ', dictionary
print 'dictionary.token2id: ', dictionary.token2id
for word, index in dictionary.token2id.iteritems():
    print word + " 's id is : "+ str(index)
# through dictionary, transform the doc that show by string to the doc's vector that show by id
corpus = [dictionary.doc2bow(text) for text in train]
#print 'corpus: ', corpus

tfidf = models.TfidfModel(corpus)
#print 'tfidf: ', tfidf

corpus_tfidf = tfidf[corpus]
i = 0
for doc in corpus_tfidf:
    print 'doc_', i, ' : ', doc
    i = i + 1

# ======================
vec = [(4, 1), (12, 1)]
print 'tfidf[vec] : ', tfidf[vec]

print 'training lda model......'
lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=50)
ldaOut = lda.print_topics(50)
print ldaOut
corpus_lda = lda[corpus_tfidf]
for doc in corpus_lda:
    print doc
# save model
lda.save('/home/zengxiaosen/model_LDA.model')
