#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 08:37:52 2022

@author: romanticcircles
"""
#installed the flashtext library using the pip install function in the command line
from collections import Counter
import flashtext
with open ('middlemarch.txt', 'r') as book:
    content= book.read()
#I generated this txt file using Project Gutenburg's electronic version of Middlemarch: https://www.gutenberg.org/ebooks/145
#I also used the following website to convert the file from html to txt: https://www.textfixer.com/html/html-to-text.php
processor= flashtext.KeywordProcessor()
processor.add_keyword('body') 
processor.add_keyword("stature")
processor.add_keyword("bearing")
processor.add_keyword("bodily")
processor.add_keyword("ride")
processor.add_keyword("riding")
processor.add_keyword("horseback")
processor.add_keyword("walk")
processor.add_keyword("walking")
processor.add_keyword("wander")
processor.add_keyword("ramble")
processor.add_keyword("amble")
processor.add_keyword("leg") 
processor.add_keyword("run")
processor.add_keyword("ran") 
processor.add_keyword("foot") 
processor.add_keyword("feet") 
processor.add_keyword("figure")
processor.add_keyword("gait")
processor.add_keyword("toddle")
processor.add_keyword("trip")
processor.add_keyword("form")
processor.add_keyword("move")
processor.add_keyword( "leap")
processor.add_keyword("frame")
processor.add_keyword("loiter") 
processor.add_keyword("limb")
processor.add_keyword("exercise")
processor.add_keyword("step")
processor.add_keyword("muscle")
processor.add_keyword("face")
processor.add_keyword("smile")
processor.add_keyword("smiling")
processor.add_keyword("eyes")
processor.add_keyword("cheek") 
processor.add_keyword("face",)
processor.add_keyword("expression")
processor.add_keyword("complexion")
processor.add_keyword("blush")
processor.add_keyword("profile")
processor.add_keyword ("features")
processor.add_keyword ("pale")
processor.add_keyword ("hair")
processor.add_keyword("nose")
processor.add_keyword("mouth")
processor.add_keyword("phsiognamy")
processor.add_keyword("head") 
processor.add_keyword("lip")
processor.add_keyword("chin")
processor.add_keyword("eyelid")
processor.add_keyword("neck") 
processor.add_keyword("frown")
processor.add_keyword("forehead")
processor.add_keyword("wrist")
processor.add_keyword("hand")
processor.add_keyword("finger")
processor.add_keyword("grasp")
processor.add_keyword("write")
processor.add_keyword("thumb")
processor.add_keyword("sew")
processor.add_keyword("glove")
processor.add_keyword("arm")
processor.add_keyword("elbow")
processor.add_keyword("handle")
processor.add_keyword("handling")
processor.add_keyword("cling")
processor.add_keyword("clasp") 
processor.add_keyword("hold")
processor.add_keyword("held")
processor.add_keyword("palm")
processor.add_keyword("knit")
processor.add_keyword("shake") 
processor.add_keyword("carry")
processor.add_keyword("caress")
processor.add_keyword("manipulate")
#While it would have been cleaner (and more powerful) to reate a keyword dictionary, I struggled to get this code to run and ended up adding in each keyword individually in order to move along with the project
print(processor.extract_keywords(content))
print(Counter(processor.extract_keywords(content)))


#this code comes from this source: https://github.com/r3ap3rpy/python/blob/master/flashtextdemo/flashprocessor.py
 #Non ordered data set. Keys and then values. You index by using the key. someDict[“Body”][0]





