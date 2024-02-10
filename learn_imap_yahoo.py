import imaplib
import email
import os           # for environment variables
import base64       # to decode environment variable

# Found imap settings at https://help.yahoo.com/kb/SLN4075.html

imap_server = "imap.mail.yahoo.com"
imap_port = 993

# Yahoo does not allow you to login using your User password.
# You will need to create an Application password.
# See https://help.yahoo.com/kb/SLN15241.html

# Using previously set environment variables YAHOO_USER and YAHOO_PW
# to get the base64 encoded Yahoo email address and app password for login

if os.getenv('YAHOO_USER') and os.getenv('YAHOO_PW'):
    username = base64.b64decode(os.getenv('YAHOO_USER')).decode('UTF-8')
    app_pw = base64.b64decode(os.getenv('YAHOO_PW')).decode('UTF-8')
else:
    print("error: need to set YAHOO_USER and YAHOO_PW environment variables with base64 encoded values")
    exit(1)

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(username, app_pw)

# The imap list command returns a list containing oddly structured folder byte data looking like this:
# b'(\\HasNoChildren) "/" "Inbox"'
# b'(\\HasChildren) "/" "SeattleTech"'
# b'(\\Drafts \\HasNoChildren) "/" "Draft"'

# Build list of folder names and record the length of the largest folder name

print(f"\nMailbox : {username}\n")
 
folders = []
maxlen = 0
for folder in imap.list()[1]:
    folders.append(folder.decode().split(' "/" ')[1])
    if len(folders[-1]) > maxlen:
        maxlen = len(folders[-1])

# Print the folder name and number of messages in that folder

col1 = "FOLDER"
col2 = "MESSAGES"
print(col1.rjust(maxlen), ":", col2)
print("".rjust(maxlen, '-'), ":", "".rjust(len(col2), '-'))

for folder in folders:
    imap.select(folder)
    _, msgnums = imap.search(None, "ALL")
    print(folder.rjust(maxlen), ":", str(len(msgnums[0].split())).rjust(len(col2)))

print("")

imap.close

