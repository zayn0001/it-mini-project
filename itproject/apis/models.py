from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver

class User(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50, unique=True, primary_key=True)
    email = models.EmailField()
    dob = models.DateField()
    password = models.CharField(max_length = 50)
    phone = models.PositiveBigIntegerField(validators=[MinValueValidator(1000000000),MaxValueValidator(9999999999)])

    def __str__(self):
        return self.first_name + " " + self.last_name

class Admin(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)    
    username = models.CharField(max_length = 50, unique=True, primary_key=True)
    dob = models.DateField()
    password = models.CharField(max_length = 50)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Package(models.Model):
    name = models.CharField(max_length = 50, primary_key=True)
    destination = models.CharField(max_length=100)
    no_of_people = models.PositiveIntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    no_of_days = models.PositiveIntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    cost_per_head = models.PositiveIntegerField()

    description = models.TextField(max_length=400)
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class ActivePackage(models.Model):
    package = models.OneToOneField(Package, on_delete=models.CASCADE, primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()   
    last_date_of_booking = models.DateField()
    vacancies = models.PositiveIntegerField(null=True, blank=True)


    def __str__(self):
        return self.package.name
    
@receiver(models.signals.post_save, sender=ActivePackage)
def execute_before_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.vacancies = instance.package.no_of_people
        instance.save()

class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activepackage = models.ForeignKey(ActivePackage, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.activepackage.vacancies -= 1 
        self.activepackage.save()
        super(Participant, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.activepackage.vacancies += 1 
        self.activepackage.save()
        super(Participant, self).delete()

    def __str__(self):
        return self.activepackage.package.name + " " + self.user.last_name

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.ForeignKey(ActivePackage, on_delete=models.CASCADE)

    def __str__(self):
        return self.active.package.name + " " + self.user.last_name
    
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    description = models.TextField(max_length=400)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.description[:20] + "..."
    
class TripHistory(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.package.name

class ParticipantHistory(models.Model):
    trip = models.ForeignKey(TripHistory, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.trip.package.name + " " + self.user.last_name 

try:
    u = User(first_name="mishal", last_name="faisal", username="mishal", email="mishal0404@gmail.com",dob="2003-04-04", password="mishal",phone="8129953715")
    u.save()
    a = Admin(first_name="jasar", last_name="faisal", username="jasar", email="mishal0404@gmail.com",dob="2003-04-04", password="mishal")
    a.save()
except:
    pass





    

    


