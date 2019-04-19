from django.db import models
from django.conf import settings
from .utils import code_generator,create_shortcode
from .validators import validate_url, validate_dot_com
from django.core.urlresolvers import reverse
# from django_hosts.resolvers import reverse
# Create your models here.

SHORTCODE_MAX = getattr(settings,"SHORTCODE_MAX",15)


#model manager (objects)
#the function all and get_or_create can be overriden here
class KirrURLManager(models.Manager):
    #to give all the active links


    def all(self,*args,**kwargs):
        qs_main = super(KirrURLManager, self).all(*args,**kwargs)
        qs = qs_main.filter(active = True)
        return qs

        #to change all the shortcodes all at once
    def refresh_shortcodes(self,items=None):
        print(items)
        #here I can't use all because my actual all
        #definition is changed
        qs = KirrURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items,int):
            qs = qs.order_by('-id')[:items]

        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes+=1
        return "New codes made: {}".format(new_codes)


class KirrURL(models.Model):
    url = models.CharField(max_length = 220,validators=[validate_url,validate_dot_com])
    #blank=True means I can keep it blank in the admin section
    #but I still require shortcode in my database
    #however there is a possibility that when blank is true and null is False
    #there might be an error thrown from django or database
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique = True,blank=True)
    updated = models.DateTimeField(auto_now=True) #everytime the model is saved
    timestamp = models.DateTimeField(auto_now_add=True) #when model was created
    active = models.BooleanField(default=True)

    #empty_datetime = models.DateTimeField(auto_now=False, auto_now_add=False) -- empty date which we can set
    #shortcode = models.CharField(max_length=15, null=True ) -- Empty in database is ok
    #shortcode = models.CharField(max_length=15, default = 'coc')
    objects = KirrURLManager()
    some_random = KirrURLManager()

    #overriding the default save method
    def save(self,*args,**kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(KirrURL,self).save(*args,**kwargs)  #calling super save method

    # def my_save(self):
    #     self.save()

    # class Meta:
    #     ordering = '-id'   but here had to run migrations
        # - implies reverse
        #can also do ordering by url alphabetically

    def __str__(self):
        return str(self.url)


    def get_short_url(self):
        # url_path = reverse("scode",kwargs={'shortcode':self.shortcode},host='www',scheme='http')
        url_path = reverse("scode",kwargs={'shortcode':self.shortcode})
        return "http://www.cocvjti.com:8000" + url_path
