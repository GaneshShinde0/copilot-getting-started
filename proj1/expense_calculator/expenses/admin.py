from django.contrib import admin

# Register your models here.
from .models import Expense

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
	"""
	these are the expense model fields
	name = models.CharField(max_length=100)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	timestamp = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)

	"""
	list_display = ['name', 'amount', 'timestamp', 'category']
	list_filter = ['category', 'timestamp']
	search_fields = ['name', 'amount']
	list_per_page = 10