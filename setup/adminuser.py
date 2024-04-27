from django.contrib.auth.models import User 


User.objects.create_superuser('superuser', 'superuser@gmail.com', 'superuser')

