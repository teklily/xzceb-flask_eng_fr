import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
#api and url

apikey = os.environ['apikey']
url = os.environ['url']

authenticator =IAMAuthenticator("Ibu_XE6JrOL-7BhwZHMlLLBYycvfp3XVPBOQ5x3H5lQM")
language_translator = LanguageTranslatorV3(version = '2018-05-01', authenticator=authenticator)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/8938ff7e-094f-402e-bd08-d42f85a0ae25')

language_translator.set_disable_ssl_verification(True)
def en_to_fr(english_text):
    translatione = language_translator.translate(text=english_text, model_id='en-fr').get_result()
    #french_text = translatione['translations'][0]['translation']
    return translatione.get("translations")[0].get("translation")

def fr_to_en(french_text):
    #f2e
    translationf = language_translator.translate(text=french_text, model_id='en-fr').get_result()
   # english_text = translationf['translations'][0]['translation']
    return translationf.get("translations")[0].get("translation")