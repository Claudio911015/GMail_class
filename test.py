import gmail
import os

os.chdir(r'D:\Git\Python\Gmail_class')

SCOPES = [
        "https://www.googleapis.com/auth/gmail.labels",			
        "https://www.googleapis.com/auth/gmail.send",				
        "https://www.googleapis.com/auth/gmail.readonly",			
        "https://www.googleapis.com/auth/gmail.compose",			
        "https://www.googleapis.com/auth/gmail.insert",			
        "https://www.googleapis.com/auth/gmail.modify",						
        "https://www.googleapis.com/auth/gmail.settings.basic",	
        "https://www.googleapis.com/auth/gmail.settings.sharing"]
correo = gmail.mail(SCOPES,'me')

#correo.showLabels()
correos = correo.ListMessagesMatchingQuery('from:a.turrent@bbva.com')

correo.snippets(correos)
