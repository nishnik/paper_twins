from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import json, gensim



# HINDUSTAN TIMES


# CRICKET

f = open('ht_cricket.csv', 'w')
list_of_htnews = []
final_url = 'http://www.hindustantimes.com/cricket' 
response = requests.get(final_url)
html = response.content
source = BeautifulSoup(html)
for division in source.findAll('div', {'class': 'top_single_story_option2_txt'}):
    text = division.text.replace('\n', '')
    text = division.text.replace(',', ';')
    list_of_htnews.append(text)

for division1 in source.findAll('div', {'class': 'top_news_txt'}):
    for link in division1.findAll('a'):
        text = link.text.replace('\n', '')
        text = link.text.replace(',', ';')
        list_of_htnews.append(text)

for division2 in source.findAll('div', {'class': 'list_txt'}):
    for link1 in division2.findAll('a'):
        text = link1.text.replace('\n', '')
        text = link1.text.replace(',', ';')
        list_of_htnews.append(text)

for division3 in source.findAll('div', {'class': 'india_topNews_links'}):
    for link2 in division3.findAll('a'):
        text = link2.text.replace(str('\n'), '')
        text = link2.text.replace(',', ';')
        list_of_htnews.append(text)

to_write = "\n".join(list_of_htnews) 
f.write(to_write.encode('ascii', 'ignore'))
f.close()


# FOOTBALL
f = open('ht_football.csv', 'w')
list_of_htnews = []
final_url = 'http://www.hindustantimes.com/football'
response = requests.get(final_url)
html = response.content
source = BeautifulSoup(html)
for division in source.findAll('div', {'class': 'top_single_story_option2_txt'}):
    text = division.text.replace(',', ';')
    list_of_htnews.append(text)

for division1 in source.findAll('div', {'class': 'top_news_txt'}):
    for link in division1.findAll('a'):
        text = link.text.replace(',', ';')
        list_of_htnews.append(text)

for division2 in source.findAll('div', {'class': 'list_txt'}):
    for link1 in division2.findAll('a'):
        text = link1.text.replace(',', ';')
        list_of_htnews.append(text)

for division3 in source.findAll('div', {'class': 'india_topNews_links'}):
    for link2 in division3.findAll('a'):
        text = link2.text.replace(',', ';')
        list_of_htnews.append(text)

to_write = "\n".join(list_of_htnews) 
f.write(to_write.encode('ascii', 'ignore'))
f.close()


# TENNIS
f = open('ht_tennis.csv', 'w')
list_of_htnews = []
final_url = 'http://www.hindustantimes.com/tennis'
response = requests.get(final_url)
html = response.content
source = BeautifulSoup(html)
for division in source.findAll('div', {'class': 'top_single_story_option2_txt'}):
    text = division.text.replace(',', ';')
    list_of_htnews.append(text)

for division1 in source.findAll('div', {'class': 'top_news_txt'}):
    for link in division1.findAll('a'):
        text = link.text.replace(',', ';')
        list_of_htnews.append(text)

for division2 in source.findAll('div', {'class': 'list_txt'}):
    for link1 in division2.findAll('a'):
        text = link1.text.replace(',', ';')
        list_of_htnews.append(text)

for division3 in source.findAll('div', {'class': 'india_topNews_links'}):
    for link2 in division3.findAll('a'):
        text = link2.text.replace(',', ';')
        list_of_htnews.append(text)


to_write = "\n".join(list_of_htnews) 
f.write(to_write.encode('ascii', 'ignore'))
f.close()



# OTHER SPORTS
f = open('ht_othersports.csv', 'w')
list_of_htnews = []
final_url = 'http://www.hindustantimes.com/other-sports'
response = requests.get(final_url)
html = response.content
source = BeautifulSoup(html)

for division in source.findAll('div', {'class': 'top_single_story_option2_txt'}):   
    text = division.text.replace(',', ';')   
    list_of_htnews.append(text.replace(',', ';'))

for division1 in source.findAll('div', {'class': 'top_news_txt'}):
    for link in division1.findAll('a'):
        text = link.text.replace(',', ';')       
        list_of_htnews.append(text.replace(',', ';'))

for division2 in source.findAll('div', {'class': 'list_txt'}):
    for link1 in division2.findAll('a'):
        text = link1.text.replace(',', ';')    
        list_of_htnews.append(text.replace(',', ';'))

