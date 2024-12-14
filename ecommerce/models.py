


from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)  # Product name
    description = models.TextField()  # Detailed description of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    stock = models.PositiveIntegerField(default=0)  # Stock availability
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Image of the product
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for product creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for product updates
    is_active = models.BooleanField(default=True)  # Visibility status of the product
    slug = models.SlugField(unique=True, blank=True)  # SEO-friendly URL field

    def save(self, *args, **kwargs):
        # Automatically generate slug if not provided
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']  # Sort products by the most recent first


class TipResource(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)  # Add the slug field
    content = models.TextField(help_text="Main content about the tip or resource.")
    health_benefits = models.TextField(help_text="Health benefits or additional information.", blank=True, null=True)
    image = models.ImageField(upload_to='tips_resources/', blank=True, null=True)  # Image for the tip/resource
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the post is created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp of when the post is last updated

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Generate slug based on title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Tip/Resource"
        verbose_name_plural = "Tips/Resources"
        ordering = ['-created_at']  # Order by creation date, newest first


class TeamMember(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the team member.")
    role = models.CharField(max_length=150, help_text="Role of the team member, e.g., CEO, Marketing Head.")
    bio = models.TextField(blank=True, null=True, help_text="Short bio or description of the team member.")
    photo = models.ImageField(upload_to='team_members/', blank=True, null=True, help_text="Photo of the team member.")
    joined_date = models.DateField(blank=True, null=True, help_text="Date the team member joined.")
    active = models.BooleanField(default=True, help_text="Mark as active to display on the website.")

    def __str__(self):
        return f"{self.name} - {self.role}"

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"
        ordering = ['-joined_date']  # Sort team members by most recent join date first




