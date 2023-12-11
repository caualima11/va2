
from rest_framework import serializers
from .models import Aluno, Turma, DetalheTurma, Professor, DetalheCurso, Curso, DetalheDisciplina, Disciplina

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

