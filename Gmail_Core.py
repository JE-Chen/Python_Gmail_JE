from Gmail_API import Gmail_API
from Gmail_Get_Token import Gmail_Get_Token
from Smtp_Gmail import Smtp_Gmail

class Gmail_Core():

    def __init__(self):
        try:
            self.Gmail_API=Gmail_API()
            self.Gmail_Get_Token=Gmail_Get_Token()
            self.Smtp_Gmail=Smtp_Gmail()
        except Exception as Errr:
            raise Errr