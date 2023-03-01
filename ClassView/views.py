from django.shortcuts import render,redirect
from rest_framework import mixins
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import User1
from rest_framework import mixins,generics
from .serializer import UserSerializer
from django.core import paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
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

    
def register_1(request):
    if request.method =="POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        re_password = request.POST["re_password"]
 
        if password ==re_password:
            if User.objects.filter(username = username).exists():
                messages.error(request,"Username already exist")
                return render (request, 'register.html') 

            elif User.objects.filter(email = email).exists():
                messages.error(request,"Email already Exist!")
                return render (request, 'register.html') 

            else:            
                user = User.objects.create_user(first_name = first_name,last_name = last_name,
                        username=username,email = email,password = password)
                user.save()
                return redirect('login')
        else:
            messages.error(request,"Password Does not march!")
            return render (request, 'register.html') 


    else:
        return render (request, 'register.html')  

def login_1(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"] 

        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('logout_1')
            # return render(request,'logout.html')
        else:
            messages.error(request,"invalid Credencials")
            return redirect('login')
    else:
        return render(request,'login.html')

def logout_1(request):
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
    logout(request)
    return render(request,'logout.html')
  
    # return render(request,'logout.html')




