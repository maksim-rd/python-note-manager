from PySide6.QtWidgets import QMainWindow, QVBoxLayout, \
QWidget, QPushButton, QTextEdit, QListWidget

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Хранение заметок")
        self.setGeometry(100, 100, 400, 300)

        self.setMinimumWidth(300)
        self.setMinimumHeight(300)

        # Основной виджет
        self.root = QWidget()
        self.setCentralWidget(self.root)
        self.layout = QVBoxLayout(self.root)

        # Ввод текста заметок
        self.note_input = QTextEdit()
        self.layout.addWidget(self.note_input)

        # Кпопка добавления заметок
        self.add_button = QPushButton("Добавить заметку")
        self.add_button.clicked.connect(self.add_note)
        self.layout.addWidget(self.add_button)

        # Список для отображения заметок
        self.notes_list = QListWidget()
        self.layout.addWidget(self.notes_list)

        # Кнопка для удаления заметки
        self.delete_button = QPushButton("Удалить выбранную заметку")
        self.delete_button.clicked.connect(self.delete_note)
        self.layout.addWidget(self.delete_button)

        # Список для заметок
        self.notes = []


    def add_note(self):
        note_text = self.note_input.toPlainText().strip()
        if note_text:
            self.notes.append(note_text)
            self.notes_list.addItem(note_text)
            self.note_input.clear()


    def delete_note(self):
        selected_item = self.notes_list.currentRow()
        if selected_item >= 0:
            self.notes_list.takeItem(selected_item)
            self.notes.pop(selected_item)
