# Create Operation:

### __Instruction__ Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949

``````from bookshelf.models import Book``````

command:

```py
Book.objects.create(title="The gods are not to blame", author="Ola Rotimi",publication_year=2005)
```

output:
<Book: Book object (4)>