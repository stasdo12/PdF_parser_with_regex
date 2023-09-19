import tabula
import pandas as pd


class PDFProcessor:
    def __init__(self, pdf_file_path):
        self.pdf_file_path = pdf_file_path

    def extract_data(self):
        tables = tabula.read_pdf(self.pdf_file_path, pages='all')
        if tables:
            return tables[0]
        else:
            return None

    def create_dataframe(self, data):
        if data is not None:
            return pd.DataFrame(data)
        else:
            return None

    def sort_dataframe(self, df, column_name):
        if df is not None:
            return df.sort_values(by=column_name)
        else:
            return None


if __name__ == "__main__":
    pdf_file_path = 'D:\pythonProject\pythonProject\PdF_parser_with_regex\pdf_parser\create_pdf\workers_table.pdf'

    processor = PDFProcessor(pdf_file_path)

    extracted_data = processor.extract_data()
    if extracted_data is not None:
        df = processor.create_dataframe(extracted_data)

        if df is not None:
            print("Tail:")
            print(df.tail().to_csv("Tail.csv"))
            print("Head:")
            print(df.head().to_csv("Head.csv"))
            print("Sorted by Name:")
            print(processor.sort_dataframe(df, "Name").to_csv("By_name.csv"))
            print("Sorted by Salary:")
            print(processor.sort_dataframe(df, "Salary").to_json("By_salary.json"))
            print("Sorted by Date:")
            print(processor.sort_dataframe(df, "Date").to_json("By_Date.json"))


