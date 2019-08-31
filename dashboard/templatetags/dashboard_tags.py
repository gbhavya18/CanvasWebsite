from django import template

register = template.Library()


@register.filter(name='split')
def split(value):
	name,domain=value.split('@')
	if domain=='professor.ub.com':
		return True
	else:
		return False