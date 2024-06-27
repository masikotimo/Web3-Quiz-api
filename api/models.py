from django.db import models
from authentication.models import (Driver, Passenger,User)
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from .mixins.base_model_mixin import BaseModel
import uuid




class SubscriptionProduct(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    name = models.CharField(max_length=255, unique=True)
    price = models.FloatField()
    billing_period = models.IntegerField()
    trial_period = models.IntegerField(default=0)
    trial_game_count = models.IntegerField(blank=True, null=True, default=0)
    game_count_limit = models.IntegerField(blank=True, null=True, default=0)


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(SubscriptionProduct, self).save()

    def __str__(self):
        return self.name
    


class SubscriptionPayment(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    transaction_id = models.CharField(max_length=255, unique=True)
    provider_transaction_id = models.CharField(max_length=255)
    payment_date = models.DateField()
    payment_amount = models.FloatField()
    payment_method = models.TextField()
    product_id = models.IntegerField()
    payment_status = models.TextField()
    provider_customer_id = models.TextField(blank=True, null=True)
    is_live = models.IntegerField(blank=True, null=True)
    payment_provider = models.TextField()


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(SubscriptionPayment, self).save()

    def __str__(self):
        return self.transaction_id
    


class Category(BaseModel):
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    name = models.CharField(max_length=100, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Category, self).save()

    def __str__(self):
        return self.name


class Question(BaseModel):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'


    CHILLED = 'chilled'
    STUPID = 'stupid'
    NOT_KAWA = 'not_kawa'

    

    DIFFICULTY_CHOICES = [
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    ]

    CLASSIFICATION_CHOICES = [
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    ]
    id = models.UUIDField(primary_key=True, max_length=50,
                          default=uuid.UUID('a365c526-2028-4985-848c-312a82699c7b'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.TextField()  # assuming tags will be stored as comma-separated values
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    question = models.TextField()
    answers = models.TextField() # storing answers as JSON array
    question_type = models.CharField(max_length=20, default='text_choice')
    classification = models.CharField(max_length=10, choices=CLASSIFICATION_CHOICES, default=CHILLED)



    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            self.id = uuid.uuid4()
        super(Question, self).save()

    def __str__(self):
        return f"Category: {self.category}, Difficulty: {self.difficulty}, Question: {self.question[:50]}"
    
    




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

