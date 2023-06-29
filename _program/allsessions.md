---
layout: page
title: Paper Sessions
description: List of Paper Sessions.
priority: 10
invisible: false
published: true
---
  
<style>
* {
  box-sizing: border-box;
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

Check the list of accepted papers <a href="{{ site.baseurl }}/program/papers/"><strong>[here]</strong></a>.

For information about the location of the sessions check out the [venue page]({{ site.baseurl }}/attending/atvenue/).

<hr>

<table id="myTable">
  <tr class="toprowHeader">
    <th >Date</th>
    <th >Time</th>
    <th >Session Name</th>
  </tr>
 {% for session in site.data.rss2023PaperSessions %}
 <tr session="{{ session.SessionName }}">
    <td>{{ session.Date }}</td>
    <td>{{ session.Time }}</td>
    <td>
      <a href="{{ site.baseurl }}/program/papersession?session={{ session.SessionLink }}">
      {{ session.SessionName }}
      </a>
    </td>
  </tr>
{% endfor %}
</table>

