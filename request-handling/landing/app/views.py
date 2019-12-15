from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    from_page = request.GET.get('from-landing')
    if from_page == 'original':
        counter_click['original'] += 1
    if from_page == 'test':
        counter_click['test'] += 1
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    page_type = request.GET.get('ab-test-arg', 'original')
    if page_type == 'original':
        counter_show['original'] += 1
        return render_to_response('landing.html')
    if page_type == 'test':
        counter_show['test'] += 1
        print(counter_show)
        return render_to_response('landing_alternate.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    test_stats = 0
    original_stats = 0
    if counter_click.get('test') and counter_show.get('test'):
        test_stats = counter_click['test'] / counter_show['test']
    if counter_click.get('original') and counter_show.get('original'):
        original_stats = counter_click['original'] / counter_show['original']
    return render_to_response('stats.html', context={
        'test_conversion': test_stats,
        'original_conversion': original_stats,
    })
