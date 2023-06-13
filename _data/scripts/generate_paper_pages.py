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
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_program', help='Path to program with group assigments')
    parser.add_argument('outdir', help='Directory for output paper pages')
    args = parser.parse_args()

    os.makedirs(args.outdir, exist_ok=True)

    f = open(args.csv_program, 'r')
    fileObject = csv.reader(f)
    total_row_count = sum(1 if row[0]!="" else None for row in fileObject)
    f.close()
    print("Number of rows: ",total_row_count)

    # Read program information
    with open(args.csv_program) as f:
        reader = csv.DictReader(f)

        for row in reader:

          paperID = row['PaperID3']
          filename = os.path.join(args.outdir, paperID + ".md")

          g = open(filename, 'w')

          # Generate HTML header
          header = '''---
layout: paper
title: "{}"
invisible: true
---\n'''.format(row["PaperTitle"])

          g.write(header)


          authors = row["AuthorNames"].replace('*', '').split(',')

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
          paperIconString = '''<div class="paper-pdf">
<div> <a href="http://www.roboticsproceedings.org/rss18/p{}.pdf"><img src="{{{{ site.baseurl }}}}/images/paper_link.png" alt="Paper Website" width = "33"  height = "40"/></a> </div>
<div> <a href="http://www.roboticsproceedings.org/rss18/p{}.pdf">Paper&nbsp;#{}</a> </div>
</div>\n\n'''.format(row['PaperID3'],row['PaperID3'],row['PaperID3'])
          g.write(paperIconString)

          # Write paper session
          sessionString = '''<div class="paper-session">Session {}</div>\n\n\n'''.format(row['Session'])
          g.write(sessionString)
          g.write("\n\n\n")
          g.write('<b style="color: black;">Abstract: </b>')
          g.write(row['Abstract']+'\n')
          g.write('''{: style="color:gray; font-size: 120%; text-align: justified;"}\n\n\n''')

          # Write link to supplementary materials (optional)
          if len(row['Supplementary']) > 0:
              g.write('### Links\n')
              g.write('- [Supplementary materials](%s)\n\n' % row['Supplementary'])

          # Write navigation bars
          g.write('''<div class="paper-menu">\n''')

          # Write previous button
          paperID = int(row['PaperID'])
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
