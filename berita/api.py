from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from functools import wraps

from berita.serializers import KategoriSerializer,ArtikelSerializer,BiodataSerializer
from berita.models import Kategori,Artikel
from pengguna.models import Biodata



def token_required(f):
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        key_token = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"

        token = request.headers.get('token')
        if token is None:
            return Response({'message': 'token not found'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if token != key_token:
            return Response({'message': 'token invalid'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return f(request, *args, **kwargs)
    return decorated_function

@api_view(['GET'])
@token_required
def api_penulis_list(request):
    users =Biodata.objects.all()
    serializer = BiodataSerializer(users, many=True)
    return Response(serializer.data)



@api_view(['GET'])
@token_required
def api_kategori_list(request):

    Kategoris = Kategori.objects.all()
    serializer = KategoriSerializer(Kategoris, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT'])
@token_required
def api_kategori_detail(request,id_kategori):
    try:
        kategoris = Kategori.objects.get(id=id_kategori)
    except:
        return Response({'messsage:':'data not found'},status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = KategoriSerializer(kategoris, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = KategoriSerializer(kategoris, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    else:
        pass

    
@api_view(['POST'])
@token_required
def api_kategori_add(request):
    serializer = KategoriSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@token_required
def api_artikel_list(request):
    key_token = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"

    token = request.headers.get('token')
    if token == None:
        return Response({'message': 'token not found'}, status=status.HTTP_401_UNAUTHORIZED)
    
    if token != key_token:
        return Response({'message': 'token invalid'}, status=status.HTTP_401_UNAUTHORIZED)
    
    artikel = Artikel.objects.all()
    serializer = ArtikelSerializer(artikel, many=True)
    data = {
        'count':artikel.count(),
        'rows':serializer.data
    }
    return Response(data)

@api_view(['GET','PUT','DELETE'])
@token_required
def api_artikel_detail(request,id_artikel):
    try:
        artikel = Artikel.objects.get(id=id_artikel)
    except:    
        return Response({'messsage:':'data not found'},status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtikelSerializer(artikel, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArtikelSerializer(artikel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        artikel.delete()
        return Response({'messsage:':'data deleted'},status=status.HTTP_204_NO_CONTENT)
    
@api_view(['POST'])
@token_required
def api_artikel_add(request):
    serializer = ArtikelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

