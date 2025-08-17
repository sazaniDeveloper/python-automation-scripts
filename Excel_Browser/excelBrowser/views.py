from django.shortcuts import render
import pandas as pd

def index(request):
    try:
        if request.method == "POST" and request.FILES:
            excel_file = request.FILES["files"]
            df = pd.read_excel(excel_file)
            pd.set_option('display.max_colwidth', None)  # Do not truncate cell contents
            pd.set_option('display.max_columns', None)
            data_to_display = df.to_html(classes="table table-striped table-bordered")
            return render(request, 'excelBrowser/index.html', {'data_to_display': data_to_display})

        return render(request, 'excelBrowser/index.html')
    except pd.errors.EmptyDataError:
        render("The Excel file is empty or has no columns to parse.")
    except FileNotFoundError:
        render("The Excel file was not found.")
