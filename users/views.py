import secrets
import string

from django.conf.global_settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        # print(url)
        send_mail(
            subject='Подтверждение почты',
            message=f'Перейдите по ссылке для подтверждения почты {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        # print(f'Отправлено {EMAIL_HOST_USER} to {user.email}')
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def password_recovery(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        print(f'Получен адрес {email}')

        user = get_object_or_404(User, email=email)

        print(f'Пользователь {user}')

        password = ''

        # Создание 12-символьного буквенно-цифрового пароля по требованиям безопасности:
        alphabet = string.ascii_letters + string.digits
        while True:
            password = ''.join(secrets.choice(alphabet) for i in range(12))
            if (any(c.islower() for c in password)
                    and any(c.isupper() for c in password)
                    and sum(c.isdigit() for c in password) >= 3):
                break

        print(f'Пароль {password}')

        message = f"Сгенерирован пароль: {password}. \
                    Если вы не запрашивали восстановление пароля, просто игнорируйте это сообщение."

        print(f'Пароль {message}')

        send_mail(
            subject='Восстановление пароля',
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[email]
        )
        # пароль шифрует  - как его дальше в шифрованом виде в базу сохранять?
        # psw = make_password(password, salt=None, hasher='default')

        user.set_password(password)
        user.save()
        return redirect(reverse('users:login'))

    return render(request, 'users/password_recovery.html')
