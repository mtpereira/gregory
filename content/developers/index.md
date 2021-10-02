---
title: "Developers"
subtitle: "There is an API to query the MS Database that you can use for free."
date: 2021-08-11T15:27:16+01:00
lastmod: 
author: Bruno Amaral
options:
  unlisted: false
  header: mini

description: 
categories: []
tags: []

url: api
layout: page

menu:
  main:
    Name: Developers
    Weight: 5

draft: false
enableDisqus : true
enableMathJax: false
disableToC: false
disableAutoCollapse: true

resources:
  - src: lagos-techie-kwzWjTnDPLk-unsplash.jpeg
    name: header
---

<div class="col-md-6 mx-auto">

## API Endpoints

### Articles

`https://api.gregory-ms.com/articles/all` : Lists all articles.

<strong>Example: </strong> <a href="https://api.gregory-ms.com/articles/all">https://api.gregory-ms.com/articles/all</a>

`https://api.gregory-ms.com/articles/by-date/{year}/{month}` : List articles for specified {year} and {month}. 

<strong>Example: </strong> <a href="https://api.gregory-ms.com/articles/by-date/2021/06">https://api.gregory-ms.com/articles/by-date/2021/06</a>

`https://api.gregory-ms.com/articles/id/{ID}` : List article that matches the {ID} number.

<strong>Example: </strong> <a href="https://api.gregory-ms.com/articles/id/19">https://api.gregory-ms.com/articles/id/19</a>

`https://api.gregory-ms.com/articles/keyword/{keyword}` : List all articles by keyword.

<strong>Example: </strong> <a href="https://api.gregory-ms.com/articles/keyword/myelin">https://api.gregory-ms.com/articles/keyword/myelin</a>

`https://api.gregory-ms.com/articles/relevant` : List all relevant articles.

<strong>Example: </strong> <a href="https://api.gregory-ms.com/articles/relevant">https://api.gregory-ms.com/articles/relevant</a>

#### Articles' Sources

`https://api.gregory-ms.com/articles/source/{source}` : List all articles from specified {source}.

<strong>Example: </strong> <a href="https://api.gregory-ms.com/articles/source/pubmed">https://api.gregory-ms.com/articles/source/pubmed</a>

`https://api.gregory-ms.com/articles/sources` : List all available sources.

<strong>Example: </strong> <a href="https://api.gregory-ms.com/articles/sources">https://api.gregory-ms.com/articles/sources</a>

### Trials

`https://api.gregory-ms.com/trials/all` : List all trials.

<strong>Example: </strong> <a href="https://api.gregory-ms.com/trials/all">https://api.gregory-ms.com/trials/all</a>

`https://api.gregory-ms.com/trials/keyword/{keyword}` : List all trials by keyword.

<strong>Example: </strong> <a href="https://api.gregory-ms.com/trials/keyword/myelin">https://api.gregory-ms.com/trials/keyword/myelin</a>

#### Trials' Sources

`https://api.gregory-ms.com/trials/source/{source}` : List all trials from specified {source}.

<strong>Example: </strong> <a href="https://api.gregory-ms.com/trials/source/pubmed">https://api.gregory-ms.com/trials/source/pubmed</a>

`https://api.gregory-ms.com/trials/sources` : List all available sources.

<strong>Example: </strong> <a href="https://api.gregory-ms.com/trials/sources">https://api.gregory-ms.com/trials/sources</a>


## Database strucuture

### Articles

The JSON response contains information on scientific articles retrieved from multiple academic sources, with the following information for each article:

- **article_id**: The ID of the article
- **discovery_date**: The date this record was retrieved from its source
- **link**: The link to the original content
- **ml_prediction_gnb**: A value of 0 or 1 if the article is relevant according to a Gaussian Naive Bayes model
- **ml_prediction_lr**: A value of 0 or 1 if the article is relevant according to a Logistic Regression model
- **published_date**: The date it was published
- **relevant**: Whether this article is relevant or not (tagged by a human)
- **sent**: A binary value that indicates if the article was sent to the admin. (The admin receives an email digest every 48 hours with the listings to mark them as relevant or not)
- **source**: The source from which the article was retrieved
- **summary**: The abstract or summary of the article
- **table_constraints**: created automatically by SQLite
- **title**: The title of the article

### Trials

- **discovery_date**: The date this record was retrieved from its source
- **link**: The link to the original content
- **published_date**: The date it was published
- **relevant**: Whether it is relevant or not (tagged by a human, and not used at the moment)
- **sent**: A binary value that indicates if the article was sent to the admin. (The admin receives an email digest every 48 hours with the listings to mark them as relevant or not)
- **source**: Website where the found information about this clinical trial
- **summary**: The abstract or summary of the clinical trial
- **table_constraints**: created automatically by SQLite
- **title**: The title of the clinical trial
- **trial_id**: The ID of the clinical trial

</div>