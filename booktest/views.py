from django.http import HttpResponse


from django.shortcuts import render
from booktest.models import BookInfo,HeroInfo

def index(request):
    book_list = BookInfo.objects.all()
    context={'title':'图书列表','list':book_list}
    return render(request,'booktest/index.html',context)


def detail_page(request,bid,bb):

    detail_hearo = HeroInfo.objects.filter(hbook_id=int(bid))
    context = {'hero_info':detail_hearo}
    return render(request,'booktest/detail_page.html',context)