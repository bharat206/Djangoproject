import os

#os.environ.setdefault('DJANGO_SETTING_MODULE','modelproject3.settings')
os.environ["DJANGO_SETTINGS_MODULE"] = "bharatjobs.settings"
import django 
django.setup()

from jobapp.models import*
from faker import*
from random import*

fake = Faker()
def phoneumber():
    digit_1 = randint(6,9)
    num = ''+str(digit_1)
    for i in range(9):
        num += str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements= ('Project Manager', 'Associate Engineer', 'Team Lead','Scrum Master','Software Engineer'))
        feligibilty = fake.random_element(elements= ('B.Tech','M.Tech','BCA'))
        faddress = fake.address()
        femail = fake.email()
        fphoneno = phoneumber()

        HydJobs.objects.get_or_create(date = fdate, company = fcompany, title = ftitle, eligibilty= feligibilty, address = faddress, email= femail, phonenumber = fphoneno)
        PuneJobs.objects.get_or_create(date = fdate, company = fcompany, title = ftitle, eligibilty= feligibilty, address = faddress, email= femail, phonenumber = fphoneno)
        BangJobs.objects.get_or_create(date = fdate, company = fcompany, title = ftitle, eligibilty= feligibilty, address = faddress, email= femail, phonenumber = fphoneno)
n = int(input('Enter number of record'))        
populate(n)
print(f'{n} Records inserted sucessfully....')