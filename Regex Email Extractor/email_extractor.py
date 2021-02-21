import re

mystr = '''
from:	Q&A with Senior UI Engineer at Apple USA <notifications@wixsaevents.com>
reply-to:	bpass.22551@gmail.com
to:	shreyad8@gmail.com
date:	Feb 20, 2021, 12:22 PM
subject:	Thank you for registering to our event!
mailed-by:	em670.wixevents.@com.com
signed-by:	wixevents@edu.com
wixevents@edu..com
security:	 Standard encryption (TLS) Learn more
:	Important according to Google magic.
'''

pattern = re.compile(r'\w{2,}(\.)*\w{1,}@[A-Za-z]{2,}.[A-Za-z]{2,3}(\.){0,1}[A-Za-z]{0,3}')
emails_re = pattern.finditer(mystr)

emails = []

for email in emails_re:
    emails.append(f'{email.group()} \n')
# print(emails)
with open('emails_lst.txt', 'a') as fp:
    for mail in emails:
        fp.write(mail)
    print('Successfully Wrote Email-IDs to file!')