from django.shortcuts import render
from .serializers import ExpensesSerializer
from .models import Expense
from .permissions import IsOwner
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

class ExpenseListAPIView(ListCreateAPIView):
    serializer_class = ExpensesSerializer
    queryset=Expense.objects.all()
    permission_classes=[permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    # NOTE::make sure that every user getjust his data
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    
    
class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ExpensesSerializer
    queryset=Expense.objects.all()
    permission_classes=[permissions.IsAuthenticated,IsOwner]
    lookup_field='id'
    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    