from split_settings.tools import include
import os


include('base.py')  # спочатку загружаємо базові налаштування

DEBUG = os.getenv('DEBUG') == 'True'

if DEBUG:
    include('local.py')  # якщо в env файлі DEBUG==True - включаємо локальні налаштування
else:
    include('prod.py')  # в іншому випадку - включаємо серверні
