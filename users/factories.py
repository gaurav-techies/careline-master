import factory
from .models import User, Tracking
from carelineapp.models import Topic


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = "John"
    last_name = "Doe"
    organisation = "Test"
    postcode = "2000"
    mobile = 232424242


class TrackingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tracking

    user = factory.SubFactory(UserFactory)
    application_name = "CarelineMobile"
    brand = "Apple"
    build_number = "8"
    bundle_id = "com.ccareline.app"
    carrier = "Telstra"
    device_country = "AU"
    device_id = "iPhone103"
    device_locale = "en-AU"
    device_name = "iphonex3"
    font_scale = 0.8199999928474426
    free_disk_storage = 198179553280
    manufacturer = "Apple"
    model = "iPhone X"
    readable_version = "1.0.7.8"
    system_name = "iOS"
    system_version = "12.1"
    timezone = "Australia/Melbourne"
    total_disk_capacity = 255937040384
    total_memory = 2960130048
    unique_id = "B462E0BA-1577-42E7-906A-906A"
    useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Mobile/16B92"
    version = "1.0.7"
    twenty_four_hour = True
    emulator = False
    tablet = False
    latitude = ""
    longitude = ""


class TopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Topic

    topic_id = 1
    title = "Test Title"
    introduction = "Test Introduction"
    custom_url = "http://www.xcover.com"