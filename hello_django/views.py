import logging

from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    main_text = ""
    logger.info(f'Страница {request.path} посещена пользователем с IP-адресом {request.META["REMOTE_ADDR"]}')
    return HttpResponse(main_text)


def about(request):
    about_text = """
    <h1>Меня зовут Александр</h1>

    <h2>Обо мне</h2>
    <p>Привет! Меня зовут Александр, и я студент GeekBrains. 
    Увлекаюсь программированием, веб-разработкой и всем, что связано с технологиями.</p>

    <h2>Мои увлечения</h2>
    <p>В свободное время я люблю заниматься футболом. Мне интересно все о жизни.</p>

    <h2>Мои достижения</h2>
    <p>На данный момент я обучаюсь на платформе GeekBrains, изучаю django.</p>
    """
    logger.info(f'Страница {request.path} посещена пользователем с IP-адресом {request.META["REMOTE_ADDR"]}')
    return HttpResponse(about_text)
