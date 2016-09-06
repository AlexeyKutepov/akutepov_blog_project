from django.http import JsonResponse
from subscribe.forms import SubscribeForm
from subscribe.models import Subscriber


def subscribe_add(request):
    """
    Add new subscriber
    :param request: request
    :return: json
    """
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email_list = Subscriber.objects.filter(email=form.cleaned_data['email'])
            if len(email_list) == 0:
                Subscriber.objects.create(
                    email=form.cleaned_data['email']
                )
            return JsonResponse({"result": "ok"})
        else:
            return JsonResponse({"result": "error"})