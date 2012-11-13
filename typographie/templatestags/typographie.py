from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import smart_str, force_unicode

import re
register = template.Library()

spaces_rules = {
    u':' : u'\xa0: ',
    u',' : u', ',
    u'.' : u'. ',
    u'\u2026' : u'\u2026 ',
    u';' : u'\xa0; ',
    u'!' : u'\xa0! ',
    u'?' : u'\xa0? ',
    u'(' : u' (',
    u')' : u') ',
    u'[' : u' [',
    u']' : u'] ',
    u'\xab' : u' \xab\xa0',
    u'\xbb' : u'\xa0\xbb '
    
  }

spaces_rules_chars = u''.join([ u"%s%s" % ( (u'\\' if c in [u'-', u'.', u'(', u')', u'[', u']'] else u''), c ) for c in spaces_rules.keys()])

re_clean_space_1 = re.compile(u'\s*(<[^>]+>|)([%s])(<[^>]+>|)\s*' % spaces_rules_chars, flags=re.U)
re_clean_space_2 = re.compile(u'([%s])\s*(<[^>]+>|)(<[^>]+>|)\s*' % spaces_rules_chars, flags=re.U)
re_clean_space_3 = re.compile(u'\s*(<[^>]+>|)(<[^>]+>|)\s*([%s])' % spaces_rules_chars, flags=re.U)

re_replace_chars_with_spaces = re.compile(u'[%s]' % spaces_rules_chars, flags=re.U)

widont_finder = re.compile(r"""((?:</?(?:a|em|span|strong|i|b)[^>]*>)|[^<>\s]) # must be proceeded by an approved inline opening or closing tag or a nontag/nonspace
                                   \s+                                             # the space to replace
                                   ([^<>\s]+                                       # must be flollowed by non-tag non-space characters
                                   \s*                                             # optional white space! 
                                   (</(a|em|span|strong|i|b)>\s*)*                 # optional closing inline tags with optional white space after each
                                   ((</(p|h[1-6]|li|dt|dd)>)|$))                   # end with a closing p, h1-6, li or the end of the string
                                   """, re.VERBOSE)

def replace_with_spaces(matchobj):
    return spaces_rules.get(matchobj.group(0))

@register.filter
@stringfilter
def spaces(text):
  # clean spaces  
  text = re_clean_space_1.sub(u'\\2\\1\\3',text)
  text = re_clean_space_2.sub(u'\\1\\2\\3',text)
  text = re_clean_space_3.sub(u'\\3\\1\\2',text)
  
  # replace chars with chars + spaces
  text = re_replace_chars_with_spaces.sub(replace_with_spaces ,text)
  
  return text

def widont(text):
    
    text = widont_finder.sub(u'\\1\xa0\\2', text)
    return text


@register.filter
@stringfilter
def ellipsis(text):
  text = re.sub(r"\.\.\.", u"\u2026", text)
  text = re.sub(r"\. \. \.", u"\u2026", text)
  return text


@register.filter
@stringfilter
def typographie(text):
  text = force_unicode(text)
  text = ellipsis(text)
  text = spaces(text)

  return text



