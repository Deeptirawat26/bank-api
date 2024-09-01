from django.shortcuts import render
from rest_framework import generics
from .models import Bank, Branch
from .serializers import BankSerializer, BranchSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

def index(request):
    return render(request, 'index.html') 

class BankListView(APIView):
    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)
    
class BankDetailView(APIView):
    def get(self, request, pk):
        try:
            bank = Bank.objects.get(pk=pk)
            serializer = BankSerializer(bank)
            return Response(serializer.data)
        except Bank.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class BranchListView(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    
class BranchDetailView(generics.RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    lookup_field = 'ifsc'