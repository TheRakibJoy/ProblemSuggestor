import pandas as pd
import numpy as np
ds = pd.read_csv('CMtoMaster.csv')
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
vectors = cv.fit_transform(ds['Tags']).toarray()
cv.get_feature_names_out()
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity(vectors)
def recommend(weak_tags):
    vectors = cv.fit_transform([weak_tags]+ds['Tags'].tolist()).toarray()
    similarity = cosine_similarity(vectors)
    distance = similarity[0]
    my_list = sorted(list(enumerate(distance)),reverse=True,key= lambda x:x[1])[1:3]
    problem_list=list()
    for x in my_list:
        problem_list.append(x[0]-1)
    return problem_list

res = recommend("dp, constructivealgorithms")
cnt=1;
for i in res:
    print("Problem ",cnt)
    cnt+=1
    print("Contest ID : ",ds['ID'][i])
    print("Problem No. : ",ds['Index'][i])
    print("Rating : ",ds['Rating'][i])
    print("Tags : ",ds['Tags'][i])
    print("")
