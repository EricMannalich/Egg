from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.base.api.serializers import *


def Paginacion(model,limite = 1,tamanno_pagina = 30):
    model = model.all()[limite * tamanno_pagina - tamanno_pagina:limite * tamanno_pagina]
    return model

def ListPageAPIView(self, request, format=None):
    pagina = request.GET.get(self.lookup_url_kwarg)
    if pagina !=None and pagina.isdigit():
        limite = int(pagina)
    else:
        limite = 1
    model = self.serializer_model.Meta.model.objects.filter(state = True)
    model = Paginacion(model,limite)
    data = self.serializer_model(model, many = True).data
    return Response(data, status = status.HTTP_200_OK)

def get_queryset(self):
    return self.get_serializer().Meta.model.objects.filter(state = True)

def get_nombre_url(self, request, format=None):
    nombre = request.GET.get(self.lookup_url_kwarg)
    if nombre != None:
        model = self.serializer_model.Meta.model.objects.filter(state = True, nombre__icontains = nombre)
        if model:
            data = self.serializer_model(model, many = True).data
            return Response(data, status = status.HTTP_200_OK)
        return Response({'error': 'No encontrado!'}, status = status.HTTP_400_BAD_REQUEST)
    model = self.serializer_model().Meta.model.objects.filter(state = True)
    data = self.serializer_model(model, many = True).data
    return Response(data, status = status.HTTP_200_OK)

class GeneralViewSet(viewsets.ModelViewSet):
    serializer_class = None
    lookup_url_kwarg = 'pagina'

    def get_queryset(self):
        return get_queryset(self)

    def destroy(self,request,pk=None):
        model = self.serializer_class().Meta.model.objects.filter(id = pk).first()
        if model:
            model.state = False
            model.save()
            return Response({'message': 'Eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No encontrado!'}, status = status.HTTP_400_BAD_REQUEST)
        
class GeneralListApiView(generics.ListAPIView):
    serializer_class = None

    def get_queryset(self):
        return get_queryset(self)

class GeneralListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = None

    def get_queryset(self):
        return get_queryset(self)

class GeneraFilterNamelListAPIView(APIView): #Authentication,
    serializer_class = NombreSerializer
    serializer_model = None
    lookup_url_kwarg = 'nombre'

    def get(self, request, format=None):
        return get_nombre_url(self, request, format=None)

    def post(self,request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            nombre = serializer.data.get('nombre')
            model = self.serializer_model().Meta.model.objects.filter(state = True, nombre__icontains = nombre)
            if len(model) > 0:
                data = self.serializer_model(model, many = True).data
                return Response(data, status = status.HTTP_200_OK)
            return Response({'error': 'No encontrado!'}, status = status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class GeneralRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = None

    def get_queryset(self):
        return get_queryset(self)

class GeneralRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = None
    def get_queryset(self):
        return get_queryset(self)

    def delete(self, request, pk = None):
        model = self.get_queryset().filter(id = pk).first()
        if model:
            model.state = False
            model.save()
            return Response({'message': 'Eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No encontrado!'}, status = status.HTTP_400_BAD_REQUEST)

