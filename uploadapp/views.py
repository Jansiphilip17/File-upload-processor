import os
import pdfplumber
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage

@csrf_exempt
def upload_pdf(request):
    if request.method == "POST":
        file = request.FILES['file']

        # Save file temporarily
        file_path = default_storage.save(file.name, file)

        # Extract PDF text
        extracted_text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                extracted_text += page.extract_text() + "\n"

        return JsonResponse({"filename": file.name, "text": extracted_text})

    return JsonResponse({"error": "Invalid request"}, status=400)


@csrf_exempt
def upload_csv(request):
    if request.method == "POST":
        file = request.FILES['file']

        # Save CSV temporarily
        file_path = default_storage.save(file.name, file)

        df = pd.read_csv(file_path)

        records = df.to_dict(orient="records")

        return JsonResponse({"filename": file.name, "records": records})

    return JsonResponse({"error": "Invalid request"}, status=400)
