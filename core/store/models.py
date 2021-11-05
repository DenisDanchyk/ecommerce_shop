from django.db import models


class Category(models.Model):
    """ Category model """

    name = models.CharField(max_length=255, verbose_name="Category")
    slug = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    """ Template for all products """

    class Meta:
        abstract = True

    name = models.CharField(max_length=255, verbose_name="Name of product")
    description = models.TextField(verbose_name="Product description")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    discount_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to="product_photo/",
        null=True,
        blank=True
    )

    image = models.ImageField(upload_to="product_photo/")
    guarantee = models.IntegerField(verbose_name="Guarantee (month)")

    slug = models.SlugField(max_length=255)
    in_order = models.BooleanField(
        default=False, verbose_name="The order is placed")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated")

    def __str__(self) -> str:
        return self.name


class Computer(Product):
    COMPUTER_OR_LAPTOR = {
        ("Computer", "Computer"),
        ("Laptop", "Laptop")
    }

    computer_or_laptop = models.CharField(
        max_length=10,
        choices=COMPUTER_OR_LAPTOR,
    )
    brief_technical_characteristics = models.CharField(
        max_length=255,
        verbose_name="Brief technical characteristics"
    )
    ram_size = models.CharField(
        max_length=255,
        verbose_name="Ram size"
    )
    motherboard = models.CharField(
        max_length=255,
        verbose_name="Matherboard"
    )
    cpu = models.CharField(max_length=255, verbose_name="Processor")
    bp = models.CharField(max_length=255, verbose_name="Power Supply")
    vedio_card = models.CharField(max_length=255, verbose_name="Video card")
    hdd = models.CharField(max_length=255, verbose_name="HDD")

    class Meta:
        verbose_name = "Computer"
        verbose_name_plural = "Computers"


class Smartphone(Product):
    COMMUNICATION_STANDARD = {
        ("2G", "2G"),
        ("3G", "3G"),
        ("4G", "3G"),
        ("5G", "5G")
    }
    MATRIX_TYPE = {
        ("OLED", "OLED"),
        ("AMOLED", "AMOLED"),
        ("SUPER AMOLED", "SUPER AMOLED"),
        ("IPS-LSD", "IPS-LSD"),
        ("TFT-LCD", "TFT-LSD"),
        ("CAPACITIVE TOUCHSCREEN LCD", "CAPACITIVE TOUCHSCREEN LCD"),
    }
    OPERATING_SYSTEM = {
        ('IOS', 'IOS'),
        ('ANDROID', 'ANDROID')
    }
    communication_standard = models.CharField(
        max_length=2,
        choices=COMMUNICATION_STANDARD,
        verbose_name="Communication standart"
    )
    matrix_type = models.CharField(
        max_length=30,
        choices=MATRIX_TYPE,
        verbose_name="Type of matrix"
    )
    displat_diagonal = models.FloatField(verbose_name="Display diagonal")
    display_resolution = models.CharField(
        max_length=15,
        verbose_name="Display resolution"
    )
    hz = models.IntegerField(verbose_name="Screen refresh rate (Hz)")
    built_in_memory = models.IntegerField(
        verbose_name="Built-in memory (GB)")
    operating_system = models.CharField(
        max_length=30,
        choices=OPERATING_SYSTEM,
        verbose_name="Operating system"
    )
    main_camera_megapixels = models.IntegerField(
        verbose_name="The number of megapixels in the main camera"
    )
    front_camera_megapixels = models.IntegerField(
        verbose_name="The number of megapixels in the front camera"
    )
    additionally = models.TextField(
        blank=True,
        null=True,
        verbose_name="Additionally"
    )

    class Meta:
        verbose_name = "Smartphone"
        verbose_name_plural = "Smartphones"


class Furniture(Product):
    peculiarities = models.CharField(
        max_length=255, verbose_name="Features")
    material = models.CharField(max_length=100, verbose_name="Material")
    color = models.CharField(max_length=55, verbose_name="Color")
    size = models.CharField(max_length=55, verbose_name="Size")
    height = models.IntegerField(verbose_name="Height")
    weight = models.IntegerField(verbose_name="Weight")

    class Meta:
        verbose_name = "Furniture"
        verbose_name_plural = "Furniture"


class Clothes(Product):
    SIZE = {
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    }
    GENDER = {
        ('MAN', 'MAN'),
        ('WOMAN', 'WOMAN')
    }
    brand = models.CharField(max_length=55, verbose_name="Brand")
    gender = models.CharField(
        max_length=5, choices=GENDER, verbose_name="Gender")
    color = models.CharField(max_length=55, verbose_name="Color")
    size = models.CharField(max_length=3, choices=SIZE, verbose_name="Size")
    material = models.CharField(max_length=100, verbose_name="Material")
    country_of_origin = models.CharField(
        max_length=55,
        verbose_name="Country of origin"
    )

    class Meta:
        verbose_name = "Clothes"
        verbose_name_plural = "Clothes"


class Shoes(Product):
    SIZE = {
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
    }
    SEASON = {
        ('SPRING', 'SPRING'),
        ('AUTUMN', 'AUTUMN'),
        ('WINTER', 'WINTER'),
        ('SUMMER', 'SUMMER')
    }
    season = models.CharField(
        max_length=6,
        choices=SEASON,
        verbose_name="Season"
    )
    country_of_origin = models.CharField(
        max_length=55,
        verbose_name="Країна виробник"
    )
    brand = models.CharField(max_length=55, verbose_name="Brand")
    color = models.CharField(max_length=55, verbose_name="Color")
    size = models.CharField(max_length=3, choices=SIZE, verbose_name="Size")
    material = models.CharField(max_length=100, verbose_name="Material")

    class Meta:
        verbose_name = "Shoes"
        verbose_name_plural = "Shoes"
