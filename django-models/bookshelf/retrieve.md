# Retrieve Operation

### __Instruction__ Retrieve and display all attributes of the book you just created.
```from bookshelf.models import Book```

Command:

```py
Book.objects.get(title="1984")
```
output:
```sh
<Book: Book object (4)>
```