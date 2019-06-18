from rest_framework.test import APIClient, APITestCase
from leads.models import LeadDB
from ..factories import UserFactory, TrackingFactory, TopicFactory


class CareAPITestCases(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.base_api = '/careapi/v2'

    def test_api_signup_fails_nojwt(self):
        response = self.client.post('{}/users/'.format(self.base_api,))
        self.assertEqual(response.status_code, 401)

    def test_api_sign_jwt(self):
        user = UserFactory()
        self.client.force_authenticate(user=user)

        response = self.client.get('{}/users/details/'.format(self.base_api, ))
        data = response.data
        self.assertEqual(data['first_name'], user.first_name)
        self.assertEqual(data['last_name'], user.last_name)
        self.assertEqual(data['mobile'], user.mobile)
        self.assertEqual(data['organisation'], user.organisation)
        self.assertEqual(data['push'], False)

    def test_api_push_true(self):
        user = UserFactory()
        tracking = TrackingFactory(user=user)
        tracking.push = True
        tracking.save()

        self.client.force_authenticate(user=user)

        response = self.client.get('{}/users/details/'.format(self.base_api, ))
        data = response.data
        self.assertEqual(data['first_name'], user.first_name)
        self.assertEqual(data['last_name'], user.last_name)
        self.assertEqual(data['mobile'], user.mobile)
        self.assertEqual(data['organisation'], user.organisation)
        self.assertEqual(data['push'], True)

    def test_create_referrer(self):
        user = UserFactory()
        TopicFactory()

        self.client.force_authenticate(user=user)

        payload = {
            "recipient_contact_name" : "Test",
            "recipient_contact_number" : "0424807835",
            "callback_permission" : True,
            "recipient_permission" : True,
            "careline_topic": 1,
            "referral_text_message_reason" : "Some Reason",
            "date_time_referral" : "2018-09-15T15:53:00+10:00"
        }
        response = self.client.post('{}/leads/create/'.format(self.base_api, ), data=payload)
        self.assertEqual(response.status_code, 201)

        lead = LeadDB.objects.get(recipient_contact_name='Test')
        self.assertIsNotNone(lead.pk)
        self.assertEqual(lead.user, user)
