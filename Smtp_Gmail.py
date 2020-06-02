import smtplib
from email.mime.text import MIMEText


#信件類別
class Smtp_Gmail:
    #初始化
    def __init__(self,gmail_user="User_Address",gmail_password="User_Passward",String_To="User_Address",String_Subject="Test",String_Content="Test"):
        #設定物件內部變數 gmail_user
        self.gmail_user = gmail_user
        # 設定物件內部變數 gmail_password
        self.gmail_password = gmail_password  # your gmail password
        # 設定物件內部變數 String_To 用來決定傳給誰
        self.String_To = String_To
        # 設定物件內部變數 String_Subject 用來決定信件主旨
        self.String_Subject = String_Subject
        # 設定物件內部變數 String_Content 用來決定信件內容
        self.String_Content = String_Content
        # 設定物件內部變數 msg 內容為 String_Content
        self.msg = MIMEText(String_Content)
        # 設定物件內部變數 msg 主旨為 String_Subject
        self.msg['Subject'] = String_Subject
        # 設定物件內部變數 msg 寄件人為 自身的gmail_user
        self.msg['From'] = self.gmail_user
        # 設定物件內部變數 msg 收件人為 String_To
        self.msg['To'] = String_To
        # 設定Gmail 傳送 , Google port number 465
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        #支援用戶認證 helo 不支援
        self.server.ehlo()
        print("TO",self.String_To,"Content",self.String_Content,"Subject",self.String_Subject)

    #設定使用者
    def Set_User_Passward(self,gmail_user,gmail_password):
        #設定物件內部變數 gmail_user
        self.gmail_user = gmail_user
        # 設定物件內部變數 gmail_password
        self.gmail_password = gmail_password  # your gmail password

    def Login(self):
        #登入
        self.server.login(self.gmail_user, self.gmail_password)

    # 設定收件者
    def String_To(self,String_To):
        self.String_To = String_To

    #設定主旨
    def String_Subject(self,String_Subject):
        self.String_Subject=String_Subject

    # 設定內容
    def String_Content(self,String_Content):
        self.String_content=String_Content

    # 寄信
    def Send_Mail(self):
        #資料不正確
        if(self.String_To==None or self.String_Subject==None or self.String_Content==None):
            raise ValueError("未設置正確")
        else:
            #信件寄出
            self.server.send_message(self.msg)
            #關閉寄信smtp server
            self.server.quit()
            #確認用訊息
            print('Email sent!')

    #寄信用方法
    def Send_Mail_Setting(self,String_To,String_Subject,String_Content):
        self.String_To = String_To
        self.String_Subject = String_Subject
        self.String_Content = String_Content
        print("In Send_Mail","TO", self.String_To, "Content",  self.String_Content, "Subject",  self.String_Subject)
        self.Send_Mail()
