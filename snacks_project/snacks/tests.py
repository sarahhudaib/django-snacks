from django.test import TestCase

# Create your tests here.
from django.test import SimpleTestCase
from django.urls import reverse


"""
- Test that home status codes
- Test that about status codes
- Test home url template use, including ancestor template.
- Test about url template use, including ancestor template.
"""

class SnacksTests(SimpleTestCase):
  """Class contains methods to test Snacks templates."""

  
  def test_about_status_codes(self):
    """Method to test whether the about page is accessible."""
    url = reverse('about')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    
  def test_home_status_codes(self):
    """ Method to check whether the home page is accessible."""
    url = reverse('home')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)

# -------------------------------------------------------------

  def test_about_url_template(self):
    """Method to test the about template for the about page."""
    url = reverse('about')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'about.html')
    self.assertTemplateUsed(response, 'base.html')
    
  def test_home_url_template(self):
    """Method to test the home template for the home page."""
    url = reverse('home')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'home.html')
    self.assertTemplateUsed(response, 'base.html')
    