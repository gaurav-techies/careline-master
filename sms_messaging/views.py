# from django_twilio.decorators import twilio_view
# from twilio.twiml.messaging_response import MessagingResponse

# @twilio_view
# def sms(request):
#     name = request.POST.get('Body', '')
#     msg = 'Hey %s, how are you today?' % (name)
#     r = MessagingResponse()
#     r.message(msg)
#     return r