
1. Проверка, что метод правильно определяет жанр книги  def test_set_book_genre(self):
2. Проверка, что метод возвращает книгу, у которой нет жанра  def test_get_book_genre_no_genre(self):
3. Проверка, что метод возвращает книги определенного жанра  def test_get_books_with_specific_genre_existing_genre(self):
4. Проверка, что метод возвращает пустой список, если в коллекции нет книг заданного жанра def test_get_books_with_specific_genre_no_genre(self
5. Проверка, что метод возвращает пустой словарь, если в коллекции нет ни одной книги с указанием жанра 
def test_get_books_genre_empty(self):
6. Проверка, что метод возвращает словарь с жанрами книг, если в коллекции есть книги уазанного жанра
def test_get_books_genre_nonempty(self):
7. Проверка, что метод возвращает пустой список, если в коллекции нет книг для детей  def test_get_books_for_children_empty(self):
8. Проверка, что книги с возрастным рейтингом отсутствуют в списке книг для детей 
def test_get_books_for_children_no_age_rating_books(self):
9. Проверка, что метод возвращает список книг для детей, если они есть в коллекции def test_get_books_for_children_nonempty(self):
10. Проверка добавления книги в избранное     def test_add_book_in_favorites_add_existing_book(self):
11. Проверка удаления книги из избранного     def test_delete_book_from_favorites_existing_book(self):
12. Проверка, что метод  возвращает список избранных книг, в который добавлена та или иная книга 
def test_get_list_of_favorites_books_existing_books(self):
       
