import en_core_web_lg
from newsapi import NewsApiClient
import pickle
import pandas as pd

nlp_eng = en_core_web_lg.load()
newsapi = NewsApiClient (api_key='ed4040f2edd548c69f7fb38097dae103')

articles = newsapi.get_everything(q='coronavirus', language='en', from_param='2021-10-01', to='2021-10-20', sort_by='relevancy', page=5)


def save_net(savedfile,path):
    with open(path, 'wb') as f:
        pickle.dump(savedfile, f)
    #print(f'Pickle file saved for Forum {forum_id} at {path}...')
    return path

def get_net(path):
    with open(path, 'rb') as f:
        load = pickle.load(f)
        #print('retrieved!')
    return load

filename = 'articlesCOVID.pckl'
save_net(articles,filename)
'''pickle.dump(filename, open(filename, 'wb')) #create pickle'''


result_articles = get_net(filename)
'''articles = pickle.load(open(filename, 'rb'))'''
print(result_articles)

'''
data = {}
for i, article in enumerate(articles):
    for x in article['articles']:
        title = x['title']
        description = x['description']
        content = x['content']
        date = x['date']
        data.append({'title':title, 'date':date, 'desc':description, 'content':content})
df = pd.DataFrame(data)
df = df.dropna()
df.head()
'''
