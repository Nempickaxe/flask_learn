
# coding: utf-8

# In[9]:


from flask import Flask, request, make_response
from stemming.porter2 import stem
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans


# In[4]:


app =Flask(__name__)


# In[8]:


def cleanse_text(text):
    if text:
        #white space
        clean = ' '.join(text.split())
        #stemming
        red_text = [stem(word) for word in clean.split()]
        return ' '.join(red_text)
    else:
        return text


# In[10]:

@app.route('/cluster', methods=['POST'])
def cluster():
    data = pd.read_csv(request.files['dataset'])
    
    unstructure = 'text'
    if 'col' in request.args:
        unstructure = request.args.get('col')
        
    no_of_cluster = 2
    if 'no_of_cluster' in request.args:
        no_of_cluster = int(request.args.get('no_of_cluster'))
        
    data = data.fillna('NULL')
    data['clean_sum'] = data[unstructure].apply(cleanse_text)
    
    vectorizer = CountVectorizer(analyzer='word',
                                 stop_words='english')
    
    counts = vectorizer.fit_transform(data['clean_sum'])
    
    kmeans = KMeans(n_clusters=no_of_cluster)
    
    data['cluster_num'] = kmeans.fit_predict(counts)
    data.drop('clean_sum', axis=1, inplace=True)
    
    return 'cool stuff!!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)