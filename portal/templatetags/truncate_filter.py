from django import template

from portal.models import Categories, Tutorial, Blogrol

register = template.Library()

@register.filter("truncate_chars")
def truncate_chars(value, max_length):
    if len(value) <= max_length:
        return value
 
    truncd_val = value[:max_length]
    if value[max_length] != " ":
        rightmost_space = truncd_val.rfind(" ")
        if rightmost_space != -1:
            truncd_val = truncd_val[:rightmost_space]
 
    return truncd_val + "..."


@register.inclusion_tag('categories.html')
def categories(category):
	cat = Categories.objects.all()
	return {'category': cat}


@register.inclusion_tag('new.html')
def new(tutor):
	new = Tutorial.objects.all().order_by('-id')[:5]
	return {'new': new}


@register.inclusion_tag('blogrol.html')
def blogrol(web):
	blog = Blogrol.objects.all()
	return {'blog': blog}
