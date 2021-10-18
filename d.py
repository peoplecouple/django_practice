import pytesseract
from PIL import Image #이미지 라이브러리랑 같이 써야함

pytesseract.pytesseract.tesseract_cmd = 'tess/tesseract.exe'
im = Image.open("한국기사.png")
text = pytesseract.image_to_string(im, lang="kor")
print(text)
