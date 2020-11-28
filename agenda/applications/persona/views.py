from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Person
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import PersonaSerializer
# both next do the same
# class PersonListView(ListView):
#     model = Person
#     template_name = "persona/personas_list.html"
#     context_object_name = 'personas'
# this one
class PersonTempListView(ListView):
    template_name = "persona/personas_list.html"
    context_object_name = 'personas'
    def get_queryset(self):
        return Person.objects.all()

class PersonListApiView(ListAPIView):
    serializer_class = PersonaSerializer

    def get_queryset(self):
        return Person.objects.all()

class PersonListView(TemplateView):
    template_name = "persona/lista.html"

class PersonSearchApiView(ListAPIView):
    serializer_class = PersonaSerializer

    def get_queryset(self):
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )

class PersonCreateView(CreateAPIView):
    serializer_class = PersonaSerializer

class PersonRetrieveApiView(RetrieveAPIView):
    serializer_class = PersonaSerializer
    queryset = Person.objects.all()

class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonaSerializer
    queryset = Person.objects.all()