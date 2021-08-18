from exchangelib import DELEGATE, Account, Credentials, Configuration
from bs4 import BeautifulSoup

#Extract Links from emails

config = Configuration(server='outlook.office365.com',credentials = Credentials(username='your@email.com',password='yourpassword'))
a = Account(primary_smtp_address='your@email.com',autodiscover=False,config=config,access_type=DELEGATE)

look4list = ['Your CSV file for "Support" is ready',
             'Your CSV file for "Web" is ready',
             'Your CSV file for "Video" is ready',
             'Your CSV file for "Management" is ready',
             'Your CSV file for "Social" is ready',
             'Your CSV file for "Creative" is ready']

txt_path = open(r'\\yourpath\email_links.txt','w')

if a.inbox.all().count() > 0:
    for item in a.inbox.all().only('sender','subject','body').order_by('-datetime_received'):
        for x in look4list:
            if x in item.subject:
                soup = BeautifulSoup(item.body,features="lxml")
                for link in soup.findAll('a'):
                    url = link.string
                    if url != 'Youtube':
                        txt_path.writelines(url+'\n')
                item.move(a.inbox/'Youtube')
                item.is_read = True
                item.save()
txt_path.close()
