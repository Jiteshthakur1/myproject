import pyttsx3
# import webbrowser
import os


import wikipedia
import speech_recognition as sr
eng=pyttsx3.init('sapi5')
voi=eng.getProperty('voices')
eng.setProperty('voice',voi[0].id)

def rea():
    r=sr.Recognizer()
    with sr.Microphone() as sourc:
        print("Active")
      
        r.pause_threshold=1
        a=r.listen(sourc)
        print(a)
        try:
            txt=r.recognize_google(a)
            
            print(txt)
            return txt.lower()
        except sr.UnknownValueError:
            s( "sorry, could not under stand ")
            return "none"
def s(st):
          
    eng.say(st)
    eng.runAndWait()    
if __name__=="__main__":
    while True:
         q=input("Active :").lower()
        #  q=rea()
         if 'wikipedia' in q:
             s("searching wekipedia ..")
             q=q.replace("wikipedia","")
             result=wikipedia.summary(q,sentences=2)
             s("acording to wikipedia")
             print(result)
             s(result)
         elif "open google" in q:
             webbrowser.open("https://googe.com.in")
         elif "open youtube" in q:
             webbrowser.open_new_tab("https://youtub.com.in")   
         elif "open chat GPT" in q:
             webbrowser.open("https://chatgpt.com")
         elif "creata java file"in q:
             os.system("cd /")
             os.system("cd C:\\Users\\jitesh\\Desktop\\JAVA")
             print("hi")
            #  os.system("mkdir 9")
             a=open(f"w.java","w")
             a.write("class w{\n")
             a.write("public static void main(String []a){\n")
             a.write("}}\n")    
             
       
          
                  

              
             
           
 
    