import xlsxwriter
from _104_main import main_scraper


def writer_xlsx(function_name):

    book = xlsxwriter.Workbook("/Users/titi/PycharmProjects/scraped_data.xlsx")
    page = book.add_worksheet("ВАКАНСИИ")
    page.write("A1", "Название вакансии")
    page.write("B1", "Дата публикации")
    page.write("C1", "Название компании")
    page.write("D1", "Местонахождение")
    page.write("E1", "Требуемый опыт")
    page.write("F1", "Сколько народу рассматривает" )
    page.write("G1", "Подробности")
    page.write("H1", "Ссылка")

    row = 1
    column = 0

    page.set_column("A:A", 20)  # дата публикации
    page.set_column("B:B", 20)  # название вакансии
    page.set_column("C:C", 20)  # название компании
    page.set_column("D:D", 20)  # местонахождение
    page.set_column("E:E", 20)  # количество сотрудников
    page.set_column("F:F", 20)  # требуемый опыт
    page.set_column("G:G", 20)  # зарплата
    page.set_column("H:H", 20)  # сколько народу рассматривает


    for item in function_name(): # имя вызывающейся функции
        # запись в ячейку
        page.write(row, column, item[0]) # первый элемент списка - название вакансии
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])
        page.write(row, column+5, item[5])
        page.write(row, column+6, item[6])
        page.write(row, column+7, item[7])
        row += 1  # конец записи информации по одной вакансии

    book.close()

writer_xlsx(main_scraper)