---
layout: page
title: Workshops
description: Workshop times, venues, and details.
days: ['Mon', 'Fri']
invisible: true
published: false
---



Workshops will take place across two days of the conference on June 27 and July 1, 2022. 
{% comment %}
They are generally scheduled to take place between 7:00AM PST and 11:15PM PST (14:00-18:15 UCT), 
and are recommended to have coffee breaks from 9:15-9:30AM and 11:15-11:30AM PST. 
{% endcomment %}
Each workshop is organized as a semi-independent event, and has a unique schedule reflecting the
planned activities, constraints and preferences of the organizers.
Please check the workshop websites for more details on their particular schedules.

{% comment %}
[Here]({{ site.baseurl }}/docs/campusmap.pdf) is a labeled map of the workshop buildings.
{% endcomment %}


{% for day in page.days %}

<a name="{{ day }}"><span style="color:white; font-size:50px;">&nbsp;</span></a>
{% if day == 'Mon' %}
### Monday, June 27
{% assign innerdays = "27th, 12-13, tbd" | split: ", " %}
{% elsif day == 'Fri' %}
### Friday, July 1
{% assign innerdays = "1st, tbd" | split: ", " %}
{% endif %}

<table class="table table-striped table-workshop" id="{{ day }}ID">
  <thead>
    <tr>
      <th width="7%" align="center">ID</th>
      <th width="15%" align="center">Location</th>
      <th width="50%">Title</th>
      <th width="28%">Organizers</th>
    </tr>
  </thead>
  <tbody>
    {% for innerday in innerdays %}
    {% for workshop in site.data.workshops %}
    {% if workshop.date contains innerday %}

    <tr>
      <td><span style="font-weight:bold; color: #3a3946;"> {{ workshop.external_id }} </span></td>
      <td>{{ workshop.location }} &nbsp; <span style="font-size:smaller; line-height:0.9; display:block;">{{ workshop.note }}</span> </td>
      <td>
        <a href="{{ workshop.url }}">
          {{ workshop.title }}
        </a>
      </td>
      <td style="font-size:smaller;">
        {{ workshop.organizers | replace: ',', '<br/>' | truncatewords: 7, "&nbsp;<button type='button' class='collapsible' style='border:none;background:none;font-size:smaller;color:#222299;'>...more&gt;</button>"}}
      <div class="content" style="display:none; padding-top:20px;">
        {{ workshop.organizers | replace: ',', '<br/>'}}
      </div>
      </td>     
    </tr>
    {% elsif workshop.date contains "?" and innerday contains 'tbd' %}
    <tr>
      <td>{{ workshop.external_id }}</td>
      <td><span style="color:#aaa;font-size:smaller;text-align:center;">TBD</span></td>
      <td>
        <a href="{{ workshop.url }}">
          {{ workshop.title }}
        </a>
      </td>
      <td style="font-size:smaller;">
        {{ workshop.organizers | replace: ',', '<br/>' | truncatewords: 7, "&nbsp;<button type='button' class='collapsible' style='border:none;background:none;font-size:smaller;color:#222299;'>...more&gt;</button>"}}
      <div class="content" style="display:none; padding-top:20px;">
        {{ workshop.organizers | replace: ',', '<br/>'}}
      </div>
      </td>     
    </tr>
    {% endif %}
    {% endfor %}
    {% endfor %}
  </tbody>
</table>
{% endfor %}

<span style="color:white; font-size:50px;">&nbsp;</span><br>
<span style="color:white; font-size:50px;">&nbsp;</span><br>
<span style="color:white; font-size:50px;">&nbsp;</span><br>
<span style="color:white; font-size:50px;">&nbsp;</span><br>
<span style="color:white; font-size:50px;">&nbsp;</span><br>


<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    this.style.display = "none";
    var content = this.nextElementSibling;
    //if (content.style.display === "block") {
    //  content.style.display = "none";
    //} else {
    //  content.style.display = "block";
    //}
    var c = this.parentElement;
    c.innerHTML = content.innerHTML;
    });
}
</script>

