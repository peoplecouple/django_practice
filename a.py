from googletrans import Translator
 
# print(googletrans.LANGUAGES)
 
text1 = "안녕하세요. 저는 학생입니다!"
 
translator = Translator()
 
trans1 = translator.translate(text1, src='ko', dest='en')

print("Korean to English: ", trans1.text)
