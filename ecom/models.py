from django.db import models


subcategory_choice =(
    ("Textbooks", "Textbooks"),
    ("Digest", "Digest"),
    ("21 Sets", "21 sets"),
    ("Combo", "combo"),
    ("biograhy", "biograhy"),
    ("storyteller", "storyteller"),
    ("Helping Hand","Helping Hnad")
)


Medium_choice =(
    ("English", "English"),
    ("Marathi", "Marathi"),
    ("Hindi", "Hindi"),
    ("Science", "Science"),
    ("Commerce", "Commerce"),
    ("Arts", "Arts"),
)

class category(models.Model):
	category=models.CharField(max_length=20)

	def __str__(self):
		return self.category


class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    medium = models.CharField(max_length=10,choices=Medium_choice,default="")
    sub_category= models.CharField(max_length=50,choices=subcategory_choice, default="")
    price=models.PositiveIntegerField(default=0)
    image= models.ImageField(upload_to="shop/images",default="")


    def __str__(self):
    	return self.product_name

