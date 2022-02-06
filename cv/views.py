from django.http import FileResponse
from cv.pdfGen import generate_pdf_cv



def cvPDF(request):
    pdf = generate_pdf_cv(not(request.user and request.user.is_staff))
    return FileResponse(pdf, as_attachment=False, filename='MagnusMagnusson_CV.pdf')