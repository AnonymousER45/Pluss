from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image
from django.core.validators import MaxValueValidator, MinValueValidator
from Accounts.models import Customer
from datetime import date
import datetime as DT

Order_Status_Choice = (
        ("1","Order Created"),
        ("2","Order Packed"),
        ("3","Out for Delivery"),
        ("4","Order delivery Pending"),
        ("5","Delivered"),
        ("6","Order Cancelled"),
        ("7","Order Completed"),
        ("8","Exchange Requested"),
        ("9","Return Requested"),
        ("10","Exchange Approved"),
        ("11","Return Approved"),
        ("12","Refund Intiated"),
        ("13","ReFunded Succesfully"),
        ("14","Exchanged Successfully"),
    )

Book_type = (
    ("1" , "Textbook"),
    ("2" , "Reference book"),
    ("3" , "Study material"),
    ("4" , "Novel"),
    ("5" , "Story books/Biography"),
    ("6" , "Others"),
)

Book_relatedto = (
    ("1" , "State Board"),
    ("2" , "CBSE Board"),
    ("3" , "Study ICSE Board"),
    ("4" , "Entrance exams"),
    ("5" , "For book readers"),
    ("6" , "Others"),
)

Medium_choice =(
    ("NEET", "NEET"),
    ("JEE", "JEE"),
    ("CET", "CET"),
    ("English", "English"),
    ("Marathi", "Marathi"),
    ("Hindi", "Hindi"),
    ("Science", "Science"),
    ("Commerce", "Commerce"),
    ("Arts", "Arts"),
    ("Notebooks","Notebooks"),
    ("Stationary","Stationary"),
    ("Story Books","Story Books"),
    ("Biography","Biography"),
    ("First Year","First Year"),
    ("Second Year","Second Year"),
    ("Third Year","Third Year")

)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

tax_CHOICE = (
    ('0','0'),
    ('5','5'),
    ('7','7'),
    ('12','12'),
    ('15','15'),
    ('18','18'),
    ('22','22'),
    ('24','24'),
    ('28','28'),
)

