from django.test import TestCase, Client
from django.urls import reverse
from user_data.models import User
from user_data.forms import UserForms

class RegisterCompanyAdminTest(TestCase):
    
   def setUp(self):
      self.client=Client()
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
      response = self.client.post(self.register_admin_url,data)
      self.assertEqual(response.status_code,302)
      self.assertTrue(User.objects.filter(username='testuser').exists())

   def test_register_admin_existing_username(self):
      # Cria um usuário existente
      User.objects.create_user(username='existinguser', password='testpassword')

      data = {
         'user_name': 'existinguser',  # Tentando usar um nome de usuário que já existe
         'password': 'testpassword',
         'password2': 'testpassword',
         'email': 'test@example.com',
         'first_name': 'Test',
         'surname': 'User'
      }
      # Enviar a solicitação POST
      response = self.client.post(self.register_admin_url, data, follow=True)

      # Verificar se o redirecionamento ocorreu
      self.assertEqual(response.status_code, 200)

      # Verificar se a mensagem de erro está presente na página de destino
      self.assertContains(response, 'Esse nome de usuario ja esta sendo utilizado')
   
   def test_register_admin_diferent_password(self):
       data = {
            'user_name': 'testuser',
            'password': 'testpassword',
            'password2': 'mismatch',  # Senhas não coincidem
            'email': 'test@example.com',
            'first_name': 'Test',
            'surname': 'User'
        }
       response = self.client.post(self.register_admin_url, data,follow=True)
       self.assertEqual(response.status_code,200)
       self.assertContains(response,'As senhas devem ser identicas')
   def test_register_admin_invalid_form(self):
        response = self.client.post(self.register_admin_url, {})
        
        # Verificar se a página é recarregada
        self.assertEqual(response.status_code, 200)

        # Verificar se o formulário é renderizado novamente com erros
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('user_name', form.errors)
        self.assertIn('password', form.errors)
        self.assertIn('password2', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('surname', form.errors)
      


   
        