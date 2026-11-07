from django.test import TestCase, Client
from django.urls import reverse


class CoursePortalTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        """Verify homepage renders with correct template, status, and metrics."""
        response = self.client.get(reverse('catalog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/home.html')
        self.assertIn('total_courses', response.context)
        self.assertIn('featured_course', response.context)
        self.assertEqual(response.context['total_courses'], 3)
        self.assertContains(response, "Welcome to DTI CoursePortal")
        self.assertContains(response, "Active Courses Offered")

    def test_course_list_view_default(self):
        """Verify course listing renders all 3 courses."""
        response = self.client.get(reverse('catalog:course_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/course_list.html')
        self.assertEqual(len(response.context['courses']), 3)
        self.assertContains(response, "DTI412")
        self.assertContains(response, "DTI201")
        self.assertContains(response, "DTI305")

    def test_course_list_search_filter_code(self):
        """Verify Extension Challenge: filtering courses by course code."""
        response = self.client.get(reverse('catalog:course_list') + '?q=DTI412')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['courses']), 1)
        self.assertEqual(response.context['courses'][0]['code'], 'DTI412')
        self.assertContains(response, "Special Topic in Application Development")

    def test_course_list_search_filter_title(self):
        """Verify Extension Challenge: filtering courses by course title keyword."""
        response = self.client.get(reverse('catalog:course_list') + '?q=react')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['courses']), 1)
        self.assertEqual(response.context['courses'][0]['code'], 'DTI305')

    def test_course_list_search_empty_result(self):
        """Verify Extension Challenge: search with no matching results."""
        response = self.client.get(reverse('catalog:course_list') + '?q=UnknownCourse')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['courses']), 0)
        self.assertContains(response, "No courses found matching")

    def test_course_detail_success(self):
        """Verify syllabus detail view for an existing course."""
        response = self.client.get(reverse('catalog:course_detail', args=[101]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/course_detail.html')
        self.assertContains(response, "DTI412")
        self.assertContains(response, "Dr. Sirisuda Buathongkeow")
        self.assertContains(response, "Special Topic in Application Development")

    def test_course_detail_404(self):
        """Verify HTTP 404 is raised when an invalid course_id is requested."""
        response = self.client.get(reverse('catalog:course_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_inquiry_get(self):
        """Verify GET request renders inquiry form correctly."""
        response = self.client.get(reverse('catalog:inquiry'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/inquiry.html')
        self.assertContains(response, "Course Inquiry Form")
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_inquiry_post_validation_error(self):
        """Verify form validation errors when required fields are missing or invalid."""
        response = self.client.post(reverse('catalog:inquiry'), {
            'student_name': '',
            'email': 'invalid-email',
            'course_code': 'DTI412',
            'message': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Student Name is required.', response.context['errors'])
        self.assertIn('A valid Email address is required.', response.context['errors'])
        self.assertIn('Inquiry message cannot be empty.', response.context['errors'])
        self.assertContains(response, "Form Submission Errors")

    def test_inquiry_post_success(self):
        """Verify successful form submission with valid input."""
        response = self.client.post(reverse('catalog:inquiry'), {
            'student_name': 'Jane Doe',
            'email': 'jane.doe@example.com',
            'course_code': 'DTI412',
            'message': 'Can I register for this course as an elective?',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['errors']), 0)
        self.assertIsNotNone(response.context['submitted_data'])
        self.assertEqual(response.context['submitted_data']['student_name'], 'Jane Doe')
        self.assertContains(response, "Inquiry Processed Successfully!")
        self.assertContains(response, "Thank you, <strong>Jane Doe</strong>")
