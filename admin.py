
from django.contrib import admin
from .models import Aluno, Turma, DetalheTurma, Professor, DetalheCurso, Curso, DetalheDisciplina, Disciplina

admin.site.register(Aluno)
admin.site.register(Turma)
admin.site.register(DetalheTurma)
admin.site.register(Professor)
admin.site.register(DetalheCurso)
admin.site.register(Curso)
admin.site.register(DetalheDisciplina)
admin.site.register(Disciplina)
