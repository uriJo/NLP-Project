from konlpy.tag import Komoran
import numpy as np
komoran = Komoran()
text = "오늘 날씨는 구름이 많아요"

nouns = komoran.nouns(text)
print(nouns)

dics = {}
for word in nouns:
    if word not in dics.keys():
        dics[word] = len(dics) #0, 1, 2
print(dics)

#one-hot-encoding
nb_classes = len(dics)
targets = list(dics.values())
one_hot_targets = np.eye(nb_classes)[targets]
print(one_hot_targets)