from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)
def main_view(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Главная страница</title>
    </head>
    <body>
        <h1>Приветствую вас на моем первом Django-сайте</h1>.
        <p>Это главная страница моего первого Django-сайта.</p>
    </body>
    </html>
    """
    logger.info(f'Page "general" is open')
    return HttpResponse(html_content)


def about_view(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Об мне</title>
    </head>
    <body>
        <h1>О себе</h1>
        <p>Это страница, на которой вы можете узнать обо мне.</p>
    </body>
    </html>
    """
    logger.info(f'Page "about" is open')
    return HttpResponse(html_content)
