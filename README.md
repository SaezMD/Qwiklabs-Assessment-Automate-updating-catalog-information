# Qwiklabs-Assessment-Automate-updating-catalog-information

You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs).

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong. What you’ll do Write a script that summarizes and processes sales data into different categories Generate a PDF using Python Automatically send a PDF by email Write a script to check the health status of the system

Files:
changeImage.py: Using the PIL library to resize and reformat (from .TIFF to .JPEG) the images
supplier_image_upload.py: Using the Python requests module to upload these modified images to the web server
run.py: Processing descriptions data from .txt files and upload these data to the web server
reports.py: A Python module for generating PDF report
emails.py: A Python module for generating email message and send email
report_email.py: Extracting data from .txt file and using those data and reports.py module to genarate a PDF report and send it through email by using emails.py module
health_check.py: Monitoring some of system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script will send an email if there are problems
