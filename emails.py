"""
Define generate_email and send_email methods by importing necessary libraries.

"""

#!/usr/bin/env python3
import os, datetime, re
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()
#report = SimpleDocTemplate("")

folderOrigin = "supplier-data/descriptions"
#folderOrigin = r""
courseaIP =  ""
url = "http://" + courseaIP + "/upload/"

feedbackFiles = os.listdir(folderOrigin)
print(feedbackFiles)

def generate_report(attachment, title, paragraph):

    report = SimpleDocTemplate(attachment)

    #Create PDF
    firstrow =  Paragraph(title, styles["Title"])
    report_title = Paragraph("Processed Update on " + datetime.date.today().strftime("%d-%m-%Y"), styles["h1"])
    body = ""


    with open(os.path.join(folderOrigin, paragraph), 'r') as f:
        dict = {}
        dict['name'] = f.readline()
        dict['weight'] = f.readline()

    thisFileDetails = "<br /><br /> name: " + dict['name'] + "<br /> weight: " + dict['weight']

    body = body + str(thisFileDetails)

    body = Paragraph( body, styles["Normal"])

    report.build([firstrow,report_title,body])


"""
#Create PDF
report_title = Paragraph("Processed Update on " + datetime.date.today().strftime("%d-%m-%Y"), styles["h1"])
body = ""

files = os.listdir(folderOrigin)
for file in files:

    with open(os.path.join(folderOrigin, file), 'r') as f:
        dict = {}
        dict['name'] = f.readline()
        dict['weight'] = f.readline()

    thisFileDetails = "<br /><br /> name: " + dict['name'] + "<br /> weight: " + dict['weight']

    body = body + str(thisFileDetails)

body = Paragraph( body, styles["Normal"])

report.build([report_title,body])

"""

