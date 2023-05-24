from djongo import models


gender = (('M','Male'),('F','Female'),('O','Other'))
notification_settings = (('Y','YES'),('N','NO'))

class User(models.Model):
    _id = models.ObjectIdField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1,choices=gender)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)
    passcode = models.CharField(max_length=30)
    notification_settings = models.CharField(max_length=1,choices=notification_settings,default='N')

    


