from cgitb import small
from django.shortcuts import render
import io
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from django.conf import settings
from cv.models import BaseInfo, References, Education, Experience, Description, Skill, Interest

STATIC_ROOT = settings.STATIC_ROOT

#constants
a4 = (595.35, 841.995)
xp = a4[0] / 100.00
yp = a4[1] / 100.00
purple = (0.51,0.05,0.37,1)
black = (0,0,0,1)
white = (1,1,1,1)
red = (1,0.25,0.25,1)
gray = (0.8,0.8,0.8,1)
marginRatio = 2.5
third = (100.00 / 3.00) * xp

giantFont = ['Helvetica', 18]
bigFont = ['Helvetica', 16]
largeFont = ['Helvetica', 14]
midFont = ['Helvetica', 12]
smallFont = ['Helvetica', 10]
tinyFont = ['Helvetica', 8]

def generate_pdf_cv(censor = True):
    #buffer 
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    background_design(p)
    left_side(p, censor)    
    p.setStrokeColorRGB(*black)
    p.setFillColorRGB(*black)
    right_side(p)

    #Finalizing
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer

def left_side(p, censor):
    p.setStrokeColorRGB(*purple)
    p.setFillColorRGB(*purple)
    offset = image(p)    
    p.setStrokeColorRGB(*white)
    p.setFillColorRGB(*white)
    offset -= marginRatio * yp
    offset = about(p, offset)
    offset -= marginRatio * yp
    offset = personal_info(p, offset, censor)
    offset -= 2.25*marginRatio*yp
    references(p, offset, censor)

def right_side(p):
    off = 100*yp - marginRatio * yp
    off = education(p, off)
    off = experiences(p, off)
    off = skills(p, off)
    off = interests(p, off)

def experiences(p, off):
    ##experiences
    off -= marginRatio * yp
    p.setFont(*giantFont)
    third = (100.00 / 3.00) * xp
    p.drawString(third + xp * marginRatio, off, "Starfsreynsla")
    experiences = Experience.objects.all().order_by("-end")
    off -= marginRatio * yp
    for experience in experiences:
        p.setFont(*largeFont)
        p.drawString(third + 2*xp * marginRatio, off, experience.workplace)
        p.drawRightString(100*xp - xp*marginRatio, off, experience.start + "-"+experience.end)
        off -= marginRatio * yp
        p.setFont(*midFont)
        p.drawString(third + 2*xp * marginRatio, off, experience.position)
        off -= marginRatio * yp
        p.setFont(*smallFont)

        off -= drawStringExt(p, third + 2*xp * marginRatio,  off, experience.description, 2*third - 2*xp * marginRatio, marginRatio*yp)
        off -= 1.5*yp
    return off

def education(p, off):
    ##education
    off -= marginRatio * yp
    p.setFont(*giantFont)
    third = (100.00 / 3.00) * xp
    p.drawString(third + xp * marginRatio, off, "Menntun")
    degrees = Education.objects.all().order_by("-end")
    off -= marginRatio * yp
    for degree in degrees:
        p.setFont(*largeFont)
        p.drawString(third + 2*xp * marginRatio, off, degree.degree)
        p.drawRightString(100*xp - xp*marginRatio, off, degree.start + "-"+degree.end)
        off -= marginRatio * yp
        p.setFont(*midFont)
        p.drawString(third + 2*xp * marginRatio, off, degree.school)
        off -= marginRatio * yp
    return off

def background_design(p):
    #left border
    p.setPageSize(a4)
    p.setFillColorRGB(*purple)
    p.setStrokeColorRGB(*purple)
    p.rect(-xp,-yp,xp*(100.0/3.0),100*yp + yp,0,1)

def image(p):
    #image
    img = ImageReader(STATIC_ROOT +"/img/pfp_img_1.jpg")
    size = img.getSize()
    imgX = marginRatio * xp 
    imgW = ((100.0/3.0) - 2*marginRatio)*xp
    ratio = imgW / size[0]
    imgH = ratio * size[1]
    imgY = yp * (100 - marginRatio) - imgH
    p.drawImage(img,imgX, imgY, imgW, imgH)
    p.setLineWidth(20)
    p.roundRect(imgX, imgY, imgW, imgH, 20,1,0)
    p.setLineWidth(5)

    #my name.
    p.setFillColorRGB(*white)
    p.setStrokeColorRGB(*white)
    p.setFont(*bigFont)
    p.drawCentredString(xp*(100.0/3.0) / 2,imgY - marginRatio * yp, "Magnús Á. Magnússon")
    return imgY - marginRatio * yp

