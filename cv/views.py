from django.http import FileResponse
from cv.pdfGen import generate_pdf_cv



def cvPDF(request):
    censor = not(request.user and request.user.is_staff)
    language = request.GET["lan"] if "lan" in request.GET else "IS"
    pdf = generate_pdf_cv( censor, language.upper())
    return FileResponse(pdf, as_attachment=False, filename='MagnusMagnusson_CV.pdf')