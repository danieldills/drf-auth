from django.test import TestCase

# for some reason, we have to use get_user_model and not settings.AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from .models import Concert


class ConcertTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(email="test@gmail.com", password="pass")
        testuser1.save()
        test_example = Concert.objects.create(
            author=testuser1, title="Green Eggs and Ham", body="I do not like green eggs and ham, Sam I  am."
        )
        test_example.save()

    def test_blog_content(self):
        example = Concert.objects.get(id=1)
        self.assertEqual(str(example.author), "test@gmail.com")
        self.assertEqual(str(example.title), "Green Eggs and Ham")
        self.assertEqual(str(example.body), "I do not like green eggs and ham, Sam I  am.")
