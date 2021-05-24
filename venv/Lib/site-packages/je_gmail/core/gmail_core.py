import datetime

from je_gmail.modules.gmail_api import GmailApi
from je_gmail.modules.smtp_gmail import SmtpGmail
from je_gmail.token.gmail_get_token import GmailGetToken


class GmailCore(object):

    def __init__(self, path):
        try:
            self.Gmail_API = GmailApi(path)
            self.Gmail_Get_Token = GmailGetToken()
            self.Smtp_Gmail = SmtpGmail()
        except Exception as error:
            raise error
        print(datetime.datetime.now(), self.__class__, 'Ready', sep=' ')
