import PyPDF2
import re
import pandas as pd


def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error extracting text from PDF : {str(e)}")
        return None


def find_pattern_in_text(text, pattern):
    try:
        matches = re.findall(pattern, text)
        return matches
    except Exception as e:
        print(f"Error applying regex pattern : {str(e)}")
        return None


def create_dataframe(matches):
    try:
        df = pd.DataFrame(matches, columns=['Found_Pattern'])
        return df
    except Exception as e:
        print(f'Error creating DataFrame : {str(e)}')
        return None


pdf_path = 'D:\pythonProject\pythonProject\PdF_parser_with_regex\pdf_parser\media\DonetcStanislav.pdf'

search_pattern = '\\bhttps?://\S+\\b'

pdf_text = extract_text_from_pdf(pdf_path)


if pdf_text:
    found_matches = find_pattern_in_text(pdf_text, search_pattern)
    if found_matches:
        result_df = create_dataframe(found_matches)
        if result_df is not None:
            print(result_df)
