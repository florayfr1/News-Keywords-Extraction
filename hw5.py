import en_core_web_lg
from newsapi import NewsApiClient
import pickle
import pandas as pd
from collections import Counter

nlp_eng = en_core_web_lg.load()
'''newsapi = NewsApiClient (api_key='ed4040f2edd548c69f7fb38097dae103')

articles = newsapi.get_everything(q='coronavirus', language='en', from_param='2021-10-01', to='2021-10-20', sort_by='relevancy', page=1, page_size=100)
'''

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
#save_net(articles,filename)
'''pickle.dump(filename, open(filename, 'wb')) #create pickle'''


result_articles = get_net(filename)
'''articles = pickle.load(open(filename, 'rb'))'''


data = pd.DataFrame(columns={'title','desc', 'content'})

data_list = []
for x in result_articles['articles']:
    title = x['title']
    description = x['description']
    content = x['content']
    container = {'title':title,'desc':description, 'content':content}
    data_list.append(container)
df = pd.DataFrame(data_list)
df = df.dropna()
#print(df.head)

def get_keywords_eng(text):
    doc = nlp_eng(text)
    result = []
    pos_tags = ["VERB", "NOUN","PROPN"]
    for token in doc:
        if (token.text in nlp_eng.Defaults.stop_words or token.is_punct):
            continue
        if (token.pos_ in pos_tags):
            result.append(token.text)
    return result

keywords = []
for content in df.content.values:
    keywords.append([('#' + x[0]) for x in Counter(get_keywords_eng(content)).most_common(5)])
df['keywords'] = keywords

df.to_csv("result.csv")