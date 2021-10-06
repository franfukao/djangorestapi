from rest_framework.views import APIView
from rest_framework.response import Response

import curso
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursoAPIView(APIView):
    def get(self, request):
        curso = Curso.objects.all()
        serializer = CursoSerializer(curso, many=True)
        print(serializer.data)
        # gerando JSON
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # return Response({"msg": "Inserido com sucesso"})
        return Response({"id": serializer.data['id']})
        # return Response(serializer.data, status=status.HTTP_201_CREATED)


class AvaliacaoAPIView(APIView):

    def get(self, request):
        av = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(av, many=True)
        # gerando JSON
        return Response(serializer.data)
