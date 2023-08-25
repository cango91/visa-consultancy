from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from forms_service.fields import TextField
from forms_service.models import FormDefinition


class WizardAPITestCase(TestCase):
    def test_all_forms_endpoint(self):
        user = get_user_model().objects.create(email="test@example",password="password",name="test user")
        user.profile.role = 'employee'
        user.save()
        
        form_field = TextField("Your name")
        form_definition = FormDefinition.objects.create(
            version=1,
            definition= form_field.serialize(),
            translations={"en": "English"},
            default_lang_code="en",
            status="draft",
            created_by=user
        )
        client = Client()
        response = client.get('/forms/wizard/definitions/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [
            {
                'name': form_definition.name,
                'status': 'draft',
                'description': form_definition.description,
                'version': 1,
                'default_lang_code': 'en',
                'created_at': str(form_definition.created_at),
                'created_by__name': user.name,
                'definition': form_field.serialize(),
                'translations': form_definition.translations
            }
        ])
        
    def test_get_form_endpoint(self):
        user = get_user_model().objects.create(email="test@example",password="password",name="test user")
        user.profile.role = 'employee'
        user.save()
        
        form_field = TextField("Your name")
        form_definition = FormDefinition.objects.create(
            version=1,
            definition= form_field.serialize(),
            translations={"en": "English"},
            default_lang_code="en",
            status="draft",
            created_by=user
        )
        client = Client()
        response = client.get(f'/forms/wizard/definitions/{form_definition.pk}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 
            {
                'name': form_definition.name,
                'status': 'draft',
                'description': form_definition.description,
                'version': 1,
                'default_lang_code': 'en',
                'created_at': str(form_definition.created_at),
                'created_by__name': user.name,
                'definition': form_field.serialize(),
                'translations': form_definition.translations
            }
        )
    
    def test_get_fields(self):
        client = Client()
        response = client.get(f'/forms/wizard/fields/').json()
        self.assertTrue("text" in response)
        self.assertTrue("number" in response)
        self.assertTrue("select" in response)
        
    def test_get_field(self):
        client = Client()
        response = client.get(f'/forms/wizard/fields/text').json()
        self.assertFalse(len(response.get("extra_attributes")))
        self.assertTrue(len(response.get("validators"))>1)
        
    def test_can_only_get(self):
        client = Client()
        response = client.post('/forms/wizard/fields/')
        self.assertEqual(response.status_code,405)