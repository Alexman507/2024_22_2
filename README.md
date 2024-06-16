## Задание 1 ()

Создайте новое приложения для работы с пользователем. Определите собственную модель для пользователя, при этом задайте
электронную почту как поле для авторизации.

Также добавьте поля:

- аватар,
- номер телефона,
- страна.

Не забудьте откатить миграции приложения auth до внесения изменений в настройки проекта и переопределения модели для авторизации. Если этого не сделать, вы не сможете взаимодействовать с базой данных. Чтобы откатить миграции приложения auth, можно воспользоваться командой `python manage.py migrate auth zero`

## Задание 2 ()

В сервисе реализуйте функционал аутентификации, а именно:

- Регистрация пользователя по почте и паролю.

**Создайте контроллер для регистрации, который будет взаимодействовать с формой регистрации — пользователю достаточно ввести почту и пароль.**

- Верификация почты пользователя через отправленное письмо.

**В контроллере регистрации переопределите метод `form_valid()` и встройте автоматическую отправку электронного сообщения пользователю на указанный в форме регистрации адрес.**

**Для отправки электронной почты воспользуйтесь встроенной в Django функцией `send_mail()`.**

**Не забудьте настроить почтовый сервер, через который будет происходить отправка электронной почты.**

Документацию можно найти [тут.](https://docs.djangoproject.com/en/5.0/topics/email/)

- Авторизация пользователя.

**Создайте отдельный контроллер для авторизации (LoginView) и зарегистрируйте его в приложении.**

- Восстановление пароля зарегистрированного пользователя на автоматически сгенерированный пароль.

**Создайте новый контроллер для восстановления пароля.**

**В интерфейсе кнопка «Восстановить пароль» должна отображаться на странице входа.**

**Пользователь вводит адрес электронной почты, в контроллере происходит генерация пароля, перезапись пароля для пользователя с соответствующим адресом электронной почты и отправка сообщения с новым паролем на адрес почты.**

**Пароль можно сгенерировать с помощью библиотеки _random_.**

Помните, что пароль в базе данных хранится в захешированном виде. Для установки пароля пользователю можно воспользоваться функцией `make_password()` ([посмотреть в документации про эту функцию](https://docs.djangoproject.com/en/5.0/topics/auth/passwords/#django.contrib.auth.hashers.make_password)).

## Задание 3 ()

Все контроллеры, которые отвечают за работу с продуктами, закройте для анонимных пользователей, при этом создаваемые продукты должны автоматически привязываться к авторизованному пользователю.

Чтобы закрыть контроллеры от анонимных пользователей, добавьте в CBV-контроллеры дополнительное наследование от _LoginRequiredMixin_ (документация [здесь](https://docs.djangoproject.com/en/5.0/topics/auth/default/#the-loginrequiredmixin-mixin)).

Не забудьте добавить поле для продуктов, которое будет указывать на владельца. Оно должно быть ссылкой на модель пользователя.

Для автоматической привязки пользователя к продукту переопределите в контроллере создания продукта метод `form_valid()`.

Текущий авторизованный пользователь доступен через `self.request.user` — запишите его в только что созданный продукт и не забудьте сохранить объект в базу данных.

### Дополнительное задание ()

Добавьте интерфейс редактирования профиля пользователя.










