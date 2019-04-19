from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import KirrURL
from .forms import SubmitURLForm
# Create your views here.
#now what we want to do is redirect the shortcode also to the page where actual site would redirect
# def test_view(request):
#     return HttpResponse("some stuff :)")

# def kirr_redirect_view(request,shortcode=None,*args,**kwargs):
     #function based view
    # print(request.user)
    # print(request.user.is_authenticated())
    # print(args)
    # print(kwargs)
    # try:
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = KirrURL.objects.all().first()

    # obj_url = None
    # qs= KirrURL.objects.filter(shortcode=shortcode)
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url
    # obj=get_object_or_404(KirrURL, shortcode = shortcode)
    # return HttpResponseRedirect(obj.url)
    # return HttpResponse("hello {sc}".format(sc=obj.url))

class URLRedirectView(View):         #class based view
    def get(self,reuqest,shortcode=None,*args,**kwargs):
        obj=get_object_or_404(KirrURL, shortcode = shortcode)
        return HttpResponseRedirect(obj.url)
    #     # return HttpResponse("hello again {sc}".format(sc=obj.url))
    #
    #     # I did not understand why post is written for class based views and not
    #     #function based views
    # def post(self,request,*args,**kwargs):
    #     return HttpResponse()

class HomeView(View):
    def get(self,request,*args,**kwargs):
        the_form = SubmitURLForm()
        context = {
        "title" : "Shortener_COC",
        "form" : the_form,

        }
        return render(request,"shortener/home.html", context)

    def post(self,request,*args,**kwargs):
        form = SubmitURLForm(request.POST)
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            context = {
            "object" : obj,
            "created": created
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"
            return render(request,template,context)
        return render(request,"shortener/invalid_url.html")
        # some_dict = {}
        # some_dict.get('url')
        # print(request.POST)
        # print(request.POST.get("url"))
        # print(request.POST["url"])
        # print(request.POST.get("url"))
