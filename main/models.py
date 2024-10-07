from django.db import models

# Create your models here.

from django.db import models

class intro(models.Model):
    intro = models.TextField()

class bio(models.Model):
    intro = models.TextField()


class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/')
    short_bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ExtendedBio(models.Model):
    personal_info = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)
    bio = models.TextField()
    personal_statement = models.TextField()
    technical_skills = models.TextField()
    soft_skills = models.TextField()
    language_proficiency = models.TextField()

    def __str__(self):
        return f"Extended Bio of {self.personal_info.name}"

class WorkExperience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    responsibilities = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    graduation_date = models.DateField()
    cgpa = models.FloatField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Certification(models.Model):
    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=100)
    issue_date = models.DateField()
    certiimage = models.ImageField(upload_to='certification/')

    def __str__(self):
        return self.name

class Award(models.Model):
    name = models.CharField(max_length=100)
    date_awarded = models.DateField()
    awardimage = models.ImageField(upload_to='certification/')

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    role = models.CharField(max_length=100)
    technologies_used = models.TextField()
    project_link = models.URLField()
    image = models.ImageField(upload_to='projects/', null=True, blank=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    skillimage = models.ImageField(upload_to='projects/', null=True, blank=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"Testimonial by {self.author}"

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    excerpt = models.TextField()

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class SocialMediaLink(models.Model):
    platform = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.platform
