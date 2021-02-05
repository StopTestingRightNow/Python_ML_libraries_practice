#!/usr/bin/env python
# coding: utf-8

# Импортируйте библиотеку Pandas и дайте ей псевдоним pd. Создайте датафрейм authors со столбцами author_id и author_name, в которых соответственно содержатся данные: [1, 2, 3] и ['Тургенев', 'Чехов', 'Островский'].
# Затем создайте датафрейм book cо столбцами author_id, book_title и price, в которых соответственно содержатся данные:  
# [1, 1, 1, 2, 2, 3, 3],
# ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
# [450, 300, 350, 500, 450, 370, 290].

# In[2]:


import pandas as pd
import numpy as np

authors = pd.DataFrame({
    "author_id": [1, 2, 3],
    "author_name": ['Тургенев', 'Чехов', 'Островский']
})

book = pd.DataFrame({
    "author_id": [1, 1, 1, 2, 2, 3, 3],
    "book_title": ['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
    "price": [450, 300, 350, 500, 450, 370, 290]
})


# Получите датафрейм authors_price, соединив датафреймы authors и books по полю author_id

# In[16]:


authors_price = pd.merge(authors, book, on="author_id")
authors_price


# Создайте датафрейм top5, в котором содержатся строки из authors_price с пятью самыми дорогими книгами.

# In[17]:


top5 = authors_price.nlargest(5,'price')
top5


# Создайте датафрейм authors_stat на основе информации из authors_price. В датафрейме authors_stat должны быть четыре столбца:
# author_name, min_price, max_price и mean_price,
# в которых должны содержаться соответственно имя автора, минимальная, максимальная и средняя цена на книги этого автора.

# In[26]:


authors_group = authors_price.groupby("author_name")
authors_stat = pd.DataFrame()
authors_stat ["min_price"] = authors_group ["price"].min()
authors_stat ["max_price"] = authors_group ["price"].max()
authors_stat ["mean_price"] = authors_group ["price"].mean()

authors_stat

