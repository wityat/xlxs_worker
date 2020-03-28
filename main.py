import os
from multiprocessing.dummy import Pool as ThreadPool
import pyexcel
import pyexcel_xlsx
import pyexcel_xls
import time
import requests

import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design

num_row_with_autonumber = 2
threads_count = 20

session = requests.session()
session.get(f"https://stats.mos.ru/handler/handler.js?time={time.time()}")


def was_in_taxi(auto_nomer):
    url = f"https://www.mos.ru/altmosmvc/api/v1/taxi/getInfo/?Region=&RegNum={auto_nomer}&FullName=&LicenseNum=&Condition=&pagenumber=1"
    response = session.get(url, headers=dict(session.cookies))
    try:
        was_in_taxi_ = response.json()["Count"]
    except:
        print("error")
        return (False, False)

    is_actual = False
    for license in response.json()["Infos"]:
        is_actual = True if license["Condition"] == "Действующее" else is_actual
    return bool(was_in_taxi_), bool(is_actual)


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.browse_file.clicked.connect(self.browse_folder)
        self.start.clicked.connect(self.start_)
        self.file_path_ = ""
        self.statusBar.showMessage('Нажмите кнопку "Выбрать файл".')

    def browse_folder(self):
        self.statusBar.showMessage('Выберите файл!')
        self.file_path_ = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")[0]
        self.statusBar.showMessage('Файл выбран. Теперь начните преобразование.')

    def start_(self):
        self.statusBar.showMessage('Начинаю парсинг...')
        file_arr = pyexcel.get_array(file_name=f"{self.file_path_}")

        pool = ThreadPool(threads_count)

        results = pool.map(was_in_taxi, [row[num_row_with_autonumber] for row in file_arr])

        file_arr = [row + list(results[i]) for i, row in enumerate(file_arr)]

        new_file_path = f"{self.file_path_.split('.')[-2]}_new.{self.file_path_.split('.')[-1]}"

        pyexcel.save_as(array=file_arr, dest_file_name=f"{new_file_path}")

        self.statusBar.showMessage(f"Всё готово! Название файла:{new_file_path.split('/')[-1]}")


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
