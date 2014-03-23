import smtplib


class MailServer(object):
    """
    A mail server facade. Immediately connects to the mail server upon
    instantiation. Do not create needlessly.
    """

    def __init__(self, username, password):
        self.username = username
        self.server = smtplib.SMTP('smtp.gmail.com:587')
        self.server.ehlo()
        self.server.starttls()
        self.server.login(username, password)

    def send(self, to_addr, subject, body):
        """
        Send an email from self.username
        """
        msg = "\r\n".join([
            "From: Dr. Rain <" + self.username + ">",
            "To: " + to_addr,
            "Subject: {0}".format(subject),
            "",
            "{0}".format(body)
        ])

        self.server.sendmail(self.username, [to_addr], msg)

    def quit(self):
        """
        Close connection to the mail server
        """
        self.server.quit()


