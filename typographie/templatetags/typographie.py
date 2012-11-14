from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import smart_str, force_unicode
from smartypants import smartyPants

import re
from django.utils.safestring import mark_safe
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
    u'\xbb' : u'\xa0\xbb ',
    u"\u2019" : u"\u2019" 
    
  }


spaces_rules_chars = u''.join([ u"%s%s" % ( (u'\\' if c in [u'-', u'.', u'(', u')', u'[', u']'] else u''), c ) for c in spaces_rules.keys()])

re_clean_space_1 = re.compile(u'\s*(<[^>]+>|)([%s])(<[^>]+>|)\s*' % spaces_rules_chars, flags=re.U)
re_clean_space_2 = re.compile(u'([%s])\s*(<[^>]+>|)(<[^>]+>|)\s*' % spaces_rules_chars, flags=re.U)
re_clean_space_3 = re.compile(u'\s*(<[^>]+>|)(<[^>]+>|)\s*([%s])' % spaces_rules_chars, flags=re.U)

re_replace_chars_with_spaces = re.compile(u'\s*[%s]\s*' % spaces_rules_chars, flags=re.U)

widont_finder = re.compile(r"""((?:</?(?:a|em|span|strong|i|b)[^>]*>)|[^<>\s]) # must be proceeded by an approved inline opening or closing tag or a nontag/nonspace
                                   \s+                                             # the space to replace
                                   ([^<>\s]+                                       # must be flollowed by non-tag non-space characters
                                   \s*                                             # optional white space! 
                                   (</(a|em|span|strong|i|b)>\s*)*                 # optional closing inline tags with optional white space after each
                                   ((</(p|h[1-6]|li|dt|dd)>)|$))                   # end with a closing p, h1-6, li or the end of the string
                                   """, re.VERBOSE)

def replace_with_spaces(matchobj):
    return spaces_rules.get(matchobj.group(0))

def replace_content(matchobj):
    text = spaces(matchobj.group(4).strip())
    
    ## clean spaces  
    #text = re_clean_space_1.sub(u'\\2\\1\\3',text)
    #text = re_clean_space_2.sub(u'\\1\\2\\3',text)
    #text = re_clean_space_3.sub(u'\\3\\1\\2',text)
    
    return u"%s%s%s%s%s" % (matchobj.group(1), matchobj.group(2),matchobj.group(3), text,matchobj.group(5))
    
re_parse_content = re.compile(r'(<[^>]* ?)((?:div|p|pre|blockquote))( ?[^>]*>)(.*?)(</\2>)', flags = re.S + re.U)

def spaces(text):
    
  if re_parse_content.match(text) is not None:
      text = re_parse_content.sub(replace_content, text)
  else:
    
      # clean spaces  
      text = re_clean_space_1.sub(u'\\2\\1\\3',text)
      text = re_clean_space_2.sub(u'\\1\\2\\3',text)
      text = re_clean_space_3.sub(u'\\3\\1\\2',text)
      
      # replace chars with chars + spaces
      text = re_replace_chars_with_spaces.sub(replace_with_spaces ,text)
      
      def test(m):
          r = " "
          if m.group(3) == u'\xa0':
              r = u'\xa0'
              
          return u"%s%s%s" % (m.group(1), r, m.group(5))
      
      text = re.compile(r'([%s])(\s*)(\xa0*)(\s*)([%s])' % (spaces_rules_chars, spaces_rules_chars), flags=re.U).sub(test,text)
      text = re.compile(r'(\S)\s*([\.,])' ).sub(u'\\1\\2',text)
      
  return text


def widont(text):
    
    text = widont_finder.sub(u'\\1\xa0\\2', text)
    return text

def ellipsis(text):
  text = re.sub(r"\.\.\.", u"\u2026", text)
  text = re.sub(r"\. \. \.", u"\u2026", text)
  return text


@register.filter
@stringfilter
def typographie(text):
  
  text = force_unicode(text)
  text = smartyPants(text)
  text = ellipsis(text)
  text = spaces(text)
  text = widont(text)
  return mark_safe(text)

typographie.is_safe = True

