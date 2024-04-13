from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .Serializers import ExpenseSerializer
from .models import Expense

class ExpenseViewSet(ModelViewSet):
	queryset = Expense.objects.all()
	serializer_class = ExpenseSerializer