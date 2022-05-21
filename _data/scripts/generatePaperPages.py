"""
Script for generating individual paper pages.
"""

import argparse
import codecs
import csv
import os
import shutil

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_program', help='Path to program with group assigments')
    parser.add_argument('outdir', help='Directory for output paper pages')
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    # Read program information
    with open(args.csv_program) as f:
        reader = csv.DictReader(f)
        for row in reader:

          paperID = row['PaperID3']
          filename = os.path.join(args.outdir, paperID + ".md")

          g = open(filename, 'w')
          header = '''---
layout: paper
title: "{}"
invisible: true
---\n'''.format(row["PaperTitle"])

          g.write(header)

          html_head = '''<head>
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

#myTable, #myTableA {
  border-collapse: collapse;
  width: 100%;
  border: 1px solid #ddd;
  font-size: 100%;
}

#myTable th, #myTable td, #myTableA th, #myTableA td {
  text-align: left;
  padding: 12px;
}

#myTable tr, #myTableA tr {
  border-bottom: 1px solid #ddd;
}

#myTable tr.header, #myTable tr:hover, #myTableA tr.header, #myTableA tr:hover {
  background-color: #f1f1f1;
}


#eventcounter1 a {
    font-size: 12px;
    color: #ffffff;
    display: block;
}

#eventcounter1 a:hover {
    text-decoration: none;
}

#eventcounter2 a {
    font-size: 12px;
    color: #ffffff;
    display: block;
}

#eventcounter2 a:hover {
    text-decoration: none;
}

</style>
</head>\n\n'''

          g.write(html_head)

          author_table_head = '''<table width = "95%" style="padding-left: 15px; margin-left: auto; margin-right: 10px;">
<tr><td style = "vertical-align: top; padding-right: 25px;" rowspan="2">\n'''
          g.write(author_table_head)

          authors = row["AuthorNames"].replace('*', '').split(';')
          g.write('''<span style="color:black; font-size: 110%;"><i>\n''')
          for k, author in enumerate(authors):
            idx = author.find('(')
            authorName = author[:idx].strip()
            authorInstitute = author[idx:]

            authorNameString = '''{} '''.format(authorName)
            g.write(authorNameString)

            authorInstituteString = '''<span style="color:gray; font-size: 85%">{}</span>'''.format(authorInstitute)
            g.write(authorInstituteString)

            if k < len(authors) - 1:
              g.write('''<span style="color:gray; font-size: 100%">,</span><br>''')
            g.write('\n')

          g.write('''</i></span>\n''')
          author_table_tail = '''</td>\n\n'''
          g.write(author_table_tail)

          paperIconString = '''<td style="text-align: right;"><a href="http://www.roboticsproceedings.org/rss18/p{}.pdf"><img src="{{{{ site.baseurl }}}}/images/paper_link.png" alt="Paper Website" width = "33"  height = "40"/></a><br></td>
</tr>\n'''.format(row['PaperID3'])
          g.write(paperIconString)

          paperIDString = '''<tr>
<td style="color:#777789; text-align:right; font-size: 75%; margin-right:10px;">Paper&nbsp;#{}</td>
</tr>
</table>\n\n'''.format(row['PaperID3'])
          g.write(paperIDString)

          sessionString = '''<table width="80%" style="margin-top: 20px; margin-left: auto; margin-right: auto;">
  <tr>
    <td style="text-align:center;">{}</td>
  </tr>
</table>
<br>\n\n\n'''.format(row['Session'])
          g.write(sessionString)

          g.write('### Abstract\n')
          g.write(row['Abstract']+'\n')
          g.write('''{: style="color:gray; font-size: 120%; text-align: justified;"}\n\n\n''')

          # navigation bars
          g.write('''<table width="100%" style="margin-top:40px;">
<tr>\n''')

          # previous button
          paperID = int(row['PaperID'])
          if paperID == 1:
            g.write('''    <td style="width: 30%; text-align: center;"> 
<img src="{{ site.baseurl }}/images/blank_icon.png"
       alt="Spacer" width = "142"  height = "90"/> 
            </td>\n''')
          else:
            g.write('''    <td style="width: 30%; text-align: center;"><a href="{{{{ site.baseurl }}}}/program/papers/{:03d}/">
<img src="{{{{ site.baseurl }}}}/images/previous_paper_icon.png"
       alt="Previous Paper" width = "142"  height = "90"/> 
</a> </td>\n'''.format(paperID-1))

          # paper overview
          g.write('''<td style="text-align: center;"><a href="{{ site.baseurl }}/program/papers">
<img src="{{ site.baseurl }}/images/overview_icon.png"
       alt="Paper Website" width = "142"  height = "90"/> 
</a> </td>\n''')

          # next button
          if paperID < 74:
            g.write('''    <td style="width: 30%; text-align: center;"><a href="{{{{ site.baseurl }}}}/program/papers/{:03d}/">
    <img src="{{{{ site.baseurl }}}}/images/next_paper_icon.png"
        alt="Next Paper" width = "142"  height = "90"/>
    </a></td>\n'''.format(paperID+1))
          else:
            g.write('''    <td style="width: 30%; text-align: center;"> 
<img src="{{ site.baseurl }}/images/blank_icon.png"
       alt="Spacer" width = "142"  height = "90"/> 
            </td>\n''')

          g.write(''''</tr>
</table>\n''')
          g.close()

          print(paperID)
    # # Generate paper CSV and pages
    # with open(args.csv_outfile, 'w') as f:
    #     writer = csv.DictWrite

if __name__ == '__main__':
    main()    
