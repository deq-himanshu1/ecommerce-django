from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

# we here we are going to create an account or account model as well as we will create account manager which is to handle the custom user
# model

# class to create superuser
class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            return ValueError("User must have email address")
        
        if not username:
            return ValueError("User must have username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # This class will take all the arguments from here but use create_user method to create user and apply all the permissions
    def create_superuser(self,first_name,last_name,username,email,password): 
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        # setting all the permission as True
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        
        return user


# creating custom user model
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)

    #required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    objects = MyAccountManager() # Telling this account class that we are using MyAccountManager for all MyAccountManager operations

    def __str__(self):
        return self.email # this means that when we return the account object inside template. so this should return email address
    
    # this must be present here whenever we create custom user model
    def has_perm(self, perm, obj=None):
        return self.is_admin # this means that user has permissions to do all the changes
    
    def has_module_perms(self, add_label):
        return True
    
    # What does has_module_perms(self, app_label) do?

    # app_label: The parameter passed to the method is a string representing the name (label) of an app (e.g., 'auth', 'myapp').

    # The method is supposed to return True if the user has any permissions in the given app. This can include view, add, change, or delete permissions.
