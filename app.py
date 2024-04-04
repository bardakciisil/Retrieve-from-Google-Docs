from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import random
import msvcrt 
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')


credentials_doc = 'service_account.json'


service_account_info = json.load(open(credentials_doc))
credentials = Credentials.from_service_account_info(service_account_info)
service = build('docs', 'v1', credentials=credentials)

document_id='1L8jwvwmf8p1lMAHzG8dcF2tU23KuyNC8M-twMxrQOjc'

document = service.documents().get(documentId=document_id).execute()
print(document)

def main():
    document_content = document['body']['content']
    text_content = ''
    for content in document_content:
        if 'paragraph' in content:
            for element in content['paragraph']['elements']:
                if 'textRun' in element and 'content' in element['textRun']:
                    text_content += element['textRun']['content']

    while True:
        input("Press enter to continue...")
        random_word = get_random_line_with_keyword(text_content)
        if random_word:
            print(random_word.strip())
        else:
            print("char could't find.")
            continue
        
        print("press any key for continue...")
        msvcrt.getch()  

        after_colon = get_random_line_with_keyword(text_content, ':')
        if after_colon:
            print(after_colon.strip().split(':', 1)[-1].strip())
        else:
            print("char could't find.")
            continue

if __name__ == "__main__":
    main()

def get_random_line_with_keyword(document_content, keyword=':'):
    random_line = random.choice(document_content.split('\n'))

    keyword_index = random_line.find(keyword)
  
    if keyword_index != -1:
        return random_line[:keyword_index + 1]  
    else:
        return None