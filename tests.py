import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
        # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    @pytest.fixture
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize("name, genre", [
        ("Гарри Поттер", "Фантастика"),
        ("Маленький принц", "Детективы"),
        ("Дом на холме", "Ужасы"),
        ("Незнайка на луне", "Мультфильмы"),
    ])
    def test_set_book_genre(collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_book_genre_no_genre(collector):
        book_name = "Гарри и Питер"
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) is None


    def test_get_books_with_specific_genre_existing_genre(collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.add_new_book("Дом на холме")
        collector.set_book_genre("Дом на холме", "Ужасы")
        collector.add_new_book("Незнайка на луне")
        collector.set_book_genre("Незнайка на луне", "Мультфильмы")
        fantasy_books = collector.get_books_with_specific_genre("Фантастика")
        assert fantasy_books == ["Гарри Поттер"]

    def test_get_books_with_specific_genre_no_genre(collector):
        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")
        collector.add_new_book("Дом на холме")
        collector.set_book_genre("Дом на холме", "Ужасы")
        collector.add_new_book("Незнайка на луне")
        collector.set_book_genre("Незнайка на луне", "Мультфильмы")
        horror_books = collector.get_books_with_specific_genre("Ужасы")
        assert horror_books == []

    def test_get_books_genre_empty(collector):
        books_genre = collector.get_books_genre()
        assert books_genre == {}

    def test_get_books_genre_nonempty(collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        books_genre = collector.get_books_genre()
        assert books_genre == {'Гарри Поттер': 'Фантастика'}

    def test_get_books_for_children_empty(collector):
        children_books = collector.get_books_for_children()
        assert children_books == []

    @pytest.mark.parametrize("book_name, genre", [
        ("Маленький принц", "Детективы"),
        ("Гарри Поттер", "Фантастика"),
        ("Дом на холме", "Ужасы"),
        ("Незнайка на луне", "Мультфильмы")
    ])
    def test_get_books_for_children_no_age_rating_books(collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        children_books = collector.get_books_for_children()
        assert book_name not in children_books

    def test_get_books_for_children_nonempty(collector):
        collector.add_new_book("Маленький принц")
        collector.set_book_genre("Маленький принц", "Детективы")

        collector.add_new_book("Гарри Поттер")
        collector.set_book_genre("Гарри Поттер", "Фантастика")

        collector.add_new_book("Дом на холме")
        collector.set_book_genre("Дом на холме", "Ужасы")

        collector.add_new_book("Незнайка на луне")
        collector.set_book_genre("Незнайка на луне", "Мультфильмы")

        children_books = collector.get_books_for_children()
        assert children_books != []
        for book in children_books:
            assert collector.get_book_genre(book) not in collector.genre_age_rating

    def test_add_book_in_favorites_add_existing_book(collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert collector.get_list_of_favorites_books() == ["Гарри Поттер"]

    def test_delete_book_from_favorites_existing_book(collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        collector.delete_book_from_favorites("Гарри Поттер")
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_existing_books(collector):
        collector.add_new_book("Гарри Поттер")
        collector.add_book_in_favorites("Гарри Поттер")
        assert collector.get_list_of_favorites_books() == ["Гарри Поттер"]









