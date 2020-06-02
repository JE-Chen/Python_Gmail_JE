import base64
import logging
import os
import os.path
import pickle

# Import the email modules we'll need
import mimetypes
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient import errors
from googleapiclient.discovery import build
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)

class Gmail_API():

    def Get_Service(self):
        """Gets an authorized Gmail API service instance.

        Returns:
            An authorized Gmail API service instance..
        """

        # If modifying these scopes, delete the file token.pickle.
        SCOPES = [
            'https://www.googleapis.com/auth/gmail.readonly',
            'https://www.googleapis.com/auth/gmail.send',
        ]

        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)
        return service

    def Want_Send_Message(self,service, sender, message):
      """Send an email message.

      Args:
        service: Authorized Gmail API service instance.
        user_id: User's email address. The special value "me"
        can be used to indicate the authenticated user.
        message: Message to be sent.

      Returns:
        Sent Message.
      """
      try:
        sent_message = (service.users().messages().send(userId=sender, body=message)
                   .execute())
        logging.info('Message Id: %s', sent_message['id'])
        return sent_message
      except errors.HttpError as error:
        logging.error('An HTTP error occurred: %s', error)

    def Create_Message(self,sender, to, subject, message_text):
      """Create a message for an email.

      Args:
        sender: Email address of the sender.
        to: Email address of the receiver.
        subject: The subject of the email message.
        message_text: The text of the email message.

      Returns:
        An object containing a base64url encoded email object.
      """
      message = MIMEText(message_text)
      message['to'] = to
      message['from'] = sender
      message['subject'] = subject
      s = message.as_string()
      b = base64.urlsafe_b64encode(s.encode('utf-8'))
      return {'raw': b.decode('utf-8')}

    def Create_Message_With_Attachment(self,sender, to, subject, message_text, file):
        """Create a message for an email.

        Args:
          sender: Email address of the sender.
          to: Email address of the receiver.
          subject: The subject of the email message.
          message_text: The text of the email message.
          file: The path to the file to be attached.

        Returns:
          An object containing a base64url encoded email object.
        """
        message = MIMEMultipart()
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject

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
        message.attach(msg)

        return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

    def Send_Mail_Basic(self,From="Mail_Address",To="Mail_Address",Subject="Test subject",Body="Test body"):

        logging.basicConfig(
            format="[%(levelname)s] %(message)s",
            level=logging.INFO
        )

        try:
            service = self.Get_Service()
            message = self.Create_Message(From,To, Subject, Body)
            self.Want_Send_Message(service, From, message)

        except Exception as e:
            logging.error(e)
            raise

    def Send_Mail_Attach(self,From="Mail_Address",To="Mail_Address",Subject="Test subject",Body="Test body",Attach_File='File_Path'):
        logging.basicConfig(
            format="[%(levelname)s] %(message)s",
            level=logging.INFO
        )

        try:
            service = self.Get_Service()
            #param From,To,Subject,Body,Attach_File
            message = self.Create_Message_With_Attachment(From,To,Subject,Body,Attach_File)
            #Service Sender,Message
            self.Want_Send_Message(service, From, message)

        except Exception as e:
            logging.error(e)
            raise