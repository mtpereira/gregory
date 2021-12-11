#!/usr/bin/python3
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path
from zipfile import ZipFile
import git  
import html
import json 
import jwt
import os
import pandas as pd
import pathlib
import requests
import spacy 
import subprocess
import time
load_dotenv()

# Set Variables
GREGORY_DIR = os.getenv('GREGORY_DIR')

# Set the API Server
## If you are running docker-compose.yaml, this is http://localhost:18080/
SERVER = os.getenv('SERVER')
WEBSITE_PATH = os.getenv('WEBSITE_PATH')


now = datetime.now()
datetime_string = now.strftime("%d-%m-%Y_%Hh%Mm%Ss")

# Variables to sign metabase embeds
METABASE_SITE_URL = os.getenv('METABASE_SITE_URL')
METABASE_SECRET_KEY = os.getenv('METABASE_SECRET_KEY')

# Workflow starts

print('''
####
## PULL FROM GITHUB
####
''')
os.chdir(GREGORY_DIR)
## Optional
g = git.cmd.Git(GREGORY_DIR)
output = g.pull()

print(output)

print('''
####
## GET JSON DATA
####
''')

# Get Articles
url = SERVER + 'articles/all'
res = requests.get(url)
file_name = GREGORY_DIR + '/data/articles.json'
with open(file_name, "w") as f:
    f.write(res.text)
file_name = GREGORY_DIR + '/content/developers/articles_' + datetime_string + '.json'
with open(file_name, "w") as f:
    f.write(res.text)
    f.close()
# Get Trials
url = SERVER + 'trials/all'
res = requests.get(url)
file_name = GREGORY_DIR + '/data/trials.json'
with open(file_name, "w") as f:
    f.write(res.text)
    f.close()
file_name = GREGORY_DIR + '/content/developers/trials_' + datetime_string + '.json'
with open(file_name, "w") as f:
    f.write(res.text)
    f.close()

print('''
####
## SAVE EXCEL VERSIONS
####
''')

## ARTICLES
articles_json = pd.read_json('data/articles.json')
articles_json.link = articles_json.link.apply(html.unescape)
articles_json.summary = articles_json.summary.apply(html.unescape)
articles_json.to_excel('content/developers/articles_'+ datetime_string + '.xlsx')

## TRIALS
trials_json = pd.read_json('data/trials.json')
trials_json.link = trials_json.link.apply(html.unescape)
trials_json.summary = trials_json.summary.apply(html.unescape)
trials_json.to_excel('content/developers/trials_' + datetime_string + '.xlsx')


print('''
####
## CREATE ZIP FILES
####

### Articles''')

zipArticles = ZipFile('content/developers/articles.zip', 'w')
# Add multiple files to the zip
print('- content/developers/articles_' + datetime_string + '.xlsx')
print('- content/developers/articles_' + datetime_string + '.json')
print('- content/developers/README.md\n')

zipArticles.write('content/developers/articles_' + datetime_string + '.xlsx')
zipArticles.write('content/developers/articles_' + datetime_string + '.json')
zipArticles.write('content/developers/README.md')

# close the Zip File
zipArticles.close()



print('### Clinical Trials')

zipTrials = ZipFile('content/developers/trials.zip', 'w')
# Add multiple files to the zip
print('- content/developers/trials_' + datetime_string + '.xlsx')
print('- content/developers/trials_' + datetime_string + '.json')
print('- content/developers/README.md\n')
zipTrials.write('content/developers/trials_' + datetime_string + '.xlsx')
zipTrials.write('content/developers/trials_' + datetime_string + '.json')
zipTrials.write('content/developers/README.md')

# close the Zip File
zipTrials.close()

print('\n# delete temporary files')
excel_file = Path('content/developers/articles_' + datetime_string + '.xlsx')
json_file = Path('content/developers/articles_' + datetime_string + '.json')
Path.unlink(excel_file)
Path.unlink(json_file)

excel_file = Path('content/developers/trials_' + datetime_string + '.xlsx')
json_file = Path('content/developers/trials_' + datetime_string + '.json')
Path.unlink(excel_file)
Path.unlink(json_file)

print('''
####
## CREATE ARTICLES
####
''')

# Make sure directory exists or create it
articlesDir = GREGORY_DIR + "/content/articles/"
articlesDirExists = pathlib.Path(articlesDir)

if articlesDirExists.exists() == False:
    articlesDirExists.mkdir(parents=True, exist_ok=True)

# Open articles.json
articles = GREGORY_DIR + '/data/articles.json'
with open(articles,"r") as a:
    data = a.read()

jsonArticles = json.loads(data)

# Set which nlp module to use
## en_core_web_trf is more precise but uses more resources
# nlp = spacy.load('en_core_web_trf')
nlp = spacy.load('en_core_web_sm')
print("Looking for noun phrases")

