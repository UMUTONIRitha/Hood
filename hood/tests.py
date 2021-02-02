from django.test import TestCase
# Create your tests here.
from .models import Profile,Neighbourhood,Post
from django.contrib.auth.models import User
import datetime as dt


class ProfileTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):
        self.user = User.objects.create(id =1,username='riri')
        self.profile = Profile(firstname = ' Rita',lastname = 'umutoni,profile_photo = 'babyb.jpeg',bio = 'Nice',date = '12.2.2121', user = self.user)
  

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        '''
        test image by save
        '''
        self.profile.save_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>=1) 

    def test_delete_method(self):
        '''
        test of delete image
        '''
        self.profile.save_profile()
        profile=Profile.delete_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile)>=0) 

        

class NeighbourhoodTestClass(TestCase):

    def setUp(self):
     
        self.neighbourhood=Neighbourhood.objects.create(neighbourhood='goood')
      

    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,Neighbourhood))

    def test_save_method(self):
        '''
        test image by save
        '''
        self.neighbourhood.save_neighbourhoods()
       neighbourhood=Neighbourhood.objects.all()
        self.assertTrue(len(comm)>0) 


       



class PostTestClass(TestCase):
    '''
    images test method
    '''
    def setUp(self):
        self.post = Post(user ='rita', name='test', neighborhood='good')

    

        # Testing Instance
        def test_instance(self):
            self.assertTrue(isinstance(self.post,Post))

        # Testing the save method
        def test_save_method(self):
            self.post=Post(name='cat',user=self.user1,likes="1",post="image")
            self.e.save_post()
            post = Post.objects.all()
            self.assertTrue(len(post) >= 1)

    

   