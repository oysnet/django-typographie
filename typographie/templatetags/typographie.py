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

re_percent = re.compile(u'([0-9])\s*(%)', flags=re.U)

# return char + spaces accoring to cb_re_replace_chars_with_spaces
re_replace_chars_with_spaces = re.compile(u'\s*([%s])\s*' % spaces_rules_chars, flags=re.U)
def cb_re_replace_chars_with_spaces(matchobj):
    return spaces_rules.get(matchobj.group(1))


# extract content between two tags
re_content_between_tags = re.compile(r'(>|^)([^<>]*)(<|$)')
def cb_re_content_between_tags(matchobj):
      text = matchobj.group(2)
      text = re_replace_chars_with_spaces.sub(cb_re_replace_chars_with_spaces ,text)
      
      # replace any white space between an integer and % and replace it with \xa0
      text = re_percent.sub(u'\\1\xa0\\2',text)
      
      # remove multiple spaces      
      text = re_remove_multiple_spaces.sub(cb_re_remove_multiple_spaces,text)
      text = re_remove_spaces_before_comma_and_dot.sub(u'\\1\\2',text)
      
      # remove space between ellipsis and close parenthesis 
      text = re_remove_space_between_ellipsis_and_parenthesis.sub(u'\u2026)' ,text)
      
      return u"%s%s%s" % (matchobj.group(1), text, matchobj.group(3))
  
# extract html between tags div, p, pre, blockquote 
re_parse_content = re.compile(r'(.*?<[^>]* ?)((?:div|p|pre|blockquote|h4))( ?[^>]*>)(.*?)(</\2>.*?)', flags = re.S + re.U)
def cb_re_parse_content(matchobj):
    
    text = spaces(matchobj.group(4))
    return u"%s%s%s%s%s" % (matchobj.group(1), matchobj.group(2),matchobj.group(3), text,matchobj.group(5))

# remove spaces
re_remove_spaces_before_comma_and_dot = re.compile(r'(\S)\s*([\.,])')
re_remove_multiple_spaces = re.compile(r'([%s])(\s*)(\xa0*)(\s*)([%s])' % (spaces_rules_chars, spaces_rules_chars), flags=re.U)
def cb_re_remove_multiple_spaces(m):
          r = " "
          if m.group(3) == u'\xa0':
              r = u'\xa0'
              
          return u"%s%s%s" % (m.group(1), r, m.group(5))
re_remove_space_between_ellipsis_and_parenthesis = re.compile(u'\u2026\s*\)',flags=re.U)
      
def spaces(text):
  text = text.strip()
  if re_parse_content.match(text) is not None:
      text = re_parse_content.sub(cb_re_parse_content, text)
  else:
    
      # clean spaces  
      text = re_clean_space_1.sub(u'\\2\\1\\3',text)
      text = re_clean_space_2.sub(u'\\1\\2\\3',text)
      text = re_clean_space_3.sub(u'\\3\\1\\2',text)
      
      # set spaces
      text = re_content_between_tags.sub(cb_re_content_between_tags, text)
      
      
      
  return text


widont_finder = re.compile(r"""((?:</?(?:a|em|span|strong|i|b)[^>]*>)|[^<>\s]) # must be proceeded by an approved inline opening or closing tag or a nontag/nonspace
                                   \s+                                             # the space to replace
                                   ([^<>\s]+                                       # must be flollowed by non-tag non-space characters
                                   \s*                                             # optional white space! 
                                   (</(a|em|span|strong|i|b)>\s*)*                 # optional closing inline tags with optional white space after each
                                   ((</(p|h[1-6]|li|dt|dd)>)|$))                   # end with a closing p, h1-6, li or the end of the string
                                   """, re.VERBOSE)


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

