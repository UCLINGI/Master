Master
======
Goal
=====
The goal of this repository is to group all synthesis, exam corrections,... about courses from ingi.  The goal is also to build theses documents together.

Usage
=====
Add A course
====
Please Add courses in this directory with the fallowing name
SIGLE_name_whithout_special_characters
Ex:
LINGI2263_Computational_Linguistics

Add A File
====
Please always add file in a text or latex type this is the easiest way to get clean versions history, merge, ...
Please sort files.  For instance add passed exam questions/solutions in course/exam/date
Ex:
LINGI2263_Computational_Linguistics/exam/201206

To add a document please use the python script (it will automatically create a base document)
python3 scripts/addDoc.py LINGI2263_Computational_Linguistics/exam/
then set the name to 201206 when asked
This will not simply copy files from empty documents but create symlinc to avoid wasting space and facilitate future update.

Other Informations
====
This repository is configured to avoid adding waste files (.aux, ...) see in .gitignore for more information.
If you want to add a .pdf file you must force it.
