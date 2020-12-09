import datetime

from Modules.GmailApi import GmailApi
from Modules.SmtpGmail import SmtpGmail
from Token.GmailGetToken import GmailGetToken


class GmailCore:

    def __init__(self):
        try:
            self.Gmail_API = GmailApi()
            self.Gmail_Get_Token = GmailGetToken()
            self.Smtp_Gmail = SmtpGmail()
        except Exception as error:
            raise error
        print(datetime.datetime.now(), self.__class__, 'Ready', sep=' ')