for division3 in source.findAll('div', {'class': 'india_topNews_links'}):
    for link2 in division3.findAll('a'):
        text = link2.text.replace(',', ';')   
        list_of_htnews.append(text.replace(',', ';'))

to_write = "\n".join(list_of_htnews) 
f.write(to_write.encode('ascii', 'ignore'))
f.close()



# TIMES OF INDIA

# FOOTBALL
f = open('toi_football.csv', 'w')
list_of_toinews = []

# NEWS FROM TOP_STORIES
final_url = 'http://timesofindia.indiatimes.com/sports/football'
top_Stories_url = final_url + '/top-stories'
response = requests.get(top_Stories_url)
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# NEWS FROM INTERVIEWS
Interviews_url = final_url + '/interviews'
response = requests.get(Interviews_url)
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# NEWS FROM EPL Top-Stories
epl_url = final_url + '/epl'
response = requests.get(epl_url + '/top-stories')
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# NEWS FROM ChampionsLeague Top-Stories
champion_league_url = 'http://timesofindia.indiatimes.com/sports/football/champions-league/articlelist/40924344.cms'
response = requests.get(champion_league_url)
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# NEWS FROM Copa_America Top-Stories
copa_america_url = 'http://timesofindia.indiatimes.com/sports/Copa-America-2015/articlelist/47642055.cms'
response = requests.get(copa_america_url)
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# NEWS FROM I-LEAGUE TOP_STORIES
i_league_url = final_url + '/i-league'
response = requests.get(i_league_url)
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# NEWS FROM ISL TOP-STORIES
isl_url = 'http://timesofindia.indiatimes.com/sports/football/indian-super-league/top-stories/articlelist/24669705.cms'
response = requests.get(isl_url)
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

to_write = "\n".join(list_of_toinews) 
f.write(to_write.encode('ascii', 'ignore'))
f.close()


# TENNIS

f = open('toi_tennis.csv', 'w')
list_of_toinews = []
# NEWS FROM TOP STORIES
final_url = 'http://timesofindia.indiatimes.com/sports/tennis'
response = requests.get(final_url + '/top-stories')
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# NEWS FROM INTERVIEWS
response = requests.get(final_url + '/interviews')
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# NEWS FROM CHENNAI OPEN
response = requests.get('http://timesofindia.indiatimes.com/sports/tennis/chennai-open-2016/articlelist/49058499.cms')
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# NEWS FROM AUSTRALIAN OPEN TOP_STORIES
response = requests.get('http://timesofindia.indiatimes.com/sports/tennis/australian-open-2016/top-stories/articlelist/50369586.cms')
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# NEWS FROM IPTL
response = requests.get('http://timesofindia.indiatimes.com/sports/tennis/iptl/articlelist/31481400.cms')
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

to_write = "\n".join(list_of_toinews) 
f.write(to_write.encode('ascii', 'ignore'))
f.close()


# CRICKET

f = open('toi_cricket.csv', 'w')
list_of_toinews = []
final_url = 'http://www.cricbuzz.com/?utm_source=TOISports_Cricwidget&utm_medium=ABtest&utm_campaign=TOISports'
response = requests.get(final_url)
html = response.content
source = BeautifulSoup(html)
i = 1
for divisions in source.findAll('div', {'class': 'cb-col-100 cb-lst-itm cb-lst-itm-sm'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

for divisions1 in source.findAll('div', {'class': 'big-crd-main cb-bg-white'}):
    text = divisions1.text
    list_of_toinews.append(text.replace(',', ';'))

for headings in source.findAll('h2', {'div': 'big-crd-hdln'}):
    text = headings.text
    list_of_toinews.append(text.replace(',', ';'))

for headings1 in source.findAll('h2', {'div': 'sml-crd-hdln'}):
    text = headings1.text
    list_of_toinews.append(text.replace(',', ';'))

for divisions2 in source.findAll('div', {'class': 'big-crd-reltd-itm'}):
    text = divisions2.text
    list_of_toinews.append(text.replace(',', ';'))

for divisions3 in source.findAll('div', {'class': 'cb-nws-intr'}):
    text = divisions3.text
    list_of_toinews.append(text.replace(',', ';'))

for divisions4 in source.findAll('div', {'class': 'cb-nws-intr cb-lst-itr-txt'}):
    text = divisions4.text
    list_of_toinews.append(text.replace(',', ';'))

for divisions5 in source.findAll('div', {'class': 'module-content-container'}):
    text = divisions5.text
    list_of_toinews.append(text.replace(',', ';'))

to_write = "\n".join(list_of_toinews) 
f.write(to_write.encode('ascii', 'ignore'))
f.close()


# BADMINTON

f = open('toi_othersports.csv', 'w')
list_of_toinews = []
final_url = 'http://timesofindia.indiatimes.com/sports/badminton'
response = requests.get(final_url)
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))


