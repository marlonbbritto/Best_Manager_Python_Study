from user_data.models import Employeer
from django.test import TestCase
from django.db.utils import IntegrityError
from django.contrib.auth.models import User

class EmployeerModelTestCase(TestCase):

    def setUp(self):
        self.existing_user = User.objects.create_user(
            username='admin_teste1',
            password='123456abcdefg',
            email='teste@teste.com',
            first_name='teste1',
            last_name='teste2'
        )

        self.employeer = Employeer.objects.create(
            company_name='Empresa teste 1',
            admin_user=self.existing_user,
            country='Brazil',
            state='Paraná',
            city='Maringá'
        )

    def test_create_duplicate_company(self):
        '''Testa a prevenção de criar uma empresa com o mesmo nome.'''
        with self.assertRaises(IntegrityError):
            Employeer.objects.create(
                company_name='Empresa teste 1',
                admin_user=self.existing_user,
                country='Brazil',
                state='Paraná',
                city='Maringá'
            )
