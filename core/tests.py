from django.test import TestCase
from django.urls import reverse
from .models import VisitorEntry


class GuestbookViewTests(TestCase):
    def test_guestbook_page_loads(self):
        response = self.client.get(reverse("guestbook"))
        self.assertEqual(response.status_code, 200)

    def test_valid_post_creates_entry(self):
        response = self.client.post("/", {
            "name": "Chance",
            "message": "Testing the guestbook."
        })

        self.assertEqual(VisitorEntry.objects.count(), 1)

        entry = VisitorEntry.objects.first()
        self.assertEqual(entry.name, "Chance")
        self.assertEqual(entry.message, "Testing the guestbook.")

    def test_invalid_post_does_not_create_entry(self):
        response = self.client.post(reverse("guestbook"), {
            "name": "",
            "message": ""
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(VisitorEntry.objects.count(), 0)
        self.assertContains(response, "This field is required.")

    def test_delete_post_removes_entry(self):
        entry = VisitorEntry.objects.create(
            name="Chance",
            message="Delete me."
        )

        response = self.client.post(
            reverse("delete_entry", args=[entry.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(VisitorEntry.objects.count(), 0)