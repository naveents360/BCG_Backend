from django.db.models import Model, CharField, IntegerField, CASCADE, DateField, DateTimeField, ForeignKey, SET_NULL, \
    BigIntegerField, PositiveSmallIntegerField,TextField

from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

gender_choices = (
    ('Male','Male'),
    ('Female','Female')
)

ownership_choices = (
    ('JOINT','JOINT'),
    ('INDIVIDUAL','INDIVIDUAL')
)

govt_choices = (
    ('AADHAR','AADHAR'),
    ('VOTER_ID','VOTER_ID'),
    ('PAN','PAN'),
    ('PASSPORT','PASSPORT')
)

category_choices = (
    ('Commerical','Commerical'),
    ('Residential','Residential')
)

status_choices = (
    ('Approved','Approved'),
    ('Pending','Pending'),
    ('Rejected','Rejected'),
    ('Connection Released','Connection Released')
)
class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True,editable=False)
    updated_at = DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        abstract = True

class Address(BaseModel):
    district = CharField(max_length=30)
    state = CharField(max_length=30)
    pincode = PositiveSmallIntegerField()

    class Meta:
        unique_together = ('district','state','pincode')

class Reviewer(BaseModel):
    name = CharField(max_length=150,unique=True)

class Application(BaseModel):
    name = CharField(max_length=150,unique=True)
    gender = CharField(max_length=6,choices=gender_choices,default='Male')
    address = ForeignKey(Address,related_name='address',on_delete=SET_NULL,null=True)
    ownership = CharField(max_length=10,choices=ownership_choices,default='INDIVIDUAL')
    govt_id = CharField(max_length=10,choices=govt_choices,default='AADHAR')
    govt_id_number = BigIntegerField(validators=[MinValueValidator(0)])
    category = CharField(max_length=11,choices=category_choices,default='Residential')
    load = PositiveSmallIntegerField(
        validators=[MaxValueValidator(200),MinValueValidator(0)])
    date = DateField()
    approval_date = DateField(null=True,blank=True)
    status = CharField(max_length=20,choices=status_choices,default='Pending')
    reviewer = ForeignKey(Reviewer,on_delete=SET_NULL,related_name='reviewer',null=True,blank=True)
    comment = TextField()