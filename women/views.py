from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .models import Women, Category
from .serializers import WomenSerializer
from rest_framework import viewsets, mixins
from rest_framework.decorators import action


# class WomenViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     serializer_class = WomenSerializer
#     queryset = Women.objects.all()
#
#     @action(methods=['get'], detail=True)
#     def category(self, request):
#         cats = Category.objects.all()
#         return Response({'cats': [c.name for c in cats]})


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated, )
    # authentication_classes = (TokenAuthentication,)


class WomenAPIDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly, )


# class WomenApiView(APIView):
#     def get(self, request):
#         w = Women.objects.all()
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = WomenSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': "Method PUT not allowed"})
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({'error': "Object does not exists"})
#
#         serializer = WomenSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': "Method PUT not allowed"})
#         serializer = Women.objects.get(pk=pk)
#         serializer.delete()
#         return Response({"post": "delete post" + str(pk)})


# class WomenApiView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
