from django.urls import path
from .views import AlunoListView, AlunoDetailView

app_name = 'api'

urlpatterns = [
    path('alunos/', AlunoListView.as_view(), name='aluno-list'),
    path('alunos/<int:pk>/', AlunoDetailView.as_view(), name='aluno-detail'),
]

