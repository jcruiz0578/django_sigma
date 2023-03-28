from django.db import models

# Create your models here.


class Personal(models.Model):
    identification_card = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=False)
    fn = models.DateField(blank=False)
    SEXO = (
        ('N/A', 'N/A'),
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        )

    sex = models.CharField(max_length=3, choices=SEXO, blank=False)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name


class Staff(models.Model):
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    TYPE_STAFF = (
        ('N/A', 'N/A'),
        ('D', 'Docente'),
        ('A', 'Administrativo'),
        ('O', 'Obrero'),
        ('C', 'Cocinera'),

        )

    type_staff = models.CharField(
        max_length=3, choices=TYPE_STAFF, blank=False)
    cod_dependency = models.CharField(max_length=20, blank=False)
    code_Dea = models.CharField(max_length=20, blank=False)
    instDependency = models.CharField(max_length=80)
    hours = models.IntegerField(blank=False)
    admission_date = models.DateField(blank=False)
    bachelor = models.BooleanField(default=True)
    pre_grade = models.CharField(max_length=100)
    post_graduate = models.CharField(max_length=100)
    other_studies = models.CharField(max_length=100)
