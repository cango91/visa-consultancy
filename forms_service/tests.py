from django.test import TestCase
from users_service.models import AppUser
from forms_service.models import FormDefinition, FormSubmission
from django.db import models
from .validators.tests import *
from .fields.tests import *
from .factories.tests import *

class FormDefinitionTestCase(TestCase):
    
    # Scenario 1: Test the creation of a form definition by a user.
    def test_create_form_definition_by_user(self):
        # Create a user
        user = AppUser.objects.create(email='test@example.com', password='password')
        
        # Define a form using the created user
        form_definition = FormDefinition.objects.create(
            version=1,
            definition={"field": "value"},
            translations={"en": "English"},
            default_lang_code="en",
            status="draft",
            created_by=user
        )
        
        # Validate that the form definition is created with the correct attributes
        self.assertEqual(form_definition.version, 1)
        self.assertEqual(form_definition.default_lang_code, "en")
        
        # Validate that the form definition is linked to the correct user
        self.assertEqual(form_definition.created_by, user)

    # Scenario 2: Test the deletion of a user when the form has no associated submissions.
    def test_delete_user_with_no_submissions(self):
        # Create a user
        user = AppUser.objects.create(email='test@example.com', password='password')
        
        # Define a form using the created user
        form_definition = FormDefinition.objects.create(
            version=1,
            definition={"field": "value"},
            translations={"en": "English"},
            default_lang_code="en",
            status="draft",
            created_by=user
        )
        
        # Delete the user
        user.delete()
        
        # Validate that the form definition is also deleted
        self.assertFalse(FormDefinition.objects.filter(id=form_definition.id).exists())

    # Scenario 3: Test the deletion of a user when a created form has associated submission data.
    def test_delete_user_with_submissions(self):
        # Create users
        user = AppUser.objects.create(email='test@example.com', password='password')
        customer = AppUser.objects.create(email='customer@example.com',password='password')
        
        # Define a form using the created user
        form_definition = FormDefinition.objects.create(
            version=1,
            definition={"field": "value"},
            translations={"en": "English"},
            default_lang_code="en",
            status="draft",
            created_by=user
        )
        
        # Create a form submission associated with the form definition
        FormSubmission.objects.create(
            form_id=form_definition,
            submitted_by=customer,
            data={"answer": "response"}
        )
        
        user.delete()
        # Assert user is deleted
        with self.assertRaises(AppUser.DoesNotExist):
            user.refresh_from_db()

        # Validate that the form definition is not deleted but marked as 'deleted'
        form_definition.refresh_from_db()
        self.assertEqual(form_definition.status, 'deleted')
        
        # Validate that the submission data remains intact
        self.assertTrue(FormSubmission.objects.filter(form_id=form_definition).exists())

    # Scenario 4: Test the deletion of user when they have submissions data
    def test_delete_user(self):
        user = AppUser.objects.create(email='test@example.com', password='password')
        # Define a form using the created user
        form_definition = FormDefinition.objects.create(
            version=1,
            definition={"field": "value"},
            translations={"en": "English"},
            default_lang_code="en",
            status="draft",
            created_by=user
        )
        
        customer = AppUser.objects.create(email='customer@example.com',password='password')
        # Create a form submission by the customer
        FormSubmission.objects.create(
            form_id=form_definition,
            submitted_by=customer,
            data={"answer": "response"}
        )
        
        # assert submission exists
        self.assertTrue(FormSubmission.objects.filter(submitted_by=customer).exists())
        
        customer.delete()
        # assert customer deleted
        with self.assertRaises(AppUser.DoesNotExist):
            customer.refresh_from_db()
        # assert submission deleted
        self.assertFalse(FormSubmission.objects.exists())
        
        # assert the form still exists
        form_definition.refresh_from_db()
        self.assertEqual(FormDefinition.objects.first(),form_definition)

        
        
