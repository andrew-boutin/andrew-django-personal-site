"""Custom site views for error handling."""
from django.template import RequestContext
from django.shortcuts import render_to_response


def bad_request(request, exception):
   """Suspicious operations."""
   context = {'exception': exception}
   response = render_to_response('400.html', context, context_instance=RequestContext(request)) 
   response.status_code = 400
   return response


def permission_denied(request, exception):
    """Forbidden actions."""
    context = {'exception': exception}
    response = render_to_response('403.html', context, context_instance=RequestContext(request))
    response.status_code = 403
    return response


def page_not_found(request, exception):
    """Invalid URLs."""
    context = {'exception': exception}
    response = render_to_response('404.html', context, context_instance=RequestContext(request))
    response.status_code = 404
    return response


def error(request):
    """Server errors."""
    response = render_to_response('500.html', {}, context_instance=RequestContext(request))
    response.status_code = 500
    return response

