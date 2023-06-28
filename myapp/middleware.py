# from django.contrib.sessions.models import Session

# class VisitorCountMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Process the request
#         response = self.get_response(request)

#         # Increment the visitor count
#         if not request.session.session_key:
#             request.session.save()
#         visitor_count = Session.objects.count()

#         # Store the visitor count in the session
#         request.session['visitor_count'] = visitor_count

#         return response
