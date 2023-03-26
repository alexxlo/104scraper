import xlsxwriter
from search import main_scraper


def writer_xlsx(function_name):

    book = xlsxwriter.Workbook("direct path")
    page = book.add_worksheet("vacancies")
    page.write("A1", "name")
    page.write("B1", "date")
    page.write("C1", "employer")
    page.write("D1", "location")
    page.write("E1", "experience")
    page.write("F1", "applicants" )
    page.write("G1", "details")
    page.write("H1", "weblink")

    row = 1
    column = 0

    page.set_column("A:A", 20)  
    page.set_column("B:B", 20)  
    page.set_column("C:C", 20)  
    page.set_column("D:D", 20)  
    page.set_column("E:E", 20)  
    page.set_column("F:F", 20)  
    page.set_column("G:G", 20)  
    page.set_column("H:H", 20)  


    for item in function_name(): 
     
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])
        page.write(row, column+5, item[5])
        page.write(row, column+6, item[6])
        page.write(row, column+7, item[7])
        row += 1  

    book.close()

writer_xlsx(main_scraper)
