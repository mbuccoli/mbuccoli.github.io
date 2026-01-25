---
layout: page
permalink: /theses/
title: theses
description: List of theses I co-supervised..
nav: true
nav_order: 6
---

Theses since 2019 were conducted as internships at BdSound S.r.l. Apply <a href="http://bdsound.com/your-thesis">here</a> to be the next one.

Theses before 2019 were conducted as a PhD student or post-doc at Politecnico di Milano.



{% comment %} 1. Pull the collection and group by the year part of the date {% endcomment %}
{% assign thesesByYear = site.theses | group_by_exp: "item", "item.date | date: '%Y'" %}

{% comment %} 2. Loop through each year group (sorted by year name) {% endcomment %}
{% for year in thesesByYear %}
  <h2>{{ year.name }}</h2>
  <ul>
    {% comment %} 3. Loop through the items within that specific year {% endcomment %}
    {% for thesis in year.items %}
      <li>
        <strong>{{ thesis.date | date: "%b %d" }}:</strong> 
        <a href="{{ thesis.url }}">{{ thesis.title }}</a>
      </li>
    {% endfor %}
  </ul>
{% endfor %}