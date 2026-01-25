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



{% comment %} Group theses by the year portion of the date {% endcomment %}
{% assign thesesByYear = site.theses | group_by_exp: "item", "item.date | date: '%Y'" | sort: "name" | reverse %}

{% for year in thesesByYear %}
  <section class="year-group">
    <h2>{{ year.name }}</h2>
    <hr>

    {% for thesis in year.items %}
      <div class="thesis-entry" style="margin-bottom: 2rem;">
        <h3 style="margin-bottom: 0.5rem;">{{ thesis.title }}</h3>
        <p><strong>{{thesis.author}}</strong> | {% if thesis.url %}
            | <a href="{{ thesis.url }}" target="_blank">Read the full abstract</a>{% endif %}
        </p>
        
        <div class="thesis-content">
          {{ thesis.content }}
        </div>
      </div>
    {% endfor %}
  </section>
{% endfor %}