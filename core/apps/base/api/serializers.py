from rest_framework import serializers


class NombreSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=30, default="")

class BuscarSerializer(serializers.Serializer):
    entrada = serializers.CharField(max_length=50, default="", required=False,allow_null=True)
    pagina = serializers.IntegerField(default=1)