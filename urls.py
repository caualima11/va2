from django.urls import path, include
from .views import AlunoListView, AlunoDetailView

app_name = 'va2projeto'

urlpatterns = [
    path('', AlunoListView.as_view(), name='index'),
    path('alunos/', AlunoListView.as_view(), name='aluno-list'),
    path('alunos/<int:pk>/', AlunoDetailView.as_view(), name='aluno-detail'),
    path('api/', include('va2projeto.api.urls')),  # Inclua as URLs da API aqui
]
