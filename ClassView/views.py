from django.shortcuts import render
from rest_framework import mixins
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import User1
from rest_framework import mixins,generics
from .serializer import UserSerializer
from django.core import paginator
# Create your views here.

class list_1(ListView):
    template_name = 'list_view.html'
    model = User1
    fields = '__all__'

class create_1(CreateView):
    template_name = 'create_view.html'
    model = User1
    fields = '__all__'
    success_url = '/list'

class detail_1(DetailView):
    template_name = 'detail_view.html'
    model = User1
    fields = '__all__'

class update_1(UpdateView):
    template_name = 'update_view.html'
    model = User1
    fields = '__all__'
    success_url = '/list'

class delete_1(DeleteView):
    template_name = 'delete_view.html'
    model = User1

    fields = '__all__'
    success_url = '/list'


class mixins_1(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    template_name = 'mixin_view.html'
    queryset = User1.objects.all()
    serializer_class = UserSerializer

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class CRUD_mixin(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin, generics.GenericAPIView ):

    queryset = User1.objects.all()
    serializer_class = UserSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)

    def put(self,request,pk):
        return self.update(request,pk)

    def delete(self,request,pk):
        return self.destroy(request,pk)

    



