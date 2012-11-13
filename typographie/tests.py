from django.utils import unittest
from templatestags.typographie import *

class TypographieTestCase(unittest.TestCase):

  def test_spaces_text(self):
    tests = [
              u"Deux points:ok",
              u"Deux points\xa0:ok",
              u"Deux points\xa0:\xa0ok",
              u"Deux points :ok",
              u"Deux points : ok", 
              u"Deux points\xa0: ok",
              u"Deux points :\xa0ok",
              u"Deux points\xa0:\nok",
              u"Deux points\xa0:  ok",
            ]
    result = u"Deux points\xa0: ok"
    for test in tests:
      self.assertEqual(spaces(test),result)

  def test_spaces_html(self):
    tests = [
              u"<b>Deux points</b>:<b>ok</b>",
              u"<b>Deux points </b>:<b>ok</b>",
              u"<b>Deux points </b>:<b> ok</b>",
              u"<b>Deux points</b>:<b> ok</b>",

							u"<b>Deux points:</b><b>ok</b>",
              u"<b>Deux points :</b><b>ok</b>",
              u"<b>Deux points :</b><b> ok</b>",
              u"<b>Deux points:</b><b> ok</b>",

							u"<b>Deux points</b><b>:ok</b>",
              u"<b>Deux points </b><b>:ok</b>",
              u"<b>Deux points </b><b> :ok</b>",
              u"<b>Deux points</b><b>: ok</b>",
            ]
    result = u"<b>Deux points\xa0: </b><b>ok</b>"
    for test in tests:
      self.assertEqual(spaces(test),result)


    tests = [
              u"<b>Deux points</b>:<b>ok </b>",
            ]
    result = u"<b>Deux points\xa0: </b><b>ok </b>"
    for test in tests:
      self.assertEqual(spaces(test),result)

