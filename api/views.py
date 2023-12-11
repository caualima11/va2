from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..models import Aluno
from .serializers import AlunoSerializer

class AlunoListView(ListAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoDetailView(RetrieveAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
