from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserProfile, AppUser

# Create your tests here.
class UserProfileTestCase(TestCase):
    def test_profile_gets_created_when_user_created(self):
        user = get_user_model().objects.create(email="test@example.com",password="password")
        
        # assert user exists
        self.assertTrue(get_user_model().objects.filter(email="test@example.com").exists())
        
        # assert the profile was created
        self.assertTrue(UserProfile.objects.filter(user__email="test@example.com").exists())
        
        # assert default profile role is customer
        self.assertTrue(user.profile.role == 'customer')
        
    def test_profile_is_deleted_when_user_deleted(self):
        user = get_user_model().objects.create(email="test@example.com",password="password")
        
        user.delete()
        # assert user deleted
        with self.assertRaises(AppUser.DoesNotExist):
            user.refresh_from_db()
            
        # assert no profile exists
        self.assertIsNone(UserProfile.objects.first())
        
    def test_default_role_is_employee_for_superuser(self):
        user = get_user_model().objects.create_superuser(email="admin@example.com",password="password")
        
        # assert superuser created
        self.assertTrue(user.is_superuser)
        
        # assert default profile role is employee
        self.assertTrue(user.profile.role == 'employee')
        
        
        