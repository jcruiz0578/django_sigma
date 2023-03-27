from django.db import models


# Create your models here.


class Representative(models.Model):
    id = models.IntegerField(primary_key=True)
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


class Estudent(models.Model):
    id = models.IntegerField(primary_key=True)
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
    representative = models.ForeignKey(Representative, on_delete=models.PROTECT)
    KINSHIP = (
        ('N/A', 'N/A'),
        ('MADRE', 'MADRE'),
        ('PADRE', 'PADRE'),
        ('MADRASTRA', 'MADRASTRA'),
        ('PADRASTRO', 'PADRASTRO'),
        ('REPRESENTANTE LOPNNA', 'REPRESENTANTE LOPNNA'),

    )

    kinship = models.CharField(max_length=30, choices=KINSHIP, blank=False)

    def __str__(self):
        return self.first_name + " " + self.last_name