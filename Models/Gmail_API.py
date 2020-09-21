import base64
import os
import os.path
import pickle
import mimetypes
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import errors
from googleapiclient.discovery import build


class Gmail_API():

    def Get_Service(self):
        SCOPES = [
            'https://www.googleapis.com/auth/gmail.readonly',
            'https://www.googleapis.com/auth/gmail.send',
        ]
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    r'../client_secret.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        service = build('gmail', 'v1', credentials=creds)
        return service

    def Want_Send_Message(self,service, sender, message):
      try:
        sent_message = (service.users().messages().send(userId=sender, body=message)
                   .execute())
        return sent_message
      except errors.HttpError as error:
        raise error

    def Create_Message(self,sender, to, subject, message_text,Use_Html=False):
      if Use_Html:
          message = MIMEText(message_text,'html')
      else:
          message = MIMEText(message_text)
      message['to'] = to
      message['from'] = sender
      message['subject'] = subject
      s = message.as_string()
      b = base64.urlsafe_b64encode(s.encode('utf-8'))
      return {'raw': b.decode('utf-8')}

    def Create_Message_With_Attachment(self,sender, to, subject, message_text, file,Use_Html=False):
        message = MIMEMultipart()
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        if Use_Html:
            msg = MIMEText(message_text,'html')
        else:
            msg = MIMEText(message_text)
        message.attach(msg)
        content_type, encoding = mimetypes.guess_type(file)
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)
        if main_type == 'text':
            fp = open(file, 'rb')
            msg = MIMEText(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'image':
            fp = open(file, 'rb')
            msg = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'audio':
            fp = open(file, 'rb')
            msg = MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()
        else:
            fp = open(file, 'rb')
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
            fp.close()
        filename = os.path.basename(file)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.add_header('Content-ID', '<%s>' % filename)
        message.attach(msg)

        return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

    def Send_Mail_Basic(self,From="Mail_Address",To="Mail_Address",Subject="Test subject",Body="Test body",UseHTML=False):
        try:
            service = self.Get_Service()
            message = self.Create_Message(From,To, Subject, Body,Use_Html=UseHTML)
            self.Want_Send_Message(service, From, message)

        except Exception as e:
            raise e

    def Send_Mail_Attach(self,From="Mail_Address",To="Mail_Address",Subject="Test subject",Body="Test body",Attach_File='File_Path',UseHTML=False):
        try:
            service = self.Get_Service()
            message = self.Create_Message_With_Attachment(From,To,Subject,Body,Attach_File,Use_Html=UseHTML)
            self.Want_Send_Message(service, From, message)

        except Exception as e:
            raise e