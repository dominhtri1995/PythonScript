import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
import smsscript

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Minty/minty.jpg"
abs_file_path = os.path.join(script_dir, rel_path)

fromaddr = "secret.kingston@gmail.com"
toaddr = ["tmd2142@columbia.edu"]
tocc=[]

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "conchobang2")

for i in range(0,1,1):
	msgRoot = MIMEMultipart('related')
	msgRoot['Subject'] = 'test message'
	msgRoot['From'] = fromaddr
	msgRoot['To'] = ", ".join(toaddr)
	msgRoot.preamble = 'This is a multi-part message in MIME format.'

	# Encapsulate the plain and HTML versions of the message body in an
	# 'alternative' part, so message agents can decide which they want to display.
	msgAlternative = MIMEMultipart('alternative')
	msgRoot.attach(msgAlternative)

	msgText = MIMEText('This is the alternative plain text message.')
	msgAlternative.attach(msgText)

	# We reference the image in the IMG SRC attribute by the ID we give it below
	msgText = MIMEText('<b>Hi <i>Babe</i> </b> <br><img src="cid:image1"><br>', 'html')
	msgAlternative.attach(msgText)

	fp =open(abs_file_path,'rb')
	msgImage= MIMEImage(fp.read())
	fp.close()
	msgImage.add_header('Content-ID', '<image1>')
	msgRoot.attach(msgImage)


	server.sendmail(fromaddr, toaddr+tocc, msgRoot.as_string())

server.quit()

####Send sms#####

smsscript.sms(8457642961, "yeu cung- anh dang test send sms tu dong")