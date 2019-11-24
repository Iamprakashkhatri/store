from django.shortcuts import render,reverse,redirect
from django.urls import reverse_lazy
from .forms import LoginForm,RegisterForm,StoreForm
from django.views.generic.edit import FormView,View
from .models import Store
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import User
from django.contrib.auth.models import Group


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from guardian.shortcuts import assign_perm
from guardian.shortcuts import get_objects_for_user
from guardian.shortcuts import get_perms


class DashboardView(FormView):


    def get(self, request):
        stores=Store.objects.all()
        return render(request, 'stor/dashboard.html', {'stores':stores})
class RegisterView(FormView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        content = {}
        content['form'] = RegisterForm
        return render(request, 'stor/register.html', content)

    def post(self, request):
        content = {}
        form = RegisterForm(request.POST, request.FILES or None)
        if form.is_valid():
            save_it = form.save(commit=False)
            save_it.password = make_password(form.cleaned_data['password'])
            save_it.save()
            print(save_it)
            login(request, save_it)
            return redirect(reverse('stor:login-view'))
        content['form'] = form
        template = 'stor/register.html'
        return render(request, template, content)



class LoginView(FormView):
    content = {}
    content['form'] = LoginForm
    # member=Member.objects.all()
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)
    def get(self, request):
        return render(request, 'stor/login.html', self.content)

    def post(self, request):
        content = {}
        email = request.POST['email']
        password = request.POST['password']
        try:
            users = User.objects.filter(email=email)
            user = authenticate(request, username=users.first().username, password=password)
            login(request, user)
            return redirect(reverse('stor:dashboard-view'))
        except Exception as e:
            content = {}
            content['form'] = LoginForm
            content['error'] = 'Unable to login with provided credentials' + e
            return render('stor/login.html', content)




class StoreList(LoginRequiredMixin, ListView):
    model = Store
    # context_object_name = 'items'
    template_name = 'items/index.html'


class StoreDetail(UserPassesTestMixin, DetailView):
    model = Store
    # pk_url_kwarg = 'item_id'
    template_name = 'items/detail.html'

    def test_func(self):
        return self.request.user.is_authenticated


class StoreCreation(PermissionRequiredMixin,SuccessMessageMixin, CreateView):
    model = Store
    form_class = StoreForm
    template_name = 'items/create.html'
    success_url = reverse_lazy('stor:list')
    success_message = "Item %(name)s created successfully"
    permission_required = ('stor.give_refund',)
    # def get(self,request):
    #
    #     form=StoreForm
    #     hari = User.objects.get(username='hari')
    #     print(hari)
    #     store = Store.objects.get(id=1)
    #     print(store)
    #     # print(joe.has_perm('post_add', post))
    #     permission_required = ('stor.add',)
    #     assign_perm('give_refund', hari,store)
    #     form = get_objects_for_user(request.user, 'stor.give_refund')
    #
    #
    #     if 'give_refund' in get_perms(hari, store):
    #         return render(request, 'items/create.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class StoreUpdate(SuccessMessageMixin, UpdateView):
    model = Store
    template_name = 'items/update.html'
    # pk_url_kwarg = 'item_id'
    form_class = StoreForm
    success_url = reverse_lazy('stor:list')
    success_message = "Item %(name)s updated successfully"


@method_decorator(user_passes_test(lambda u: Group.objects.get(name='create store')),name='dispatch')
class StoreDelete(PermissionRequiredMixin,DeleteView):
    template_name = 'items/delete.html'
    model = Store
    # pk_url_kwarg = 'item_id'
    success_url = reverse_lazy('stor:list')
    permission_required = ('stor.give_refund',)




