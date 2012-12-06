#!/usr/bin/env python

class Form:
  def __init__(self, name, action, target='', method=''):
    if target == '' and method == '':
      print '<form name="'+name+'" action="'+action+'">'
    if target == '' and method != '':
      print '<form name="'+name+'" action="'+action+'" method="'+method+'">'
    if target != '' and method == '':
      print '<form name="'+name+'" action="'+action+'" target="'+target+'">'
    if target != '' and method != '':
      print '<form name="'+name+'" action="'+action+'" method="'+method+'" target="'+target+'">'

  def text_field(title,name):
    print title
    print '<br/>'
    print '<input name="'+name+'"/>'
    print '<br/>'

  def drop_down(title,name,elements,size=''):
    print title
    print '<br/>'

    if size == '':
      print '<select name="'+name+'">'
    if size != '':
      print '<select name="'+name+'" multiple="multiple" size="'+size'">'
    
    for e in elements:
      print '<option value="'+str(e[0])+'">'+e[1]+'</option>'

    print '</select>'

  def button(title,name):
    print '<button name="'+name+'" type="submit">'+title+'</button>'

  def close:
    print '</form>'
