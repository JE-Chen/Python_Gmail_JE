import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from functools import partial

#信件類別
class Mail:
    #初始化
    def __init__(self,String_To="410877027@mail.nknu.edu.tw",String_Subject="Test",String_content="Test"):
        #設定物件內部變數 gmail_user
        self.gmail_user = '410877027@mail.nknu.edu.tw'
        # 設定物件內部變數 gmail_password
        self.gmail_password = 'zenazm1397'  # your gmail password
        # 設定物件內部變數 String_To 用來決定傳給誰
        self.String_To = String_To
        # 設定物件內部變數 String_Subject 用來決定信件主旨
        self.String_Subject = String_Subject
        # 設定物件內部變數 String_content 用來決定信件內容
        self.String_content = String_content
        # 設定物件內部變數 msg 內容為 String_content
        self.msg = MIMEText(String_content)
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
        #登入
        self.server.login(self.gmail_user, self.gmail_password)
        print("TO",self.String_To,"Content",self.String_content,"Subject",self.String_Subject)

    #str物件後的回傳
    def __str__(self):
        return "String_To \t "+self.String_To+"\nString_Subject \t"+self.String_Subject+"\nString_content \t "+self.String_content

    #設定主旨
    def String_Subject(self,String_Subject):
        self.String_Subject=String_Subject

    # 設定內容
    def String_content(self,String_content):
        self.String_content=String_content

    # 寄信
    def send_mail(self):
        #資料不正確
        if(self.String_To==None or self.String_Subject==None or self.String_content==None):
            raise ValueError("未設置正確")
        else:
            #信件寄出
            self.server.send_message(self.msg)
            #關閉寄信smtp server
            self.server.quit()
            #確認用訊息
            print('Email sent!')

#寄信用方法
def Send_Mail():
    String_To=str(TO_Entry.get())
    String_Subject=str(Subject_Entry.get())
    String_Content=str(Content_Text.get("1.0", "end-1c"))
    print("In Send_Mail","TO", String_To, "Content", String_Content, "Subject", String_Subject)
    #實例化物件
    mail=Mail(String_To,String_Subject,String_Content)
    #使用物件 send.mail 方法
    mail.send_mail()

#window 物件 =tk.Tk方法的回傳值
window=tk.Tk()
#設定視窗大小
window.geometry("500x500")
#設定視窗標題
window.title("SMTP EMail System")
#設定視窗不可縮放
window.resizable(0,0)
#設定視窗Label 用於提示輸入
TO_Label=tk.Label(window,fg='black',font=('Times New Roman',12),text="收件人 \n 請在下方輸入收件人:")
TO_Label.pack(fill="x")
#設定視窗Entry 用於輸入收件人
TO_Entry=tk.Entry(window,fg='black',font=('Times New Roman',12))
TO_Entry.pack(fill="x")
#設定視窗Label 用於提示輸入
Suject_Label=tk.Label(window,fg='black',font=('Times New Roman',12),text="主旨 \n 請在下方輸入主旨:")
Suject_Label.pack(fill="x")
#設定視窗Entry 用於輸入主旨
Subject_Entry=tk.Entry(window,fg='black',font=('Times New Roman',12))
Subject_Entry.pack(fill="x")
#設定視窗Label 用於提示輸入
Content_Label=tk.Label(window,fg='black',font=('Times New Roman',12),text="內容 \n 請在下方輸入內容:")
Content_Label.pack(fill="x")
#設定視窗text 用於輸入內容
Content_Text=tk.Text(window,fg='black',font=('Times New Roman',12),height=15)
Content_Text.pack(fill="x")
#設定視窗button 用於取得資料跟寄信
Send_Button=tk.Button(window, text="Send Mail",command=partial(Send_Mail))
Send_Button.pack(fill="x",expand=True)
window.mainloop()