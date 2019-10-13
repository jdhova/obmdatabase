from django.db import models


# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=25)
    infix = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    photo = models.ImageField(default='')
    company_name = models.CharField(max_length=25)
    job_title = models.CharField(max_length=25)
    company_photo = models.ImageField(default='')
    company_address = models.CharField(max_length=25)

    class Meta:
        db_table = 'Member'

    @classmethod
    def create(cls, r_d):
        member = cls(first_name=r_d['firstName'], infix=r_d['infix'], last_name=r_d['lastName'],
                     photo=r_d['photo'], company_name=r_d['companyName'], job_title=r_d['jobTitle'],
                     company_photo=r_d['companyPhoto'], company_address=r_d['companyAddress'])
        return member


