from django.http import HttpResponse


def index(request):
    return HttpResponse('Main page')


def group_posts(request):
    return HttpResponse('Groups posts')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts_detail(request, pk):
    return HttpResponse(f'Post number {pk}')
