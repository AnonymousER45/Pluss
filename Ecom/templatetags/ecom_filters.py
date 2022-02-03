import datetime
from django import template

register = template.Library()

@register.filter(name='product_names')
def list_products(products_text):
    prd_names = []
    products = products_text.split(',')
    for prod in products:
        prd_names.append(prod.split(':')[0])
    return prd_names

@register.filter(name='product_images')
def list_image_links(products_text):
    prd_imgs = []
    products = products_text.split(',')
    for prod in products:
        prd_imgs.append(prod.split(':')[-1])
    return prd_imgs

@register.filter(name='img')
def get_img(products_text):
    img = '/media/uploads/'+products_text.split(',')[0].split(':')[-1]
    return img

@register.filter(name='plusdays')
def plus_days(value):
    return str(value + datetime.timedelta(days=7))