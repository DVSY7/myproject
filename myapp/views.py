from django.shortcuts import render, HttpResponse
import random

topics = [
    {'id':1, 'title':'routing', 'body': 'routing as..'},
    {'id':2, 'title':'views', 'body': 'views as..'},
    {'id':3, 'title':'model', 'body': 'model as..'}
]
def HTMLTemplate(articleTeg):
     global topics
     ol = ''
     for topic in topics:
            ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
     
     return f'''
    <html>
    <body>
            <h1><a href="/">Django</a></h1>
            <ul>
                {ol}
            </ul>
           {articleTeg}
           <ul>
                <li><a href="/create/">create</a></li>
           </ul>

    </body>
                        
    </html>
    '''

def index(request):
    article = '''
    <h2>wellcome</h2>
     Hello, django
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
         if topic['id'] == int(id):
              article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))

def create(request):
    article = '''
        <form action="/create/">
            <p><input type="text" name="title" placeholder="text"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
    '''
    return HttpResponse(HTMLTemplate(article))



