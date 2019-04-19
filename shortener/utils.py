import random
import string
from django.conf import settings
#The below line will give me an error! As in models file  I am importing from this file and in this file
#I am importing from models file...so that two way around does not work
# from shortener.models import KirrURL
SHORTCODE_MIN = getattr(settings,"SHORTCODE_MIN",6)
#define a generator for shortcode
def code_generator(size=6,chars=string.ascii_lowercase + string.digits):
    return 'coc_'+''.join(random.choice(chars) for _ in range(size))
    # new_code = 'coc'
    # for _ in range(size):
    #     new_code+=random.choice(chars)
    # return new_code


#with create_shortcode we are making sure that the shortcode url generated randomly is not repeated otherwise how can
#one same url refer to two different pages
#instance is the instance of the model that we are actually working with


#But I want to use KirrURL. How?
#importing class without importing
#following is the function
def create_shortcode(instance,size=6):
    new_code = code_generator(size=SHORTCODE_MIN)
    #getting the class from instance
    # print(instance)
    # print(instance.__class__)
    # print(instance.__class__.__name__)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(instance,size=SHORTCODE_MIN)
    return new_code
