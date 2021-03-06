# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 09:54:50 2016

@author: lenovo
"""

#“Pig Latin”是一个英语儿童文字改写游戏，整个游戏遵从下述规则：

#(1). 元音字母是‘a’、‘e’、‘i’、‘o’、‘u’。字母‘y’在不是第一个字母的情况下，也被视作元音字母。
#其他字母均为辅音字母。例如，单词“yearly”有三个元音字母（分别为‘e’、‘a’和最后一个‘y’）
#和三个辅音字母（第一个‘y’、‘r’和‘l’）。
#(2). 如果英文单词以元音字母开始，则在单词末尾加入“hay”后得到“Pig Latin”对应单词。
#例如，“ask”变为“askhay”，“use”变为“usehay”。
#(3). 如果英文单词以‘q’字母开始，并且后面有个字母‘u’，将“qu”移动到单词末尾加入“ay”后得到“Pig Latin”对应单词。例如，“quiet”变为“ietquay”，“quay”变为“ayquay”。
#(4). 如果英文单词以辅音字母开始，所有连续的辅音字母一起移动到单词末尾加入“ay”后得到“Pig Latin”对应单词。例如，“tomato”变为“omatotay”， “school” 变为“oolschay”，“you” 变为“ouyay”，“my” 变为“ymay ”，“ssssh” 变为“sssshay”。
#(5). 如果英文单词中有大写字母，必须所有字母均转换为小写。 
#输入格式:
#一系列单词，单词之间使用空格分隔。
#输出格式：
#按照以上规则转化每个单词，单词之间使用空格分隔。
#输入样例：
#Welcome to the Python world Are you ready
#输出样例：
#elcomeway otay ethay ythonpay orldway arehay ouyay eadyray

line = str(raw_input('Please enter some words:'))
line = line.lower()#将所有字符串转换为小写的，对应的大写的函数是.upper()
words = line.split()#切片函数，括号空时默认按空格切片
for word in words:
    if word[0] in 'aeiou':
        print word + 'hay', #一个逗号加空格，就把默认换行的操作取消了，使得全部输出都在一行上
    elif word[0] == 'q' and word[1] == 'u':
        print word[2:] + word[:1] + 'ay', 
    else:
        n = 1
        while n >= 1 and word[n] not in 'aeiouy':
            n += 1
        print word[n:] + word[:n] + 'ay', 
            