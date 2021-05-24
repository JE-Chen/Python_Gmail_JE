import os
import unittest

from je_gmail.core import GmailCore


class TestGmail(unittest.TestCase):

    def setUp(self) -> None:
        self.Gmail = GmailCore('/test')

    def test_log(self):
        with open(os.getcwd() + '/test/templates/Email_Template1_Picture.html', 'r+') as File:
            content = (File.read())
        self.Gmail.Gmail_API.send_mail_attach("410877027@mail.nknu.edu.tw", "410877027@mail.nknu.edu.tw", "Hello",
                                              content, attach_file=os.getcwd() + '/test/images/firefox_test.png',
                                              use_html=True)
        File.close()


if __name__ == '__main__':
    suite = (unittest.TestLoader().loadTestsFromTestCase(TestGmail))
    unittest.TextTestRunner(verbosity=2).run(suite)
