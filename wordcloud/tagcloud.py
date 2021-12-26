import json
import sqlite3
import pandas as pd
import numpy as np
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


## GET DATA
con = sqlite3.connect('../docker-data/gregory.db')
cur = con.cursor()
nounphrases = cur.execute('select noun_phrases from articles;')

df = pd.read_sql_query("SELECT noun_phrases FROM articles;", con)

words = []

for row in df.noun_phrases:
    try:
        row = json.loads(row)
    except:
        if row != "":
            print(row)
        pass
    for item in row:
        words.append(item)

unique_string=(',').join(words)
print('generating image')
gregory_coloring = np.array(Image.open("gregory_face_big.png"))

# gregory_coloring=np.where(gregory_coloring > 3, 255, gregory_coloring)

wordcloud = WordCloud(
                    width = 1920,
                    height = 900,
                    mask=gregory_coloring,
                    background_color='white',
                    colormap='Blues',
                    contour_width=0).generate(unique_string)

image=plt.figure(figsize=(15,8),frameon=False)
ax = plt.Axes(image, [0., 0., 1., 1.])
ax.set_axis_off()
image.add_axes(ax)
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("tagcloud"+".png", bbox_inches='tight')
plt.show()