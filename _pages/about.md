---
layout: about
permalink: /
title: "Shu Chen"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a PhD student in the Department Computer Science at Brown University, where I'm advised by Prof. Ugur Cetintemel. I received my Master's degree from University of Pennsylvania and my Bachelor's degree from University of Waterloo. Prior to joining Brown University, I worked as a Software Engineer at Huawei and Tencent for three years. 

My work has leveraged techniques from machine learning, data management systems, parallel and distributed systems. I am interested in machine learning for computer systems, especially database systems. The goal of my research is to enhance traditional core system components using ML.

## News
{% assign all_posts = site.posts | concat: site.talks | sort: 'date' | reverse %}
{% for post in all_posts limit:4 %}
* **{{ post.date | date: "%b %Y" }}** - {{ post.title }}{% if post.venue %} at {{ post.venue }}{% endif %}
{% endfor %}

## Research Projects
My current and past research projects include:

* **Deep Reinforcement Learning on Cache Replacement Algorithm**  
  Developing intelligent caching strategies using deep RL techniques.

* **Deep Learning on Cardinality Estimation**  
  Improving query optimization through ML-based cardinality estimation.

* **Deep Reinforcement Learning on Query Optimization**  
  Enhancing query planning and execution using reinforcement learning.

* **Key-Value separated LSM-tree**  
  Optimizing LSM-tree structure for better performance in key-value stores.

## Contact
If you are interested in my research, please email me at [shu_chen@brown.edu](mailto:shu_chen@brown.edu).