Return_Choices =(
    ("1", "Poor product quality"),
    ("2", "Product received is damaged"),
    ("3", "Product & Shipping box both are damaged"),
    ("4", "Product received is different"),
    ("5", "Other"),
)

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(verbose_name="category")
    cat_ban = models.ImageField(upload_to="uploads/Category/",blank=True,null=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return 'f/self.slug/'

class Banner(models.Model):
    homeban = models.ImageField(upload_to="uploads/products/",blank=True,null=True)
    homeban1 = models.ImageField(upload_to="uploads/products/",blank=True,null=True)
    homeban2 = models.ImageField(upload_to="uploads/products/",blank=True,null=True)
    homeban3 = models.ImageField(upload_to="uploads/products/",blank=True,null=True)


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
    dateadded = models.DateTimeField(auto_now_add=True)
    pub_date = models.CharField(max_length=4)
    edition = models.CharField(max_length=4,default="2018")
    medium = models.CharField(max_length=20,choices=Medium_choice,default="")
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    instock = models.BooleanField(default=True)
    isExchnageable = models.BooleanField(default=True)
    isReturnable = models.BooleanField(default=True)
    isBestSeller = models.BooleanField(default=False)
    isDealoftheday = models.BooleanField(default=False,blank=True,null=True)
    isBindable = models.BooleanField(default=False)
    isBinding = models.BooleanField(default=False)
    bind_price = models.DecimalField(max_digits=6,decimal_places=2,default=30.00)


    class meta:
        ordering :('-dateadded',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return 'f/{self.Category.slug}/self.slug/'



##Cart Related Stuff
class Cart(models.Model):
    user_id  = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    Products = models.ManyToManyField(Product, through='CartProduct')

    def __str__(self):
        return self.user_id.username

class CartProduct(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quan = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    # is_binding = models.BooleanField(default=False)
    # gift_message = models.CharField(max_length=255,default="  ",null=True,blank=True)
    # is_gift = models.BooleanField(default=False)

    # gift_from = models.CharField(max_length=20,default="  ",null=True,blank=True)
    # gift_box = models.BooleanField(default=False)


    def __str__(self):
        return self.user.username + self.Product.title


##whishlist
##Cart Related Stuff
class Wishlist(models.Model):
    user_id  = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    Products = models.ManyToManyField(Product, through='WishlistProduct')

    def __str__(self):
        return self.user_id.username

class WishlistProduct(models.Model):
    userx = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + self.Product.title

class ProductUnavailable(models.Model):
    Products = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer_mail_id = models.EmailField(max_length=254,null=False,blank=False)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id



class Requestbook(models.Model):
    book_name = models.CharField(max_length=200)
    book_type = models.CharField(max_length=10,choices=Book_type,default="")
    book_relatedto = models.CharField(max_length=10,choices=Book_relatedto,default="")
    book_desp = models.TextField()
    book_img = models.ImageField(upload_to="uploads/Request/",blank=True,null=True)
    book_required = models.CharField(max_length=10,null=True)
    customer_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200,null=True, blank=True)
    customer_phone = models.IntegerField(null=True, blank=True)
    customer_mail_id = models.EmailField(max_length=254,null=False,blank=False)
    ispriority = models.BooleanField(default=False)

class EcomOrder(models.Model):
    PAYMENT_METHODS = (
        ("1","Online Payment"),
        ("2", "Cash Payment"),
    )

    Order_placed_BY = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='order_placed_by_User',default=1)
    total_products = models.IntegerField(default=0)
    order_total = models.IntegerField(default=100)
    order_price = models.IntegerField(default=100)
    payment_mode = models.CharField(
        null=False, choices=PAYMENT_METHODS,max_length=20, default="Cash Payment")
    products = models.TextField(default="")
    address = models.CharField(max_length=100, default="")
    order_completed = models.BooleanField(default=False)
    date_of_ordering = models.DateField(default=date.today)
    date_of_delivery = models.DateField(default=DT.date.today() + DT.timedelta(days=5))
    gift_message = models.TextField(default="",null=True, blank=True)
    gift_from = models.CharField(max_length=255, default="",null=True, blank=True)
    order_status = models.CharField(choices=Order_Status_Choice,max_length=20, default="Order Created")
    contact_name = models.CharField(max_length=25)
    contact_no = models.CharField(max_length=10)

    def __str__(self):
        return str(self.id)

    #order_handled_by = models.ForeignKey(Customer,limit_choices_to={'is_staff': True}, on_delete=models.DO_NOTHING,blank=True,null=True,related_name='order_Handled_by_User')


class Exchange_return(models.Model):
    return_exchange_option = (
        ("1","Return"),
        ("2", "Exchnage"),
    )
    #order_id = models.ForeignKey(EcomOrder, on_delete=models.CASCADE)
    orderplacedby = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='orderplacedbyuser',default=1)
    option = models.CharField(choices=return_exchange_option,max_length=20)
    reason = models.CharField(choices=Return_Choices,max_length=20)
    comment = models.CharField(max_length=25,default="",null=True, blank=True)



class Refund_bankdetails(models.Model):
    returnid = models.ForeignKey(Exchange_return, on_delete=models.CASCADE,default="0")
    recipent_name = models.CharField(max_length=20)
    account_number = models.CharField(max_length=15)
    ifsc_code = models.CharField(max_length=10)
    updated_datetime = models.DateTimeField(auto_now=True)
    refund_completed = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.returnid



class Refund_upidetails(models.Model):
    returnid = models.ForeignKey(Exchange_return, on_delete=models.CASCADE,default="0")
    recipent_name = models.CharField(max_length=20)
    recipent_upi_id = models.CharField(max_length=15)
    updated_datetime = models.DateTimeField(auto_now=True)
    refund_completed = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.returnid

