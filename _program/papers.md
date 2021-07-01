---
layout: page
title: Accepted Papers
description: Accepted papers.
invisible: false
---


<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

#myInput {
  background-position: 10px 10px;
  background-repeat: no-repeat;
  width: 100%;
  font-size: 100%;
  padding: 12px 20px 12px 40px;
  border: 1px solid #ddd;
  margin-bottom: 12px;
}

#myTable {
  border-collapse: collapse;
  width: 100%;
  border: 1px solid #ddd;
  font-size: 100%;
}

#myTable th, #myTable td {
  text-align: left;
  padding: 12px;
}

#myTable tr {
  border-bottom: 1px solid #ddd;
}

#myTable tr.header, #myTable tr:hover {
  background-color: #f1f1f1;
}
</style>
</head>
<body>

<input type="text" id="search" placeholder="Type to search">

<table id="myTable">
  <tr class="toprowHeader">
    <th>Paper ID</th>
    <th>Title</th>
    <th>Authors</th>
  </tr>
 {% for paper in site.data.rss2021CameraReadyIntegration %}
 <tr>
    <td width="8%" height="100px">{{paper.PaperID }}</td>
    <td width="30%" height="100px" > <a href="http://www.roboticsproceedings.org/rss17/p{{paper.PaperID3}}.pdf">{{paper.PaperTitle}}</a></td>
{% comment %}
    <td width="30%" height="100px" > <a href="{{ site.baseurl }}/program/papers/{{ paper.PaperId}}/">{{paper.PaperTitle}}</a></td>
{% endcomment %}
    <td width="30%" height="100px">{{paper.AuthorNames | replace: ';', ','}}</td>
  </tr>
{% endfor %}
</table>

<script>
var $rows = $('#myTable tr');
$('#search').keyup(function() {

    var val = '^(?=.*\\b' + $.trim($(this).val()).split(/\s+/).join('\\b)(?=.*\\b') + ').*$',
        reg = RegExp(val, 'i'),
        text;

    $rows.show().filter(function() {
        text = $(this).text().replace(/\s+/g, ' ');
        return !reg.test(text);
    }).not('.toprowHeader').hide();
});
</script>

</body>
</html>


{% comment %}



<div id="papers" class="row text-center">
    {% for paper in site.data.rss2020_papers %}
    {% capture modulo %}{{ forloop.index0 | modulo:4 }}{% endcapture %}
    {% if modulo == '0' %}<div class="row text-center">{% endif %}
        <div class="col-sm-6">
            <a href="{{ paper.PaperTitle }}">temp</a><br>
		<i>{{ paper.AuthorNames }}</i><br>
        </div>
    {% if modulo == '3' or forloop.last %}</div>{% endif %}
    {% endfor %}
</div>


<ul>
{% for paper in site.data.rss2020_papers %}
<li>
  <a href="{{ site.baseurl }}/program/papers/{{ paper.PaperOrder}}/">
    {{ paper.PaperTitle}}
  </a>
  <br/>
  {{ paper.AuthorNames }}
</li>
<br/>
{% endfor %}
</ul>

<ul>
{% for paper in site.data.papers %}
<li>
  <a href="{{ site.baseurl }}/program/papers/{{ paper.external_id }}/">
    {{ paper.title }}
  </a>
  <br/>
  {{ paper.authors }}
  {% for award in site.data.award_finalists %}
  {% if award.internal_id == paper.internal_id %}
  <br/>
  <b>{{ award.type }} Award {{ award.status }}</b>
  {% endif %}
  {% endfor %}
</li>
<br/>
{% endfor %}
</ul>

{% endcomment %}
