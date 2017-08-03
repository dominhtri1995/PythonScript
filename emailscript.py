import smtplib
from email import encoders, parser
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from optparse import OptionParser

# abs_file_path = "/Users/TriDo/Downloads/heart.jpg"
youremail = "secret.kingston@gmail.com"
password = "conchobang2"

parser = OptionParser()
parser.add_option("-t", "--to", action="append", type="string", dest="toaddr")
parser.add_option("-c", "--cc", action="append", type="string", dest="tocc")
parser.add_option("-s", "--subject", action="store", type="string", dest="subject", default= "Sent from my Mac")
parser.add_option("-f", "--file", action="append", type="string", dest="file")
parser.add_option("-m","--message",action= "store", type="string", dest="message",default ="")
options, args = parser.parse_args()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(youremail, password)

msgRoot = MIMEMultipart()
msgRoot['Subject'] = options.subject
msgRoot['From'] = youremail
msgRoot['To'] = ", ".join(options.toaddr)
if options.tocc:
    msgRoot['Cc'] = ", ".join(options.tocc)
    options.toaddr += options.tocc

body = options.message
msgRoot.attach(MIMEText(body, 'plain'))

# embed image into email
# fp = open(abs_file_path, 'rb')
# msgImage = MIMEImage(fp.read())
# fp.close()
# msgImage.add_header('Content-ID', '<image1>')
# msgRoot.attach(msgImage)

# Attachment
if options.file:
    for file in options.file:
        arr = file.split("/")
        filename = arr[len(arr) - 1]
        attachment = open(file, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msgRoot.attach(part)

server.sendmail(youremail, options.toaddr, msgRoot.as_string())
server.quit()