for article in jsonArticles:

    # Process whole documents
    text = article["title"]
    doc=nlp(text)
    # Analyze syntax
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    # print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    # print("verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])
    # Find named entities, phrases and concepts
    # for entity in doc.ents:
    #     print(entity.text, entity. label)


    # Write a file for each record
    markdownDir = pathlib.Path(articlesDir+str(article["article_id"]))
    markdownDir.mkdir(parents=True, exist_ok=True)

    with open(str(markdownDir)+"/index.md", "w+") as f:
        articledata = "---\narticle_id: " + \
            str(article["article_id"]) + \
            "\ndiscovery_date: " + str(article["discovery_date"]) + \
            "\ndate: " + str(article["discovery_date"]) +\
            "\ntitle: \'" + article["title"] + "\'" +\
            "\nsummary: |" + \
            '\n  ' + article["summary"].replace("\n", "\n  ") +\
            "\nlink: \'" + article["link"] + "\'" +\
            "\npublished_date: " + str(article["published_date"]) + \
            "\narticle_source: " + article["source"] + \
            "\nrelevant: " + str(article["relevant"]) + \
            "\nnounphrases: " + str(noun_phrases) + \
            "\nml_prediction_gnb: " + str(article["ml_prediction_gnb"]) + \
            "\nml_prediction_lr: " + str(article["ml_prediction_lr"]) + \
            "\noptions:" + \
            "\n  unlisted: false" + \
            "\n---\n" + \
            html.unescape(article["summary"])
        # add content to file

        f.write(articledata)
        f.close()

print('''
####
## CREATE TRIALS
####
''')

# Make sure directory exists or create it
trialsDir = GREGORY_DIR + "/content/trials/"
trialsDirExists = pathlib.Path(trialsDir)

if trialsDirExists.exists() == False:
    trialsDirExists.mkdir(parents=True, exist_ok=True)


# Open trials.json
trials = GREGORY_DIR + '/data/trials.json'
with open(trials,"r") as a:
    data = a.read()

jsonTrials = json.loads(data)

for trial in jsonTrials:

    # Process whole documents
    text = trial["title"]

    # Write a file for each record
    markdownDir = pathlib.Path(trialsDir+str(trial["trial_id"]))
    markdownDir.mkdir(parents=True, exist_ok=True)

    with open(str(markdownDir)+"/index.md", "w+") as f:
        trialdata = "---\ntrial_id: " + \
            str(trial["trial_id"]) + \
            "\ndiscovery_date: " + str(trial["discovery_date"]) + \
            "\ndate: " + str(trial["discovery_date"]) + "Z" +\
            "\ntitle: \'" + trial["title"] + "\'" +\
            "\nsummary: |" + \
            '\n  ' + trial["summary"].replace("\n", "\n  ") +\
            "\nlink: \'" + trial["link"] + "\'" +\
            "\npublished_date: " + str(trial["published_date"]) + \
            "\ntrial_source: " + trial["source"] + \
            "\nrelevant: " + str(trial["relevant"]) + \
            "\noptions:" + \
            "\n  unlisted: false" + \
            "\n---\n" + \
            html.unescape(trial["summary"])
        # add content to file

        f.write(trialdata)
        f.close()


print('''
####
## GENERATE EMBED KEYS
####
''')

# Opening JSON file
f = open('data/dashboards.json')
 
# returns JSON object as
# a dictionary
dashboards = json.load(f)
 
# Iterating through the json list
metabase_json = {}
for i in dashboards:
    print("Generating key for dashboard: "+ i)
    payload = { "resource": {"dashboard": i}, "params": { }, "exp": round(time.time()) + (60 * 60)}
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm='HS256')
    iframeUrl = METABASE_SITE_URL + 'embed/dashboard/' + token + '#bordered=true&titled=true'
    entry = "dashboard_" + str(i) 
    metabase_json[str(entry)] = iframeUrl

f.close()

embedsJson = GREGORY_DIR + '/data/embeds.json';
with open(embedsJson, "w") as f:
    f.write(json.dumps(metabase_json))
    f.close()

print('''
####
## BUILD THE WEBSITE
####
''')
args = ("/usr/local/bin/hugo", "-d", WEBSITE_PATH,"--cacheDir", GREGORY_DIR)
popen = subprocess.Popen(args, stdout=subprocess.PIPE, universal_newlines=True)
popen.wait()
output = popen.stdout.read()
print(output)

# print('''
# ####
# ## UPDATE THE SEARCH INDEX 
# ####
# ''')

# from algoliasearch.search_client import SearchClient
# algolia_id = os.getenv('ALGOLIA_ID')
# algolia_key = os.getenv('ALGOLIA_KEY')

# client = SearchClient.create(algolia_id, algolia_key)
# index = client.init_index('gregory')

# index = client.init_index('gregory')
# batch = json.load(open(website_path + '/index.json'))
# index.save_objects(batch, {'autoGenerateObjectIDIfNotExist': True})


