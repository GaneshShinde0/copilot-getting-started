from django.db import models

class Expense(models.Model):
	name = models.CharField(max_length=100)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True)
	CATEGORY_CHOICES = (
		('general', 'General'),
		('food', 'Food'),
		('travel', 'Travel'),
		('entertainment', 'Entertainment'),
		('health', 'Health'),
		('clothing', 'Clothing'),
		('electronics', 'Electronics'),
		('other', 'Other'),
	)
	category = models.CharField(max_length=100, choices = CATEGORY_CHOICES)

	def __str__(self):
		return f'{self.name} - {self.amount}'