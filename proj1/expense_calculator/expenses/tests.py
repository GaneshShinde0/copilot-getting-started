from django.test import TestCase
# imports for django_rest_framework tests
from rest_framework.test import APITestCase

from .models import Expense


class ExpenseTestCase(APITestCase):
    def setUp(self):
        # Create 5 Expenses usig bulk_create
        Expense.objects.bulk_create([
            Expense(name='Expense 1', amount=100, category='general'),
            Expense(name='Expense 2', amount=200, category='food'),
            Expense(name='Expense 3', amount=300, category='travel'),
            Expense(name='Expense 4', amount=400, category='entertainment'),
            Expense(name='Expense 5', amount=500, category='health')
        ])

    def test_expense_list(self):
        ## use client.get to get the list of expenses
        response = self.client.get('/api/expenses/')
        # check if the status code is 200
        self.assertEqual(response.status_code, 200)
        # check if there are 5 expenses
        self.assertEqual(len(response.data), 5)

    def test_expense_count(self):
        # get all expenses
        expenses = Expense.objects.all()
        # check if there are 5 expenses
        self.assertEqual(expenses.count(), 5)

    # test expense create using self.client.post
    def test_expense_create(self):
        # create an expense
        response = self.client.post('/api/expenses/', {
            'name': 'Expense 6',
            'amount': 600,
            'category': 'clothing'
        })
        # check if the status code is 201
        self.assertEqual(response.status_code, 201)
        # check if there are 6 expenses
        self.assertEqual(Expense.objects.all().count(), 6)
    # test expense delete using self.client.delete
    def test_expense_delete(self):
        # delete an expense
        response = self.client.delete('/api/expenses/1/')
        # check if the status code is 204
        self.assertEqual(response.status_code, 204)
        # check if there are 4 expenses
        self.assertEqual(Expense.objects.all().count(), 4)

    def test_expense_update(self):
        # update an expense
        response = self.client.put('/api/expenses/1/', {
            'name': 'Expense 1 Updated',
            'amount': 1000,
            'category': 'electronics'
        })
        # check if the status code is 200
        self.assertEqual(response.status_code, 200)
        # check if the expense is updated
        expense = Expense.objects.get(id=1)
        self.assertEqual(expense.name, 'Expense 1 Updated')
        self.assertEqual(expense.amount, 1000)
        self.assertEqual(expense.category, 'electronics')

    def tearDown(self):
        # delete all expenses
        Expense.objects.all().delete()