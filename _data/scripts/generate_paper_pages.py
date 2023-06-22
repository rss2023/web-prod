"""
Script for generating individual paper pages (RSS 2022 format)
python generate_paper_pages.py ../rss2022CameraReady.csv ../../_program/papers

Contact: Yuke Zhu (yukez@cs.utexas.edu)
"""

import argparse
import codecs
import csv
import os
import shutil

def main():
    paperIDName = "PaperID"
    paperTitleName = "PaperTitle"
    authorNamesName = "AuthorNames"
    abstractName = "Abstract"
    sessionName = "SessionName"
    posterName = "PosterID"
    demoName = "Demo"
    supplementaryName = "Supplementary"
    posterSessionName = "PosterSession"
    notesName = "Notes"
    #list of embargo paper ids
    embargo = ["070"]

    parser = argparse.ArgumentParser()
    parser.add_argument('csv_program', help='Path to program with group assigments')
    parser.add_argument('outdir', help='Directory for output paper pages')
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    f = open(args.csv_program, 'r')
    fileObject = csv.reader(f)
    total_row_count = sum(1 if row[1]!="" else None for row in fileObject)
    f.close()
    print("Number of rows: ",total_row_count)

    # Read program information
    with open(args.csv_program) as f:
        reader = csv.DictReader(f)

        for row in reader:
          paperIDValue = "{0:03}".format(int(row[paperIDName]))
          paperID = paperIDValue
          filename = os.path.join(args.outdir, paperID + ".md")

          g = open(filename, 'w')

          # Generate HTML header
          header = '''---
layout: paper
title: "{}"
invisible: true
---\n'''.format(row[paperTitleName])

          g.write(header)


          # authors = row[authorNamesName].replace('*', '').split(',')
          authors = row[authorNamesName].replace('*', '').split(';')

          g.write('''<div class="paper-authors">\n''')
          for author in authors:
            aName = ""
            aUni = ""
            idx = author.find('(')
            if idx != -1:
                aName = author[:idx].strip()
                aUni = author[idx:]
                aUni = aUni[1:-1]
            else:
                aName = author.strip()
            authorString = '''<div class="paper-author-box">
    <div class="paper-author-name">{}</div>
    <div class="paper-author-uni">{}</div>
</div>
'''.format(aName,aUni)
            g.write(authorString)
          
          g.write('''\n</div>''')
          # Write link to paper PDF
          # <div> <a href="http://www.roboticsproceedings.org/rss19/p{}.pdf">Paper&nbsp;#{}</a> </div>
          paperIconString = '''<div class="paper-pdf">
<div> <a href="http://www.roboticsproceedings.org/rss19/p{}.pdf"><img src="{{{{ site.baseurl }}}}/images/paper_link.png" alt="Paper Website" width = "33"  height = "40"/></a> </div>
</div>\n\n'''.format(paperIDValue,paperIDValue,paperIDValue)
          if paperIDValue not in embargo:
            g.write(paperIconString)

          # Write paper session
          # session = row[notesName].split(";")[0]
          # sessionString = '''<div class="paper-session">Session: {}</div>\n\n\n'''.format(session)
          # g.write("### Session: "+session+"\n{: style=\"text-align: center;\"}\n\n")
          # if row[notesName].split(";")[1] != "":
          #   g.write("### "+row[notesName].split(";")[1]+"\n{: style=\"margin-top: 10px; color: #428bca; text-align: center;\"}\n\n")
          # if row[notesName].split(";")[2] != "":
          #   g.write("### Nominated for "+row[notesName].split(";")[2]+" Paper\n{: style=\"margin-top: 10px; color: #428bca; text-align: center;\"}\n\n")
          
          g.write("### Paper ID "+row[paperIDName] +"\n{: style=\"margin-top: 10px; text-align: center;\"}\n\n")
          # g.write("### Session "+row[sessionName]+"\n{: style=\"text-align: center;\"}\n\n")
          
          g.write("### [Session "+row[sessionName]+"]({{ site.baseurl }}/program/papersession?session="+row[sessionName].replace(' ','%20').replace('&','%26')+")\n{: style=\"text-align: center;\"}\n\n")



          if row[demoName] != "":
            g.write("### "+row[demoName].title() +"\n{: style=\"margin-top: 10px; color: #555555; text-align: center;\"}\n\n")
          g.write("#### Poster Session "+row[posterSessionName] +"\n{: style=\"margin-top: 10px; color: #555555; text-align: center;\"}\n\n")
          if row[posterName] != "":
            g.write("#### Poster "+row[posterName]+"\n{: style=\"margin-top: 10px; color: #555555; text-align: center;\"}\n\n")



          g.write('<b style="color: black;">Abstract: </b>')
          g.write(row[abstractName]+'\n')
          g.write('''{: style="color:gray; font-size: 120%; text-align: justified;"}\n\n\n''')

          # Write link to supplementary materials (optional)
          try:
              if len(row[supplementaryName]) > 0:
                  g.write('### Links\n')
                  g.write('- [Supplementary materials](http://www.roboticsproceedings.org/rss19/%s)\n\n' % row[supplementaryName])
          except:
            pass

          # Write navigation bars
          g.write('''<div class="paper-menu">\n''')

          # Write previous button
          paperID = int(paperIDValue)
          if paperID == 1:
            g.write('''<img src="{{ site.baseurl }}/images/blank_icon.png" alt="End of Program" title="End of Program"/>\n''')
          else:
            g.write('''<a href="{{{{ site.baseurl }}}}/program/papers/{:03d}/"> <img src="{{{{ site.baseurl }}}}/images/previous_paper_icon.png" alt="Previous Paper" title="Previous Paper"/> </a>\n'''.format(paperID-1))

          # Write paper overview
          g.write('''<a href="{{ site.baseurl }}/program/papers"><img src="{{ site.baseurl }}/images/overview_icon.png" alt="All Papers" title="All Papers"/> </a>\n''')

          # Write next button (TODO: remove magic number 74!)
          #ASSUMES THAT PAPER ID's FOLLOW CONVENTION [1...NUM-PAPERS-1]
          if paperID < total_row_count-1:
            g.write('''<a href="{{{{ site.baseurl }}}}/program/papers/{:03d}/"> <img src="{{{{ site.baseurl }}}}/images/next_paper_icon.png" alt="Next Paper" title="Next Paper"/> </a>\n'''.format(paperID+1))
          else:
            g.write('''<img src="{{ site.baseurl }}/images/blank_icon.png" alt="End of Program" title="End of Program"/> \n''')

          g.write('''\n</div>\n''')
          g.close()

          print(paperID)
    # # Generate paper CSV and pages
    # with open(args.csv_outfile, 'w') as f:
    #     writer = csv.DictWrite

if __name__ == '__main__':
    main()    
