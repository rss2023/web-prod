---
layout: default
title: Home
---
<h1 class="page-title">{{ site.title }}<br>
June 27&ndash;July 1, 2022</h1>



{% comment %}
<center>
<table width="100%" style="border: solid #aaa 3px; background:#444;">
<tr><td>
<br />
<h2><b><center><a href="https://pheedloop.com/rss2021/virtual/"><span style="color: #fff">Join the PheedLoop Conference System</span></a></center></b></h2>
<br />
</td></tr>
</table>
</center>
<br>

<center>
<table width="100%" style="border: solid #aaa 3px; background:#444;">
<tr><td>
<br />
<h2><b><center><a href="https://gather.town/invite?token=XEJwMZnl"><span style="color: #fff">
If you're having difficulty with the link above, 
join the interactive poster sessions directly via this link</span></a></center></b></h2>
<br />
</td></tr>
</table>
</center>
<br>




<center>
<div id="player"></div>
</center>

<script>

// 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var player;
function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '390',
        width: '640',
        playerVars: {
            'autoplay': 0
        },
        videoId: 'QiHMAYQ_iz0',
        events: {
            'onReady': onPlayerReady
        }
    });
}

// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
    //player.setPlaybackRate(1.0);
    //event.target.playVideo();
}

</script>

{% endcomment %}





### News and Updates
* [The preliminary program](program/overview/) and [list of workshops](program/workshops/) are now available.
* [Early registration](attending/registration/) is also available at a discount until April 28.


### Call for Participation
The Robotics: Science and Systems has a long history of bringing together
researchers in all areas of robotics from around the world for an engaging and
focused week of single-track presentations, workshops, poster sessions,
tutorials! This year, as always, we solicit your best work.

RSS 2022 will be held in New York City in the week June 27-July 1, 2022.  After two years of virtual conferences due to the Coronavirus pandemic, RSS 2022 is planned as a hybrid conference with substantial in-person activities! We are closely monitoring the developing COVID-19 situation and will make further determinations about the distribution of in-person vs virtual activities as we get closer to the conference date.


### Timeline

<table class="table">
    <thead>
      <tr>
        <th colspan="3">Timeline</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strike>January 29th, 2022</strike></td>
        <td>11:59am <a href="https://time.is/Anywhere_on_Earth">AoE</a></td>
        <td>Paper Submission Deadline</td>
      </tr>
      <tr>
        <td><strike>February 18th, 2022</strike></td>
        <td>11:59pm <a href="https://time.is/Anywhere_on_Earth">AoE</a></td>
        <td>Workshop Submission Deadline</td>
      </tr>
      <tr>
      <td colspan="2"><strike>March 4th, 2022</strike></td>
        <td>Workshop Acceptance Notification</td>
      </tr>
      <tr>
        <td colspan="2"><strike>April 15th, 2022</strike></td>
        <td>Paper Acceptance Notification</td>
      </tr>
      <tr>
        <td colspan="2">June 27th &ndash; July 1st, 2022</td>
        <td>New York City, USA</td>
      </tr>
    </tbody>
  </table>

{% comment %}

### RSS Sponsors


<table width="75%" style="margin-left: 10%; margin-right: auto;">
<tr>
<td style="width: 20%; text-align: center;">
<a href="https://www.amazon.science/">
  <img height="40px" src="{{ site.baseurl }}/images/sponsors/amazon_logo_RGB.png"
       alt="Amazon Robotics"/></a>
</td>
<td style="width: 20%; text-align: center; padding-bottom: 18px;">
<a href="http://www.tri.global/">
  <img height="60px" src="{{ site.baseurl }}/images/sponsors/tri.png"
       alt="Toyota Research Institute"/> </a>
</td>
</tr>
<tr>

<td style="text-align: center;">
<a href="https://global.abb/">
  <img height="48px;" src="{{ site.baseurl }}/images/sponsors/abblogo.png"
       alt="ABB"/> </a>
</td>

<td style="text-align: center; padding-bottom: 18px;">
<a href="https://clearpathrobotics.com/">
  <img height="50px;" src="{{ site.baseurl }}/images/sponsors/Clearpath-Logo-Q309---Short-Run_Colour_Trans.png"
       alt="Clearpath Robotics"/> </a>
</td>
</tr>

<tr>
<td style="text-align: center;">
<a href="https://www.merl.com/">
  <img height="75px" src="{{ site.baseurl }}/images/sponsors/merl.png"
       alt="MERL"/> </a>
</td>
<td style="text-align: center; padding-bottom: 15px;">
<a href="https://www.nvidia.com/en-us/research/">
  <img height="80px" src="{{ site.baseurl }}/images/sponsors/nvidia.png"
       alt="NVDIA"/> </a>
</td>
</tr>

<tr>
<td style="text-align: center;" colspan=2>
<a href="https://waymo.com/">
  <img width="120px" src="{{ site.baseurl }}/images/sponsors/Waymo.png"
       alt="Waymo"/> </a>
</td>
</tr>


<tr>
<td style="padding-bottom:60px;">
&nbsp;
</td>
</tr>

</table>

{% endcomment %}

The website of the 2021 RSS conference can be found [here](https://roboticsconference.org/2021/).
