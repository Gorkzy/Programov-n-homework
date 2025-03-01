# import json
# import csv
# from abc import ABC, abstractmethod
# # 1. Abstraktní třída pro práci se soubory
# class FileHandler(ABC):
#     @abstractmethod
#     def read(self, file_path):
#         pass
#     @abstractmethod
#     def write(self, file_path, data):
#         pass
# # 2. Konkrétní třídy pro jednotlivé formáty
# class TxtFileHandler(FileHandler):
#     def read(self, file_path):
#         with open(file_path, 'r', encoding='utf-8') as file:
#             return file.read()
#     def write(self, file_path, data):
#         with open(file_path, 'w', encoding='utf-8') as file:
#             file.write(data)
# class CsvFileHandler(FileHandler):
#     def read(self, file_path):
#         with open(file_path, newline='', encoding='utf-8') as file:
#             return list(csv.reader(file))
#     def write(self, file_path, data):
#         with open(file_path, 'w', newline='', encoding='utf-8') as file:
#             writer = csv.writer(file)
#             writer.writerows(data)
# class JsonFileHandler(FileHandler):
#     def read(self, file_path):
#         with open(file_path, 'r', encoding='utf-8') as file:
#             return json.load(file)
#     def write(self, file_path, data):
#         with open(file_path, 'w', encoding='utf-8') as file:
#             json.dump(data, file, indent=4)
# # 3. Factory třída
# class FileHandlerFactory:
#     @staticmethod
#     def get_handler(file_type):
#         if file_type == "txt":
#             return TxtFileHandler()
#         elif file_type == "csv":
#             return CsvFileHandler()
#         elif file_type == "json":
#             return JsonFileHandler()
#         else:
#             raise ValueError("Unsupported file type")
# # 4. Použití Factory
# def main():
#     file_type = "json"  # Může být "txt", "csv", "json"
#     handler = FileHandlerFactory.get_handler(file_type)
#     # Zápis
#     data = {"name": "Alice", "age": 25}
#     handler.write("example.json", data)
#     # Čtení
#     loaded_data = handler.read("example.json")
#     print("Loaded Data:", loaded_data)
# if __name__ == "__main__":
#     main()

# class Singleton:
#     _instance = None  # single instance
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.value = "init value"
#         return cls._instance
# obj1 = Singleton()
# obj2 = Singleton()
# print(obj1.value)
# obj2.value = "New value"
# print(obj1.value)
# print(obj1 is obj2)
# class OldPrinter:
#     """Old system."""
#     def old_print(self, text):
#         print(f"Starý tisk: {text}")
# class PrinterAdapter:
#     """Adapter to convert old to new"""
#     def __init__(self, old_printer):
#         self.old_printer = old_printer
#     def print(self, text):
#         self.old_printer.old_print(text)
# old_printer = OldPrinter()
# adapter = PrinterAdapter(old_printer)
# adapter.print("Tisknu přes adaptér")


# class OldCurrencySystem:
#     """Starý systém vrací ceny pouze v CZK."""
#     def get_price_czk(self):
#         return 1000  # Například 1000 Kč
# class CurrencyAdapter:
#     """Adaptér převádí CZK na EUR podle aktuálního kurzu."""
#     EXCHANGE_RATE = 0.04  # 1 CZK = 0.04 EUR
#     def __init__(self, old_system):
#         self.old_system = old_system
#     def get_price_eur(self):
#         price_czk = self.old_system.get_price_czk()
#         return round(price_czk * self.EXCHANGE_RATE, 2)  # Převod na EUR
# # Použití Adapteru
# old_system = OldCurrencySystem()
# adapter = CurrencyAdapter(old_system)
# print(f"Cena v CZK: {old_system.get_price_czk()} Kč")
# print(f"Cena v EUR: {adapter.get_price_eur()} €")

# class Model:
#     def __init__(self):
#         # Initialize an empty list to hold tasks.
#         self.tasks = []
#     # Adds a task to the list of tasks.
#     def add_task(self, task):
#         self.tasks.append(task)
#     # Returns the list of tasks.
#     def get_tasks(self):
#         return self.tasks
# # View class responsible for
# # handling user interaction and display.
# class View:
#     # Reads a task from the user.
#     def input_task(self):
#         return input("Input task:\n")
#     # Displays the list of tasks to the user.
#     def show_tasks(self, tasks):
#         for item in tasks:
#             print(item)
#     # Shows the menu and returns the user's choice.
#     def show_menu(self):
#         print("*************************")
#         print("1 - Add task")
#         print("2 - Show tasks")
#         print("3 - Exit")
#         result = int(input("Choose what to do:\n"))
#         print("*************************")
#         return result
#     # Controller class to act
#     # as an intermediary between the Model and View.
# class Controller:
#     # Initialize the Controller with a Model and a View.
#     def __init__(self, model, view):
#         self.model = model
#         self.view = view
#     # Method to handle adding a new task.
#     def action_input_task(self):
#         task = self.view.input_task()
#         self.model.add_task(task)
#     # Method to handle showing the list of tasks.
#     def action_show_tasks(self):
#         tasks = self.model.get_tasks()
#         self.view.show_tasks(tasks)
# # Initialize the MVC components.
# obj_controller = Controller(Model(), View())
# # Main application loop.
# while True:
#     # Display menu and get user choice.
#     result = obj_controller.view.show_menu()
#     # Match user choice to appropriate action.
#     match result:
#         case 1:
#             # Add a new task.
#             obj_controller.action_input_task()
#         case 2:
#             # Show list of tasks.
#             obj_controller.action_show_tasks()
#         case 3:
#             # Exit the application.
#             print("Bye!")
#             break
#         case _:
#             # Handle invalid user input.
#             print("\nWrong choice. Try again!\n")
class Article:
    def __init__(self, title, author, publisher, brief_summary):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.brief_summary = brief_summary
        self.number_of_characters = len(brief_summary)  

    def __str__(self):  
        return f"Název: {self.title}\nAutor: {self.author}\nVydavatel: {self.publisher}\nStručné shrnutí: {self.brief_summary}\nPočet znaků: {self.number_of_characters}"

    def update_summary(self, new_summary):
        self.brief_summary = new_summary
        self.number_of_characters = len(new_summary)

    def get_brief_summary(self):
        return self.brief_summary

    def get_number_of_characters(self):
        return self.number_of_characters
    
class ArticleController:
    def __init__(self):
        self.articles = []

    def create_article(self, title, author, publisher, brief_summary):
        article = Article(title, author, publisher, brief_summary)
        self.articles.append(article)
        return article

    def get_article(self, title):
        for article in self.articles:
            if article.title == title:
                return article
        return None

    def update_article_summary(self, title, new_summary):
        article = self.get_article(title)
        if article:
            article.update_summary(new_summary)

    def list_articles(self):
        return self.articles
 
class ArticleView:
    def display_article(self, article):
        if article:
            print(article)
        else:
            print("Článek nenalezen.")

    def display_articles(self, articles):
        for article in articles:
            self.display_article(article)

    def get_user_input(self, prompt):
        return input(prompt)
    
controller = ArticleController()
view = ArticleView()

# Vytvoření článku
article = controller.create_article("Můj článek", "Jan Novák", "MujWeb.cz", "Stručný popis článku.")

# Zobrazení článku
view.display_article(article)

# Aktualizace shrnutí
new_summary = "Zcela nový a vylepšený popis článku."
controller.update_article_summary("Můj článek", new_summary)

# Zobrazení aktualizovaného článku
view.display_article(article)

# Výpis všech článků
articles = controller.list_articles()
view.display_articles(articles)
