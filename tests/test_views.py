import logging
from django.test import TestCase, Client
from django.urls import reverse
from user_data.models import Employeer, Positions
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

logger = logging.getLogger(__name__)

class RegisterCompanyAdminTest(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.register_admin_url = reverse('register_first_admin')

    def test_register_admin_sucess(self):
        data = {
            'user_name': 'testuser',
            'password': 'testpassword',
            'password2': 'testpassword',
            'email': 'test@example.com',
            'first_name': 'Test',
            'surname': 'User'
        }
        response = self.client.post(self.register_admin_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_admin_existing_username(self):
        User.objects.create_user(username='existinguser', password='testpassword')
        data = {
            'user_name': 'existinguser',
            'password': 'testpassword',
            'password2': 'testpassword',
            'email': 'test@example.com',
            'first_name': 'Test',
            'surname': 'User'
        }
        response = self.client.post(self.register_admin_url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Esse nome de usuario ja esta sendo utilizado')
   
    def test_register_admin_diferent_password(self):
        data = {
            'user_name': 'testuser',
            'password': 'testpassword',
            'password2': 'mismatch',
            'email': 'test@example.com',
            'first_name': 'Test',
            'surname': 'User'
        }
        response = self.client.post(self.register_admin_url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'As senhas devem ser identicas')
        
    def test_register_admin_invalid_form(self):
        response = self.client.post(self.register_admin_url, {})
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('user_name', form.errors)
        self.assertIn('password', form.errors)
        self.assertIn('password2', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('surname', form.errors)
      
class RegisterCompanyTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_company_url = reverse('company_register')
        self.valid_data = {
            'company_name': 'Nova Empresa',
            'admin_user': User.objects.create(username='admin', password='Teste321').pk,
            'country': 'Brazil',
            'state': 'Paraná',
            'city': 'Maringá'
        }
        # Criar um contador para garantir nomes de usuário exclusivos em cada execução do teste
        self.username_counter = 1

    def test_invalid_form_submission(self):
        # Criar um nome de usuário exclusivo usando o contador
        username = f'admin_unique_{self.username_counter}'
        self.username_counter += 1
        
        # Enviar dados inválidos para o formulário (por exemplo, omitir o campo company_name)
        invalid_data = {
            'admin_user': User.objects.create(username=username, password='Teste321').pk,
            'country': 'Brazil',
            'state': 'InvalidState',  # Estado inválido para forçar uma falha de validação
            'city': 'Maringá'
        }
        
        # Enviar uma solicitação POST com dados inválidos
        response = self.client.post(self.register_company_url, invalid_data)

        # Verificar se a resposta redireciona para 'index'
        self.assertRedirects(response, reverse('index'))

        # Verificar se existem mensagens de erro na sessão de mensagens
        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(messages)  # Verifica se há mensagens disponíveis

        # Verificar se a parte relevante da mensagem de erro esperada está presente em pelo menos uma das mensagens
        error_message_part = 'O formulário contém os seguintes erros:'
        self.assertTrue(any(error_message_part in str(message) for message in messages))






 
      
       

class RegisterPositionViewTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.company = Employeer.objects.create(company_name='Test Company', admin_user=self.user)
        self.position_data = {
            'company_name': self.company.id,
            'position': 'Test Position',
            'level': 1
        }
        self.invalid_position_data = {
            'company_name': self.company.id + 1,  
            'position': 'Test Position',
            'level': 1
        }

    def test_access_view_authenticated_user(self):
        """Teste que verifica se o usuario esta autenticado"""
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('register_position'))
        self.assertEqual(response.status_code, 200)

    def test_register_position_success(self):
        """Teste que valida o registro de uma posição de uma empresa"""
        self.client.login(username='test_user', password='test_password')
        response = self.client.post(reverse('register_position'), data=self.position_data)
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Positions.objects.filter(position='Test Position').count(), 1)
   
    def test_register_position_failure_permission(self):
        """Teste que verifica que um formulario de posição nao valido não ira criar uma posição"""
        self.client.login(username='test_user', password='test_password')
        response = self.client.post(reverse('register_position'), data=self.invalid_position_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Positions.objects.filter(position='Test Position').count(), 0)
