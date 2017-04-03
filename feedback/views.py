from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils import timezone

from akutepov_blog import settings
from feedback.forms import FeedbackForm
from feedback.models import Feedback


def feedback(request):
    """
    Handle feedback
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            if 'subject' in form.cleaned_data and form.cleaned_data['subject']:
                return JsonResponse({"result": "error"})
            if 'email' in form.cleaned_data:
                email = form.cleaned_data['email']
            else:
                email = None
            if 'message' in form.cleaned_data:
                message = form.cleaned_data['message']
            else:
                message = None
            if email == "" and message == "":
                return JsonResponse({"result": "error"})
            Feedback.objects.create(
                email=email,
                message=message,
                datetime=timezone.now()
            )
            try:
                send_mail(
                    "Новое сообщение",
                    'e-mail: ' + email + '\n \nСообщение: ' + message,
                    getattr(settings, "EMAIL_HOST_USER", None),
                    [settings.EMAIL_ADDRESS, ],
                    fail_silently=False,
                )
            except:
                pass
            return JsonResponse({"result": "ok"})
        else:
            return JsonResponse({"result": "error"})
