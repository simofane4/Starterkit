from django.shortcuts import render
from django.contrib.auth import  logout
from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
def custom_page_not_found_view(request, exception):
    return render(request, "404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "404.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "400.html", {}) 

def sign_in(request):
    form = RegisterForm()

    if request.method == 'POST':
        if 'register' in request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid():
                # On crée l'utilisateur et le client
                user = User(username=form.cleaned_data['username'], email=form.cleaned_data['email'],
                            first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'])
                user.set_password(form.cleaned_data['password'])
                user.save()
                client = Client(user_id=user.id)
                client.save()

                # On connecte le client
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                __move_session_cart_to_database_cart(request, client.id)
                login(request, user)

                if request.GET.get('next', False):
                    return redirect(request.GET['next'])
                else:
                    return redirect(reverse('commerce:root'))
        else:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    client = Client.objects.filter(user_id=user.id).first()
                    __move_session_cart_to_database_cart(request, client.id)
                    login(request, user)
                    if request.GET.get('next', False):
                        return redirect(request.GET['next'])
                    else:
                        return redirect(reverse('commerce:root'))
                else:
                    messages.add_message(request, messages.ERROR,
                                         'Votre compte a été désactivé, veuillez-contacter le service client.')
            else:
                messages.add_message(request, messages.ERROR,
                                     'Les identifiants que vous avez saisis sont incorrects !')

    return render(request, 'signin.html', {
        'get': request.GET,
        'form': form
    })


def sign_out(request):
    logout(request)
    return redirect(reverse('commerce:root'))
