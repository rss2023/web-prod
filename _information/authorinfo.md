---
layout: page
title: Author Information
description: Instructions for paper submission.
priority: 8
---


## Submission Instructions
The submissions site at <a href="https://cmt3.research.microsoft.com/RSS2021/"> https://cmt3.research.microsoft.com/RSS2021/</a> will open for submission Feb 1st.

{% comment %}

Browse to [https://cmt3.research.microsoft.com/RSS2021/](https://cmt3.research.microsoft.com/RSS2021/) for submissions.

* **Logging into the system**: If you already have a CMT account, use those credentials to login. If you do not, sign up as a new user.
* **Conflict domains**: When you login for the first time, CMT will prompt you to enter your conflict domains. You will not be allowed to start the submission process without finishing this step.
* **Paper submission**: Enter title, abstract, and authors. Select your primary and secondary [subject areas]({{site.baseurl}}/information/cfp/#subject-areas). Your paper may now be uploaded. Papers must be in the accepted conference style format and must be submitted as a PDF. Papers may be edited, updated and replaced up to the full paper final submission deadline. Answer if your first author is a student (eligible then for the Best Student Paper Award) and select which [Area Chair]({{site.baseurl}}/committees/pc/) might be best suited to handle your submission. Finally, if you want your accepted paper to be considered for invitation to special issues (potentially with expedited review), please give your consent to us forwarding the reviews to the journal editors who decide on such invitations.
* **Paper ID**: After clicking the Submit link, your paper will be assigned an ID.
* **Supplementary material**: Authors may submit supplementary material such as a video or an expanded version of a proof (20MB max, accepted formats: avi, mov, mp4, mpg, pdf, tar, tgz, zip). Please note that the link to upload supplementary material becomes active only after the paper submission is complete.

{% endcomment %}

## Paper Format
{% comment %}
We only accept submissions in PDF. 
Submissions may be up to 8 pages in length, including figures but possibly excluding references. Additional pages can be used for references. However, the 9th page, and any subsequent pages, can contain ONLY references. This will be strictly enforced. Submissions can use a font no smaller than 10 point. Submissions violating these guidelines will not be considered. A paper template is available in <a href="{{site.baseurl}}/docs/paper-template-latex.tar.gz">LaTeX</a> and <a href="{{site.baseurl}}/docs/paper-template-word.zip">Word</a>. Please read the [detailed instructions]({{site.baseurl}}{% post_url 2019-12-04-paper-format%}).
{% endcomment %}

We only accept submissions in PDF. 
A paper template is available in <a href="{{site.baseurl}}/docs/paper-template-latex.tar.gz">LaTeX</a> and <a href="{{site.baseurl}}/docs/paper-template-word.zip">Word</a>.

Do not modify the formatting provided in the templates. Any change to font sizes, page dimensions, line spacing, etc. may delay the publication of your paper. Please do not include any additional markings such as <i>Draft</i> or <i>To appear in...</i> on the pages. Make sure your paper does not contain page numbers. 

Submit a PDF-format paper. We do not accept papers submitted after the deadline
no matter what the reason is, so please check on your ability to convert to PDF
early. Delays in the production of proceedings are usually caused by PDF file
submissions that do not embed all fonts. Please follow the below instructions
to ensure that your PDF document will not suffer from this problem.

When preparing your document in LaTeX, make sure to create the PDF file from
your LaTeX source using these (or equivalent, xelatex or pdflatex) commands:

{% highlight js %}
latex paper.tex
dvips paper.dvi -o paper.ps -t letter -Ppdf -G0
ps2pdf paper.ps 
{% endhighlight %}


The arguments provided to dvips will ensure that all fonts are embedded in the PDF file produced by ps2pdf.


{% comment %}
Here is some additional [detail on formating and presentation]({{site.baseurl}}/information/paperformatting).
{% endcomment %}


## Supplementary Materials
Authors may submit supplementary material such as a video or an expanded version of a proof. The deadline for supplementary material is the same as for paper submission. Note that reviewers are not required to view this material and include it in their assessment of the paper. Lastly, if authors feel they must link to additional supplementary material, they are cautioned to ensure that their identities are not revealed. Please note that the link to upload supplementary material becomes active only after the paper submission is complete.

## Double Blind Submission

Reviewing for RSS 2021 will be double blind, so authors should not be listed on
the title page and reasonable anonymity should be maintained in the paper.
Authors are asked to take particular care when referencing their own work &mdash; 
careless use of self citations can easily violate the requirements for double
blind reviewing and this will result in papers being rejected. 

Double Blind reviewing requires that the paper reviewers should not know the names or affiliation of the paper authors. This is desirable to remove any possible or perceived bias toward a paper on non technical grounds. However, in practice this is difficult to achieve in full as descriptions of background material or experiments, which are essential to the technical content of the paper, often give a clear indication to knowledgeable reviewers of the likely source of the paper. RSS 2021 will try to adopt a pragmatic approach to double blind reviewing in which authors are encouraged to hide identity without unduly affecting the quality or import of their submission.

The following general principles should be applied in submissions:

* Authors names and affiliations should not be cited in the title or text of the submission.
* Acknowledgments to people or funding agencies should not appear in the submission.
* Citing of web links to the authors or author's institute should be avoided.

In self citing authors previous work, avoid expressions such as "In the authors earlier work...", rather use alternative expressions such as "In previous work..." or "In related work...", in a manner that does not distinguish their own work from the work of others. Authors should otherwise cite work, including their own, as required for the completeness of the submission.

In presentation of experimental work, avoid logos in pictures, or overt references to an individual laboratory. Use expressions such as "The experimental equipment..." rather than "The University of XYZ's Robby the Robot...". Otherwise authors should include photographs, graphics and other presentation material as in the normal manner for a paper submission.

In general authors should avoid obviously attributable self-references while ensuring that the paper is complete, makes appropriate citations of related work and fully describes the contributions made.


## Multiple Submissions
Submissions that are identical (or substantially similar) to versions that have
been previously published, or accepted for publication, or that have been
submitted in parallel to other conferences are not appropriate for RSS and
violate our dual submission policy. 
Exceptions to this rule are the following:

1. Submission is permitted of a short version of a paper that has been submitted to a journal, but has not yet been published in that journal. Authors must declare such dual-submissions either through the paper upload submission form, or via email to the program chair. It is the authors' responsibility to make sure that the journal in question allows dual concurrent submissions to conferences.
2. Submission is permitted for papers presented or to be presented at conferences or workshops without proceedings, or with only abstracts published.
3. It is acceptable to submit to RSS work that has been made available as a technical report (or similar, e.g. in arXiv) without citing it.

None of the above override the requirements of other publishing venues. In addition, keep in mind that author anonymity to RSS reviewers might be compromised for authors availing themselves of exceptions 2 and 3.


## Plagiarism
RSS is utterly intolerant of plagiarism. Submitted papers are expected to contain original work executed by the authors with adequate, proper and scholarly citations to the work of others. It is the job of the authors to clearly identify both their own contribution(s) and also published results / techniques on which they depend or build. RSS reviewers are charged to ensure these standards are met. In cases of alleged plagiarism, the program chair will be guided by Section 8.2.4 Allegations of Misconduct as laid out by the IEEE in this <a href="{{site.baseurl}}/docs/opsmanual.pdf">document</a>.

## Review Process
Authors, Program Committee members, and Area Chairs will all be anonymous. Each paper will receive 3 reviews.
Consistent with last year, we will not have conditional acceptances, nor will we have a full author-to-reviewer rebuttal process,
instead we will keep the opportunity to write a post-review response to the Area Chairs.

{% comment %}
Please examine the [Review form]({{site.baseurl}}/information/reviewform) 

## Review Process
Please read the [review form]({{site.baseurl}}{% post_url 2019-12-04-review-form%}) to understand our emphasis this year.
Authors, Program Committee members, and Area Chairs will all be anonymous. Each paper will receive 3 reviews.
This year, we will have no rebuttals nor conditional acceptances.

{% endcomment %}
