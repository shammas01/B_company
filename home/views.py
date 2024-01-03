from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from . serializers import BookCreateSerializer
from . models import Books
from rest_framework.response import Response
from rest_framework import status
# Create your views here.





class Book(APIView):
    def post(self, request):
        serializer = BookCreateSerializer(request.data)
        if serializer:
            data = Books.objects.create(
                name = serializer.data.get('name'),
                autor = serializer.data.get('autor'),
                price = serializer.data.get('price'),
                quatity = serializer.data.get('quatity')

            )
            return Response("Book succssefully added",status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        book = Books.objects.all()
        serializer = BookCreateSerializer(book,many=True)
        return Response(serializer.data)



# class TotalQuantity(APIView):
#     def get(self, request):
#         book = Books.objects.all().annotate(total_price=)
    

class Purchase(APIView):
    def post(self,request,pk):
        book = Books.objects.filter(id=pk)
        book.quatity -= 1
        book.save()

        return Response("you have pusrchase success fully")