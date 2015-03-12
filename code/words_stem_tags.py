#! /usr/bin/env python
# encoding: utf-8

"""
Copyright (c) 2014-2015 ourren
author: ourren <i@ourren.com>
"""
import nltk

def sentence_stem(sentences):
    for sent in sentences:
        # Porter
        porter = nltk.PorterStemmer()
        words = [porter.stem(word) for word in sent]
        print words

        # Lancaster
        lancaster = nltk.LancasterStemmer()
        lwords = [lancaster.stem(t) for t in sent]
        print lwords

        # WordNet
        wnl = nltk.WordNetLemmatizer()
        wwrods = [wnl.lemmatize(t) for t in sent]
        print wwrods

def sentence_pos(sentences):
    for sent in sentences:
        words = nltk.pos_tag(sent)
        print words

def main():
    print 'enter main...'
    sentence = "Listen, strange women lying in ponds distributing swords. Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony"
    sentences = nltk.sent_tokenize(sentence)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    # stem
    sentence_stem(sentences)

    # pos_tag
    sentence_pos(sentences)


if __name__ == "__main__":
    main()