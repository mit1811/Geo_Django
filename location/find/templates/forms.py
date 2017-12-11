from .models import Location

class PostForm(models.Model):
	class Meta:
		fields = [
		"address",
		"position",
		]