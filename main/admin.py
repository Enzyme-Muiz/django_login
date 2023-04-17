from django.contrib import admin


from .models import Tutorial, miRNA, image_upload


from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.


class miRNAadmin(admin.ModelAdmin):
	fields=[
	"location",
	"name"
	]

	formfield_overrides = {
	models.TextField: {
	'widget': TinyMCE()
	}
	}              

    




admin.site.register(Tutorial)
admin.site.register(miRNA, miRNAadmin)
#admin.site.register(Hotel)
admin.site.register(image_upload)
