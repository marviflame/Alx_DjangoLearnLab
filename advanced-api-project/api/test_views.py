from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITests(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create an author
        self.author = Author.objects.create(name="John Doe")

        # Create a book
        self.book = Book.objects.create(title="Sample Book", publication_year=2023, author=self.author)

    def test_create_book(self):
        """Test creating a new book"""
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-create')
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, "New Book")

    def test_get_book_list(self):
        """Test retrieving a list of books"""
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_book_detail(self):
        """Test retrieving a single book by ID"""
        url = reverse('book-detail', kwargs={'pk': self.book.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        """Test updating a book"""
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-update', kwargs={'pk': self.book.id})
        data = {
            "title": "Updated Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(id=self.book.id).title, "Updated Book")

    def test_delete_book(self):
        """Test deleting a book"""
        self.client.login(username='testuser', password='testpassword')
        url = reverse('book-delete', kwargs={'pk': self.book.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_permissions(self):
        """Test that unauthenticated users cannot create, update, or delete books"""
        create_url = reverse('book-create')
        update_url = reverse('book-update', kwargs={'pk': self.book.id})
        delete_url = reverse('book-delete', kwargs={'pk': self.book.id})

        # Unauthenticated create attempt
        response = self.client.post(create_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Unauthenticated update attempt
        response = self.client.put(update_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        # Unauthenticated delete attempt
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

