from django import template

register = template.Library()


@register.simple_tag 
def any_function(usuario, grupo, *args, **kwargs): 
      
      if usuario.is_superuser:
            return True
      return grupo in (g.name for g in usuario.groups.all())


