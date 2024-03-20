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

        self.existing_user2 = User.objects.create_user(
            username='admin_teste2',
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
    def test_create_blank_company(self):
        '''Teste que verificar se bloqueia a criação de uma empresa com nome em branco'''
        with self.assertRaises(IntegrityError):
            Employeer.objects.create(
                company_name='',
                admin_user=self.existing_user,
                country='Brazil',
                state='Paraná',
                city='Maringá'
            )
    def test_create_employeer_country_default(self):

        '''Teste para verificar Default com country como Brazil quando não fornecido'''

        self.employeer1 = Employeer.objects.create(
            company_name='Empresa teste 2',
            admin_user=self.existing_user2,
            state='Paraná',
            city='Maringá'
        )
        
        # Adicionando uma declaração print para inspecionar o valor do campo country e as propriedades do objeto
        print("Objeto Employeer após a criação:", repr(self.employeer1))
        print("Valor do campo 'country' após a criação do Employeer:", self.employeer1.country)

        # Verificar se o país é preenchido com 'Brazil' por padrão
        self.assertEqual(self.employeer1.country, 'Brazil')


