from django.db import models


# Create your models here.

class Base(models.Model):
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

    class Meta:
        abstract = True


class Representative(Base):

    def __str__(self):
        return self.first_name + " " + self.last_name


class Estudent(Base):
    representative = models.ForeignKey(
        Representative, on_delete=models.PROTECT)
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


class Receipts(models.Model):
    id = models.CharField(max_length=80, primary_key=True)
    school_period = models.CharField(max_length=10)
    student = models.ForeignKey(
        Estudent, on_delete=models.PROTECT)
    sw_prosecution = models.BooleanField()
    CONDITION = (
        ('N/A', 'N/A'),
        ('RG', 'REGULAR'),
        ('NI', 'NUEVO INGRESO'),
        ('R', 'REPITIENTE'),

    )
    condition = models.CharField(max_length=5, choices=CONDITION, blank=False)

    GRADE = (
        ('N/A', 'N/A'),
        ('1ER AÑO', '1ER AÑO'),
        ('2DO AÑO', '2DO AÑO'),
        ('3ER AÑO', '3ER AÑO'),
        ('4TO AÑO', '4TO AÑO'),
        ('5TO AÑO', '5TO AÑO'),

    )

    grade = models.CharField(max_length=20, choices=GRADE, blank=False)

    SECTION = (
        ('N/A', 'N/A'),
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H'),
        ('I', 'I'),

    )

    section = models.CharField(max_length=5, choices=SECTION, blank=False)
    representative = models.ForeignKey(
        Representative, on_delete=models.PROTECT)
    admission_date = models.DateField()

    MONTH = (
        ('ENERO', 'ENERO'),
        ('FEBRERO', 'FEBRERO'),
        ('MARZO', 'MARZO'),
        ('ABRIL', 'ABRIL'),
        ('MAYO', 'MAYO'),
        ('JUNIO', 'JUNIO'),
        ('JULIO', 'JULIO'),
        ('AGOSTO', 'AGOSTO'),
        ('SEPTIEMBRE', 'SEPTIEMBRE'),
        ('OCTUBRE', 'OCTUBRE'),
        ('NOVIEMBRE', 'NOVIEMBRE'),
        ('DICIEMBRE', 'DICIEMBRE'),

    )

    month_dat = models.CharField(max_length=15, choices=MONTH, blank=False)
    system_date = models.DateField()
    re_registration = models.BooleanField(default=False)
    registration_type = models.CharField(max_length=10)
    status = models.CharField(max_length=2, default="I")
    observation = models.TextField()
    enroller_name = models.CharField(max_length=150)
    record_number = models.CharField(max_length=5)
    institution_name = models.CharField(max_length=100)
    institution_dea = models.CharField(max_length=50)
    institution_cod_adm = models.CharField(max_length=100)
