#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2013-2014 ourren (http://blog.ourren.com/)
author: ourren <i@ourren.com>
"""
import nltk

def main():
    sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
    tokens = nltk.word_tokenize(sentence)
    print tokens

if __name__ == '__main__':
    main()