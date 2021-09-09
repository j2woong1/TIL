1. Read

   ![image-20210909221202306](0909_workshop.assets/image-20210909221202306.png)

   ```html
   <!-- index.html -->
   
   {% extends 'base.html' %}
   {% load static %}
   {% block content %}
     <img src="{% static 'images/ssafy1.png' %}" alt="ssafy image">
     <h1 class="text-danger">Articles</h1>
     <a href="{% url 'articles:create' %}">[CREATE]</a>
     <hr>
     {% for article in articles %}
       <p>글 번호 : {{ article.pk }}</p>
       <p>글 제목 : {{ article.title }}</p>
       <p>글 내용 : {{ article.content }}</p>
       <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
       <hr>
     {% endfor %}
   {% endblock content %}
   ```

   ```python
   # views.py
   
   def index(request):
       articles = Article.objects.order_by('-pk')
       context = {
           'articles': articles,
       }
       return render(request, 'articles/index.html', context)
   ```

2. Create

   ![image-20210909221404299](0909_workshop.assets/image-20210909221404299.png)

   ```python
   # views.py
   
   @require_http_methods(['GET', 'POST'])
   def create(request):
       if request.method == 'POST':
           form = ArticleForm(request.POST, request.FILES)
           imageform = ArticleImageForm(request.POST, request.FILES)
           if form.is_valid():
               article = form.save()
               imageform.save()        
               return redirect('articles:detail', article.pk)
       else:
           form = ArticleForm()
           imageform = ArticleImageForm()
       context = {
           'form': form,
           'imageform': imageform,
       }
       return render(request, 'articles/create.html', context)
   ```

   ```html
   <!-- create.html -->
   
   {% extends 'base.html' %}
   {% load bootstrap5 %}
   {% block content %}
     <h1>CREATE</h1>
     <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
       {% csrf_token %}
       {% bootstrap_form form %}
       {{ imageform.as_p }}
       <input type="submit" value="제출" accept="image/*">
     </form>
     <a href="{% url 'articles:index' %}">[back]</a>
   {% endblock content %}
   ```

3. Detail

   ![image-20210909221518151](0909_workshop.assets/image-20210909221518151.png)

   ```python
   # views.py 
   
   def detail(request, pk):
       article = get_object_or_404(Article, pk=pk)
       articleimage = get_object_or_404(ArticleImage, pk=pk)
       context = {
           'article': article,
           'articleimage': articleimage,
       }
       return render(request, 'articles/detail.html', context)
   ```

   ```html
   <!-- detail.html -->
   
   {% extends 'base.html' %}
   
   {% block content %}
     <br>
     <p>제목 : {{ article.title }}</p>
     <p>내용 : {{ article.content }}</p>
     {% if articleimage.image %}
       <img src="{{ articleimage.image.url }}" alt="{{ articleimage.image }}">
     {% endif %}
     <p>작성시각 : {{ article.created_at }}</p>
     <p>수정시각 : {{ article.updated_at }}</p>
     <hr>
     <a href="{% url 'articles:update' article.pk %}">
       <button class="btn btn-primary">UPDATE</button>
     </a>
     <form action="{% url 'articles:delete' article.pk %}" method="POST">
       {% csrf_token %}
       <button class="btn btn-danger">DELETE</button>
     </form>
     <a href="{% url 'articles:index' %}">[back]</a>
   {% endblock content %}
   ```

4. Update

   ![image-20210909222632873](0909_workshop.assets/image-20210909222632873.png)

   ```python
   # views.py
   @require_http_methods(['GET', 'POST'])
   def update(request, pk):
       article = get_object_or_404(Article, pk=pk)
       articleimage = get_object_or_404(ArticleImage, pk=pk)
       if request.method == 'POST':
           form = ArticleForm(request.POST, request.FILES, instance=article)
           imageform = ArticleForm(request.POST, request.FILES, instance=articleimage)
           if form.is_valid():
               form.save()
               imageform.save()
               return redirect('articles:detail', article.pk)
       else:
           form = ArticleForm(instance=article)
           imageform = ArticleImageForm(instance=articleimage)
       context = {
           'article': article,
           'form': form,
           'imageform': imageform,
       }
       return render(request, 'articles/update.html', context)
   ```

   ```html
   <!-- update.html -->
   
   {% extends 'base.html' %}
   {% load bootstrap5 %}
   {% block content %}
     <h1>UPDATE</h1>
     <form action="{% url 'articles:update' article.pk %}" method="POST" enctype="multipart/form-data">
       {% csrf_token %}
       {% bootstrap_form form %}
       {{ imageform.as_p }}
       {% buttons submit='OK' reset="Cancel" %}{% endbuttons %}
     </form>
     <hr>
     <a href="{% url 'articles:index' %}">[back]</a>
   {% endblock content %}
   ```

5. Delete

   ```python
   # views.py
   
   @require_POST
   def delete(request, pk):
       article = get_object_or_404(Article, pk=pk)
       articleimage = get_object_or_404(ArticleImage, pk=pk)
       article.delete()
       articleimage.delete()
       return redirect('articles:index')
   ```

   

