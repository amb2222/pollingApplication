import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# Create your models here.
class Question(models.Model):
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # modifies how a method is rendered in the Django admin list view
    @admin.display(
        boolean=True,                            # Display as a checkmark (✔/✖) based on True/False
        ordering="pub_date",                        # Allows sorting this column by the 'pub_date' field
        description="Published recently?",            # Column header in the admin UI
    )
    
    def __str__(self):
        return self.description
    
    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now - \
            datetime.timedelta(days=1)
        

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.description
    