# HOCKEY
# TOP_STORIES
final_url = 'http://timesofindia.indiatimes.com/sports/hockey'
response = requests.get(final_url + '/top-stories')
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# HOCKEY INDIA LEAGUE TOP_STORIES
hil_url = 'http://timesofindia.indiatimes.com/sports/hockey/hockey-india-league/top-stories/articlelist/18007462.cms'
response = requests.get(hil_url)
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))


# GOLF
# TOP_STORIES
final_url = 'http://timesofindia.indiatimes.com/sports/golf'
response = requests.get(final_url + '/top-stories')
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# GOLF INTERVIEWS NEWS:
response = requests.get(final_url + '/interviews')
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))


# RACING
# TOP_STORIES
final_url = 'http://timesofindia.indiatimes.com/sports/racing'
response = requests.get(final_url + '/top-stories')
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# RACING INTERVIEWS NEWS:
response = requests.get(final_url + '/interviews')
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# NEWS FROM INDIAN-GP:
response = requests.get(final_url + '/indian-gp')
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# NBA
# TOP_STORIES
final_url = 'http://timesofindia.indiatimes.com/sports/nba'
response = requests.get(final_url + '/top-stories')
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# OFF THE COURT
response = requests.get('http://timesofindia.indiatimes.com/sports/nba/off-the-court/articlelist/8014746.cms')
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))


# CHESS
final_url = 'http://timesofindia.indiatimes.com/sports/chess'
response = requests.get(final_url)
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))

# BOXING
final_url = 'http://timesofindia.indiatimes.com/sports/boxing/articlelist/3413166.cms'
response = requests.get(final_url)
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('div', {'id': 'fsts'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))


# MORE_SPORTS
final_url = 'http://timesofindia.indiatimes.com/sports/more-sports'
response = requests.get(final_url)
html = response.content
source = BeautifulSoup(html)
for divisions in source.findAll('td', {'style': 'padding:10px 0px 10px 15px;font-size:13px;height:82px;'}):
    text = divisions.text
    list_of_toinews.append(text.replace(',', ';'))



to_write = "\n".join(list_of_toinews) 
f.write(to_write.encode('ascii', 'ignore'))
f.close()

# MATCHING NEWS 
sports = ["football", "cricket", "tennis", "othersports"]

model = gensim.models.Word2Vec.load_word2vec_format('vec.txt', binary = False)
print ("model loaded")

for sport in sports:
    with open('ht_'+ sport + '.csv') as w:
        ht = w.readlines()

    with open('toi_'+ sport + '.csv') as w:
        toi = w.readlines()


    tokenizer = RegexpTokenizer(r'\w+')
    stop = stopwords.words('english')

    def chk_in_model(b):
        d = []
        for bb in b:
            if bb in model:
                pass
            else:
                continue
            d.append(bb)
        return d

    def clean_ques(query):
        query = query.lower()# converted to lowercase alphabet
        query = tokenizer.tokenize(query) # tokenized
        query = [q for q in query if q not in stop] # removed stop words
        query = chk_in_model(query)
        return query


    def clean_ques_not_stop(query):
    # here query is list of words that are present in the question
        query = query.lower()# converted to lowercase alphabet
        query = tokenizer.tokenize(query) # tokenized
        query = chk_in_model(query)
        return query

    # def wordvec(word):
    #     try:
    #         return model[word]
    #     except KeyError:
    #         pass    
    #     return numpy.zeros(len(model["one"]))   

    print ("Same news in " + sport)
    res = {}
    for a in ht:
        a_c = clean_ques(a)
        dist = -1    
        for b in toi:
            b_c = clean_ques(b)
            n = model.n_similarity(a_c, b_c)
            if n > dist:
                dist = n
                res[a] = b

    for a in res:
        print (a)
        print (res[a])
        print ("====")