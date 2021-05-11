from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator


Medium_choice =(
    ("English", "English"),
    ("Marathi", "Marathi"),
    ("Hindi", "Hindi"),
    ("Science", "Science"),
    ("Commerce", "Commerce"),
    ("Arts", "Arts"),
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

tax_CHOICE = (
    ('5','5'),
    ('12','12'),
    ('15','15'),
    ('18','18'),
)
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(verbose_name="category")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return 'f/self.slug/'

    
class subCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(verbose_name="subcategory")

    def __str__(self):
        return self.name
        
class Product(models.Model):
    product_id=models.AutoField
    title = models.CharField(max_length=200,null=False)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subCategory = models.ForeignKey(subCategory,on_delete=models.CASCADE)
    slug = models.SlugField()
    desp = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    mrp = models.DecimalField(max_digits=6,decimal_places=2,blank=True,null=True)
    gst = models.CharField(choices=tax_CHOICE,default="18",max_length=5)
    discount_per = models.DecimalField(max_digits=2,decimal_places=0,default=5)
    img = models.ImageField(upload_to="uploads/products/",blank=True,null=True)
    img1 = models.ImageField(upload_to="uploads/products/",blank=True,null=True)
    img2 = models.ImageField(upload_to="uploads/products/",blank=True,null=True)
    img3 = models.ImageField(upload_to="uploads/products/",blank=True,null=True)
    thumbnail = models.ImageField(upload_to="uploads/products/",blank=True,null=True)
    dateadded = models.DateTimeField(auto_now_add=True)
    pub_date = models.CharField(max_length=4)
    edition = models.CharField(max_length=4,default="2018")
    medium = models.CharField(max_length=10,choices=Medium_choice,default="")
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    instock = models.BooleanField(default=True)
    isExchnageable = models.BooleanField(default=True)
    isReturnable = models.BooleanField(default=True)
    

    class meta:
        ordering :('-dateadded',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return 'f/{self.Category.slug}/self.slug/'

    def get_img(self):
        if self.img :
            return 'https://127.0.0.1:8000'+ self.img
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail :
            return 'https://127.0.0.1:8000'+ self.thumbnail.url
        else :
            if  self.img:
                self.thumbnail = self.make_thumbnail(self.img)
                self.save()

                return 'https://127.0.0.1:8000'+ self.thumbnail.url
            else :
                return ''

    def make_thumbnail(self,img,size=(219,208)):
        image = Image.open(img)
        image.convert('RGB')
        image.thumbnail(size)
        thumb_io =BytesIO()
        image.save(self.thumbnail,'JPEG',quality=85)
        thumbnail = File(thumb_io,name=img.name)
        return thumbnail


