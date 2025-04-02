from rest_framework import serializers
from api.models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ["id", "nome", "telefone"] # poderia colocar também "__all__" se quisesse todos os campos.
