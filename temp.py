import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QComboBox, QLineEdit, QGridLayout, QTableWidget, QTableWidgetItem, QHBoxLayout


class LibraryCatalog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Каталог библиотеки")
        self.setGeometry(100, 100, 400, 300)

        # Главный виджет и компоновка
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QGridLayout()

        # Поле выбора параметра поиска
        self.combo_box = QComboBox()
        self.combo_box.addItems(["Название", "Автор", "Год"])
        layout.addWidget(self.combo_box, 0, 0)

        # Поле для ввода текста поиска
        self.search_input = QLineEdit()
        layout.addWidget(self.search_input, 0, 1)

        # Кнопка поиска
        search_button = QPushButton("Искать")
        layout.addWidget(search_button, 0, 2)
        search_button.clicked.connect(self.display_results)

        # Таблица для отображения результатов
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(1)  # Один столбец для кнопок
        self.table_widget.setHorizontalHeaderLabels(["Результаты"])
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.verticalHeader().setVisible(False)
        self.table_widget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table_widget.setSelectionMode(QTableWidget.NoSelection)
        layout.addWidget(self.table_widget, 1, 0, 1, 3)

        main_widget.setLayout(layout)

    def display_results(self):
        # Пример данных для отображения
        sample_results = ["Трое с площади Карронад", "Чоки-чок, или Рыцарь Прозрачного Кота"]

        # Установка количества строк
        self.table_widget.setRowCount(len(sample_results))

        # Добавление данных в таблицу
        for row, title in enumerate(sample_results):
            button = QPushButton(title)
            button.clicked.connect(lambda checked, t=title: self.on_result_clicked(t))

            # Вставляем кнопку в таблицу
            self.table_widget.setCellWidget(row, 0, button)

    def on_result_clicked(self, title):
        print(f"Книга выбрана: {title}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LibraryCatalog()
    window.show()
    sys.exit(app.exec())