def about(p, off):
    desc = Description.objects.all()
    if(len(desc) > 0):
        d = desc[0]
        p.setFont(*smallFont)
        off -= drawStringExt(p, marginRatio*xp, off, d.description, xp*((100.0 / 3.0) - 2*marginRatio), 0.55*marginRatio*yp)

    return off

def personal_info(p, offset, censor):
    info = BaseInfo.objects.all().order_by("section__ordering")
    lastSection = None 
    off = offset
    p.setFont(*midFont)
    for sec in info:
        if sec.section != lastSection:
            lastSection = sec.section
            off -= marginRatio * yp 
        if sec.icon != "":
            img = STATIC_ROOT + "/cv/icons/" + sec.icon
            scale = 1*marginRatio*xp
            p.drawImage(img, xp * marginRatio, off - (scale/4), width=scale, height=scale, mask='auto', anchor='n')
        
        text = sec.text if sec.public or not censor else "*************"
        p.drawRightString(xp * (100.0/3.0 - marginRatio), off, text)
        off -= 2*yp
        ## References
    return off

def references(p, offset, censor):    
    references = References.objects.all()
    off = offset
    p.setFont(*largeFont)
    p.drawString(xp * marginRatio, off, "Meðmæli:")
    off += 1*yp
    if censor:
        off -= 4*yp
        p.setFont(*smallFont)
        p.drawString(xp * marginRatio, off, "Meðmæli falin af friðhelgisástæðum.")
    else:
        for reference in references:
            off -= 3*yp
            p.setFont(*midFont)
            p.drawString(xp * marginRatio, off, reference.name)
            p.setFont(*smallFont)
            off -= 2*yp
            p.drawString(xp * marginRatio, off, reference.job)
            #off -= 2*yp
            #p.drawString(xp * marginRatio, off, reference.relation)
            off -= 2*yp
            p.drawString(xp * marginRatio, off, reference.email)
            off -= 2*yp
            p.drawString(xp * marginRatio, off, reference.phone)
    return off

def skills(p, offset):
    p.setFont(*giantFont)
    middle = xp*marginRatio + third
    p.drawString(middle, offset, "Hæfni")
    middle += xp*marginRatio
    skillDict = Skill.skillDict()
    offset -= marginRatio * yp
    p.setFont(*midFont)
    p.setLineWidth(1)
    hor = 0
    horSeperation = 30 * xp
    for category in skillDict:
        for skill in skillDict[category]:
            p.setFillColorRGB(*black)
            p.drawString((hor * horSeperation) + middle, offset, skill[0])
            val = skill[1]
            for i in range(1,6):
                if val >= i:
                    p.setFillColorRGB(*purple)
                else:
                    p.setFillColorRGB(*gray)
                p.circle((hor * horSeperation) + middle + 9*xp + 2.5*i*xp, offset + 0.5*xp, xp,0,1)
            hor += 1
            if(hor >= 2):
                hor = 0
                offset -= marginRatio * yp
        offset -= yp
    return offset

def interests(p, offset):
    offset -= yp
    p.setFillColorRGB(*black)
    p.setFont(*giantFont)
    middle = xp*marginRatio + third
    p.drawString(middle, offset, "Áhugamál")
    offset -= marginRatio * yp
    interests = Interest.objects.all().order_by("interest")
    intTest = ""
    for interest in interests:
        intTest += interest.interest + ", "
    intTest = intTest[:-2]+", og fleira"
    p.setFont(*smallFont)
    drawStringExt(p, middle + 2*xp, offset, intTest, third*2 - 2*xp*marginRatio, marginRatio*yp)

def drawStringExt(canvas, x, y, text, width, sep):
    segments = []
    words = text.split()
    segment = ""
    while len(words) > 0:
        word = words.pop(0)
        if canvas.stringWidth(segment + word) > width:
            segments.append(segment)
            segment = ""
        segment += word + " "
    segments.append(segment)
    off = 0
    for segment in segments:
        canvas.drawString(x, y - off, segment)
        off += sep
    return off