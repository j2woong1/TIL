> 제시된 Reservation Class 를 참고하여 각 문항에 답하시오
>
> ```
> # models.py
> class Reservation(model.Model):
>     name = models.CharField(max_length=10)
>     date = models.DateField()
> ```
>
> 

1. Model Form 을 정의하기 위해 빈칸에 들어갈 코드 (a),(b) 를 작성하시오

   ```python
   from django import forms
   from .models import Reservation
   
   class ResercationForm(__(a)__):
       
       class __(b)__:
           model = Reservation
           filed = '__all__'
   ```

   - (a) : `forms.ModelForm`
   - (b) : `Meta`

2. 글 작성 기능을 구현하기 위해 다음과 같이 코드를 작성하였다. 서버를 실행시킨 후 기능을 테스트 해보니 특정 상황에서 문제가 발생하였다. 이유와 해결방법을 작성하시오

   ```python
   def create(request):
       if request.method == 'POST':
           form = ReservationForm(request.POST)
           if form.is_valid():
               reservation = form.save()
               return redirect('reservations:detail', reservation.pk)
       else:  
       	form = ArticleForm()
           context = {
              'form':form,
           }
           return render(request, 'articles/create.html', context)
   ```

   - POST 요청 시 context 미작동
   - context ~ return 구문 if else와 동일한 레벨에서 작성

3. 글 수정 기능을 구현하기 위해 빈칸에 들어갈 코드 (a), (b) 를 작성하시오.

   ```python
   def update(request, pk):
       reservation = Reservation.objects.get(pk=pk)
       if request.method == 'POST':
           __(a)__
           if form.is vaild():
               reservaion = form.save()
               return redirect('reservations:detail', reservation.pk)
       else:
           __(b)__
       context = {
           'reservaion': reservation,
           'form': form
       }
       return render(request, 'reservaions/update.html', context)
   ```

   - (a) : `form = ReservationForm(request.POST, instance=reservation)`
   - (b) : `form = ReservationForm(instance=reservation)`

4. form 출력을 구현하기 위해 빈칸 (a) 에 작성 할 수 있는 코드를 모두 작성하시오.

   ```html
   <h2> edit </h2>
   <form action="{% url ' reservations:update' reservation.pk %}" method="POST">
   {% csrf_token %}
   {{ form.__(a)__}}
   <input type="submit" value="submit">
   </form>
   ```

   - `as_p`, `as_ul`, `as_table`

