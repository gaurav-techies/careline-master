from taskapp.celery import app
from scarface.models import Device, PushMessage
from scarface.exceptions import NotRegisteredException


@app.task
def send_push(msg):
    # get max number
    max_id = PushMessage.objects.all()
    if max_id:
        max_id = max_id.order_by('-id')[0].id
    else:
        max_id = 1
    now_id = max_id + 1
    message = PushMessage(
        id=now_id,
        badge_count=1,
        context='url_alert',
        has_new_content=True,
        message=msg
    )

    for each in Device.objects.all():
        try:
            each.send(message)
        except NotRegisteredException as f:
            pass
        except:
            pass