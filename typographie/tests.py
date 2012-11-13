from django.utils import unittest
from templatetags.typographie import *

class spacesTestCase(unittest.TestCase):


  def get_text_tests(self, c):
      
      return [test % c for test in  [
              u"Du texte%sok",
              u"Du texte\xa0%sok",
              u"Du texte\xa0%s\xa0ok",
              u"Du texte %sok",
              u"Du texte %s ok", 
              u"Du texte\xa0%s ok",
              u"Du texte %s\xa0ok",
              u"Du texte\xa0%s\nok",
              u"Du texte\xa0%s  ok",
            ]]
  
  def get_html_tests(self, c):
      
      return [test % c for test in  [
              u"<b>Du texte</b>%s<b>ok</b>",
              u"<b>Du texte </b>%s<b>ok</b>",
              u"<b>Du texte </b>%s<b> ok</b>",
              u"<b>Du texte</b>%s<b> ok</b>",

              u"<b>Du texte%s</b><b>ok</b>",
              u"<b>Du texte %s</b><b>ok</b>",
              u"<b>Du texte %s</b><b> ok</b>",
              u"<b>Du texte%s</b><b> ok</b>",

              u"<b>Du texte</b><b>%sok</b>",
              u"<b>Du texte </b><b>%sok</b>",
              u"<b>Du texte </b><b> %sok</b>",
              u"<b>Du texte</b><b>%s ok</b>",
            ]]
  
  def get_html_tests_2(self, c):
      
      return [test % c for test in [
              u"<b>Du texte</b>%s<b>ok </b>",
            ]]
  
  def test_spaces_deux_points_text(self):
    
    tests = self.get_text_tests(u':')
    result = u"Du texte\xa0: ok"
    for test in tests:
      self.assertEqual(spaces(test),result)


  def test_spaces_virgule_text(self):
    tests = self.get_text_tests(u',')
    result = u"Du texte, ok"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def test_spaces_point_text(self):
    tests = self.get_text_tests(u'.')
    result = u"Du texte. ok"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def test_spaces_point_virgule_text(self):
    
    tests = self.get_text_tests(u';')
    result = u"Du texte\xa0; ok"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  
  def test_spaces_point_exclamation_text(self):
    
    tests = self.get_text_tests(u'!')
    result = u"Du texte\xa0! ok"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
      
  def test_spaces_point_interrogation_text(self):
    
    tests = self.get_text_tests(u'?')
    result = u"Du texte\xa0? ok"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def test_spaces_points_suspensions_text(self):
    
    tests = self.get_text_tests(u'\u2026')
    result = u"Du texte\u2026 ok"
    for test in tests:
      self.assertEqual(spaces(test),result)
   
  def test_spaces_points_suspensions_text_2(self):
    
    tests = self.get_text_tests(u'...')
    result = u"Du texte\u2026 ok"
    for test in tests:
      self.assertEqual(spaces(ellipsis(test)),result)
   
  def test_spaces_paranthese_ouvrante_text(self):
    
    tests = self.get_text_tests(u'(')
    result = u"Du texte (ok"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def test_spaces_crochet_ouvrant_text(self):
    
    tests = self.get_text_tests(u'[')
    result = u"Du texte [ok"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def test_spaces_paranthese_fermante_text(self):
    
    tests = self.get_text_tests(u')')
    result = u"Du texte) ok"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def test_spaces_crochet_fermant_text(self):
    
    tests = self.get_text_tests(u']')
    result = u"Du texte] ok"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def test_spaces_guillemet_ouvrant_text(self):
    
    tests = self.get_text_tests(u'\xab')
    result = u"Du texte \xab\xa0ok"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def test_spaces_guillemet_fermant_text(self):
    
    tests = self.get_text_tests(u'\xbb')
    result = u"Du texte\xa0\xbb ok"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def test_spaces_apostrophe_text(self):
    
    tests = self.get_text_tests(u"\u2019")
    result = u"Du texte\u2019ok"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def  test_spaces_deux_points_html(self):
    tests = self.get_html_tests(u':')
    result = u"<b>Du texte\xa0: </b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

    tests =self.get_html_tests_2(u':')
    result = u"<b>Du texte\xa0: </b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def  test_spaces_virgule_html(self):
    tests = self.get_html_tests(u',')
    result = u"<b>Du texte, </b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

    tests =self.get_html_tests_2(u',')
    result = u"<b>Du texte, </b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def  test_spaces_point_html(self):
    tests = self.get_html_tests(u'.')
    result = u"<b>Du texte. </b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

    tests =self.get_html_tests_2(u'.')
    result = u"<b>Du texte. </b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
      
  def  test_spaces_point_virgule_html(self):
    tests = self.get_html_tests(u';')
    result = u"<b>Du texte\xa0; </b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

    tests =self.get_html_tests_2(u';')
    result = u"<b>Du texte\xa0; </b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

  def  test_spaces_point_exclamation_html(self):
    tests = self.get_html_tests(u'!')
    result = u"<b>Du texte\xa0! </b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

    tests =self.get_html_tests_2(u'!')
    result = u"<b>Du texte\xa0! </b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(test),result)


  def  test_spaces_point_interrogation_html(self):
    tests = self.get_html_tests(u'?')
    result = u"<b>Du texte\xa0? </b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

    tests =self.get_html_tests_2(u'?')
    result = u"<b>Du texte\xa0? </b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
      
  def  test_spaces_points_suspensions_html(self):
    tests = self.get_html_tests(u'\u2026')
    result = u"<b>Du texte\u2026 </b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

    tests =self.get_html_tests_2(u'\u2026')
    result = u"<b>Du texte\u2026 </b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def  test_spaces_points_suspensions_html_2(self):
    tests = self.get_html_tests(u'...')
    result = u"<b>Du texte\u2026 </b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(ellipsis(test)),result)

    tests =self.get_html_tests_2(u'...')
    result = u"<b>Du texte\u2026 </b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(ellipsis(test)),result)
      
  def  test_spaces_paranthese_ouvrante_html(self):
    tests = self.get_html_tests(u'(')
    result = u"<b>Du texte (</b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

    tests =self.get_html_tests_2(u'(')
    result = u"<b>Du texte (</b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def  test_spaces_crochet_ouvrant_html(self):
    tests = self.get_html_tests(u'[')
    result = u"<b>Du texte [</b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

    tests =self.get_html_tests_2(u'[')
    result = u"<b>Du texte [</b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def  test_spaces_paranthese_fermante_html(self):
    tests = self.get_html_tests(u')')
    result = u"<b>Du texte) </b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

    tests =self.get_html_tests_2(u')')
    result = u"<b>Du texte) </b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def  test_spaces_crochet_fermant_html(self):
    tests = self.get_html_tests(u']')
    result = u"<b>Du texte] </b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

    tests =self.get_html_tests_2(u']')
    result = u"<b>Du texte] </b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def  test_spaces_guillemet_ouvrant_html(self):
    tests = self.get_html_tests(u'\xab')
    result = u"<b>Du texte \xab\xa0</b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

    tests =self.get_html_tests_2(u'\xab')
    result = u"<b>Du texte \xab\xa0</b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def  test_spaces_guillemet_fermant_html(self):
    tests = self.get_html_tests(u'\xbb')
    result = u"<b>Du texte\xa0\xbb </b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

    tests =self.get_html_tests_2(u'\xbb')
    result = u"<b>Du texte\xa0\xbb </b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(test),result)
      
  def  test_spaces_apostrophe_html(self):
    tests = self.get_html_tests(u"\u2019")
    result = u"<b>Du texte\u2019</b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

    tests =self.get_html_tests_2(u"\u2019")
    result = u"<b>Du texte\u2019</b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(test),result)