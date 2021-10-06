import rest_framework
from .models import Curso, Avaliacao


class AvaliacaoSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "email": {"write_only": True}
        }

        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentarios',
            'nota',
            'create',
            'active',
        )


class CursoSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            "email": {"write_only":True}
        }
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'create',
            'active',
        )
