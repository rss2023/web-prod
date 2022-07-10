---
layout: default
title: Home
---
<h1 class="page-title">{{ site.title }}<br>
June 27&ndash;July 1, 2022</h1>

<p><br /></p>
<center>
<table width="100%" style="border: solid #aaa 3px; background:#444;">
<tr><td>
<br />
<h2><b><center><span style="color: #fff">RSS 2022 is now over! If you missed it, you can watch all of the paper presentations and keynote talks on <a href="https://youtube.com/playlist?list=PLG0LjilbrcCbEmRZuP5yxvUCSTieqmJnn">our YouTube playlist</a>.</span></center></b></h2>
<br />
</td></tr>
</table>
</center>
<p><br /></p>


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
* Please see the [Attending RSS](https://roboticsconference.org/attending/) page for information for conference attendees.
* Please follow us on our [LinkedIn](https://www.linkedin.com/in/rss-conference-99b28823b/) and [Twitter](https://twitter.com/RoboticsSciSys) pages.
* Review our [Covid-19 policies](attending/covid/).
* With great pleasure we announce the two [keynote speakers](program/keynote/) for RSS this year.
* The list of [accepted papers](program/papers/) is available now.
* [The program](program/overview/) and [list of workshops](program/workshops/) are now available.
* [Standard registration](attending/registration/) is available until June 2.


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

### RSS Sponsors


<table width="75%" style="margin-right: auto;">
<tr>
<td style="width: 20%; text-align: center;">
<a href="https://www.amazon.science/">
  <img height="75px" src="{{ site.baseurl }}/images/sponsors/Amazon-Robotics-logo.png"
       alt="Amazon Robotics"/></a>
</td>
<td style="width: 20%; text-align: center; padding-bottom: 18px;">
<a href="http://www.tri.global/">
  <img height="75px" src="{{ site.baseurl }}/images/sponsors/tri.png"
       alt="Toyota Research Institute"/> </a>
</td>
</tr>
<tr>

<td style="text-align: center;">
<a href="https://www.dexterity.ai/">
  <img height="90px;" src="{{ site.baseurl }}/images/sponsors/Dexterity-logo.png"
       alt="Dexterity"/> </a>
</td>

<td style="text-align: center; padding-bottom: 18px;">
<a href="https://www.rtx.com/our-company/what-we-do/transformative-technologies/rtrc">
  <img height="80px;" src="{{ site.baseurl }}/images/sponsors/RTX_RTRC_logo.png"
       alt="Raytheon"/> </a>
</td>
</tr>

<tr>
<td style="text-align: center;">
<a href="https://www.merl.com/">
  <img height="85px" src="{{ site.baseurl }}/images/sponsors/merl.png"
       alt="MERL"/> </a>
</td>
<td style="text-align: center; padding-bottom: 15px;">
<a href="https://zoox.com/">
  <img height="100px" src="{{ site.baseurl }}/images/sponsors/Zoox-logo.png"
       alt="Zoox"/> </a>
</td>
</tr>

<tr>
  <td style="text-align: center; padding-bottom: 15px; padding-top: 5px">
  <a href="https://www.lockheedmartin.com/en-us/index.html">
    <img height="85px" src="{{ site.baseurl }}/images/sponsors/LM-logo.png"
         alt="Lockheed Martin"/> </a>
  </td>
<td style="text-align: center; padding-bottom: 15px; padding-top: 5px">
<a href="https://intrinsic.ai/">
  <img height="45px" src="{{ site.baseurl }}/images/sponsors/Intrinsic-logo.png"
       alt="Intrinsic"/> </a>
</td>
</tr>

<tr>
<td style="padding-bottom:60px;">
&nbsp;
</td>
</tr>

</table>

<table width="75%" style="margin-left: 0%; margin-right: auto;">
<tr>
<td style="width: 30%; text-align: left; padding-bottom: 18px; padding-right: 10px;">
  <img height="200px" src="{{ site.baseurl }}/images/ColumbiaCREA.MorningsideAerial.jpg"
       alt="Columbia Daytime"/>
</td>
<td style="width: 30%; text-align: left; padding-bottom: 18px;">
  <img height="200px" src="{{ site.baseurl }}/images/ColumbiaCampusAndCityFromNWCB.Night.jpg"
       alt="Columbia Night"/>
</td>
</tr>
</table>

The website of the 2021 RSS conference can be found [here](https://roboticsconference.org/2021/).

<tr>
<td style="padding-bottom:60px;">
&nbsp;
</td>
</tr>
