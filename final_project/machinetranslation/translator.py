import json
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


load_dotenv()

#apikey = os.environ['apikey']
#url = os.environ['url']
apikey='N7KRwpL9qDw2eLNJUh89pw28UvX1BS0aziowrLJC3WwV'
url='https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/46f8e3b5-9ac9-4b96-a098-0908acad7023'
authenticator=IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(version='2018-08-01',authenticator=authenticator)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    frenchText = language_translator.translate(text=englishText,model_id='en-fr').get_result()
    frenchText = frenchText.get("translations")[0].get("translation")
    

    return frenchText


def frenchToEnglish(frenchText):
    englishText = language_translator.translate(text=frenchText,model_id='fr-en').get_result()
    englishText = englishText.get("translations")[0].get("translation")

    

    return englishText