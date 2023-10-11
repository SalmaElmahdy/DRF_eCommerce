from rest_framework import serializers
from .models import Expense

class ExpensesSerializer(serializers.ModelSerializer):
    # if we define field here in swagger it will be in default try object within the same data type
    # for example in fields we define amount so it wil be in default example like "string"
    # if we want it to be decimal value we should define amount here
    # amount=serializers.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
        model= Expense
        fields=['id','date','description','amount','category']