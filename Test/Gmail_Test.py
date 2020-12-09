from Core.GmailCore import GmailCore

a = GmailCore()
a.Gmail_API.send_mail_attach("410877027@mail.nknu.edu.tw", "410877027@mail.nknu.edu.tw", "Hello",
                             r"""
                             <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
                             <html xmlns="http://www.w3.org/1999/xhtml" lang="zh">
                             <head>
                                 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                                 <title>Email Template</title>
                                 <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
                             </head>
                             <body style="margin:0; padding:0;">
                             <table border="1" cellpadding="0" cellspacing="0" width="600" bgcolor="#a9a9a9" style="border-collapse: collapse;">
                                 <tr>
                                     <td align="center" bgcolor="#a9a9a9" style="padding:40px 0 30px 0;">
                                         <img src="cid:firefox_test.png" alt="Test Email Image" width="384" height="384" style="display: block;" />
                                     </td>
                                 </tr>
                             </table>
                             </body>
                             </html>
                             """, attach_file='../images/firefox_test.png', use_html=True)
