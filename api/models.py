from django.db import models
from authentication.models import (Driver, Passenger,User)
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from .mixins.base_model_mixin import BaseModel
import uuid

class Region(BaseModel):
    """

    """
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    name =  models.CharField(max_length=50,null=False,default='None')

    abbreviation = models.CharField(max_length=50,null=False,default='None')
    

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Region, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str
    

class Purpose(BaseModel):
    """

    """
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    name =  models.CharField(max_length=50,null=False,default='None')

    abbreviation = models.CharField(max_length=50,null=False,default='None')
    

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Purpose, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str
    

class Basis(BaseModel):
    """

    """
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    name =  models.CharField(max_length=50,null=False,default='None')

    abbreviation = models.CharField(max_length=50,null=False,default='None')
    

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Basis, self).save()

    def __str__(self):
        _str = '%s' % self.name
        return _str

class Record(BaseModel):
    """

    """
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    region =  models.OneToOneField(
        Region, related_name="Region", on_delete=models.CASCADE)
    
    purpose =  models.OneToOneField(
        Purpose, related_name="Purpose", on_delete=models.CASCADE)
    
    basis =  models.OneToOneField(
        Basis, related_name="Basis", on_delete=models.CASCADE)
    

    county = models.CharField(max_length=50,null=False,default='None')

    place = models.CharField(max_length=50,null=False,default='None')

    reference = models.CharField(max_length=50,null=False,default='None')

    officer = models.CharField(max_length=50,null=False,default='None')

    block = models.CharField(max_length=50,null=False,default='None')
    

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Record, self).save()

    def __str__(self):
        _str = '%s' % self.id
        return _str







class PhoneNumber(BaseModel):

    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    number = PhoneNumberField(max_length=16, unique=True, blank=False)
    

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(PhoneNumber, self).save()

    def __str__(self):
        _str = '%s' % self.number
        return _str


class UserPhoneNumber (BaseModel):


    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    user = models.ForeignKey(
        User, related_name='phone_numbers', null=False, on_delete=models.CASCADE)
    phone_number = models.ForeignKey(
        PhoneNumber, null=False, on_delete=models.CASCADE)
    primary = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(UserPhoneNumber, self).save()

    def __str__(self):
        _str = '%s' % self.phone_number.number
        return _str

