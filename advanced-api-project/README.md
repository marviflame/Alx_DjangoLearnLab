## API Endpoints

### Books

- `GET /books/`: Retrieve a list of all books.
- `GET /books/<id>/`: Retrieve a single book by ID.
- `POST /books/create/`: Create a new book (authenticated users only).
- `PUT /books/<id>/update/`: Update an existing book (authenticated users only).
- `DELETE /books/<id>/delete/`: Delete a book (authenticated users only).

### Permissions

- Read operations (ListView and DetailView) are open to any user.
- Write operations (CreateView, UpdateView, DeleteView) require authentication.

