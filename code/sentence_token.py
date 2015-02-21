#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2013-2014 ourren (http://blog.ourren.com/)
author: ourren <i@ourren.com>
"""

def sentence_split(str_centence):
    list_ret = list()
    for s_str in str_centence.split('.'):
        if '?' in s_str:
            list_ret.extend(s_str.split('?'))
        elif '!' in s_str:
            list_ret.extend(s_str.split('!'))
        else:
            list_ret.append(s_str)
    return list_ret

def main():
    sentence = "I saw Annie who is Dr. Ting's PA and she is amazing!! She was extremely knowledgeable and thorough and knew my skin type right away. She is the only Dr. Who's been able to completely clear up my skin and their product lines are incredible and affordable!!! I will not go to anyone but her now. I recommend seeing Annie for any skin condition- they have every laser there is for every skin disorder there is including broken capillaries! Love this office!"
    print sentence_split(sentence)

if __name__ == '__main__':
    main()