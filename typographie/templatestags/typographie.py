from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import smart_str, force_unicode

import re
register = template.Library()


@register.filter
@stringfilter
def ellipsis(text):
  pass

@register.filter
@stringfilter
def spaces(text):
  text = re.sub(r'\s*(<[^>]+>|):(<[^>]+>|)\s*',u':\\1\\2',text,flags=re.U)
  text = re.sub(r':\s*(<[^>]+>|)(<[^>]+>|)\s*',u':\\1\\2',text,flags=re.U)
  text = re.sub(r'\s*(<[^>]+>|)(<[^>]+>|)\s*:',u':\\1\\2',text,flags=re.U)
  text = re.sub(r':',u'\xa0: ',text,flags=re.U)
  return text

@register.filter
@stringfilter
def typographie(text):
  text = force_unicode(text)
  text = spaces(text)

  return text



