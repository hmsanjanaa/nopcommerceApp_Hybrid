import configparser

config = configparser.RawConfigParser()
config.read(".\\config\\config.ini")

class ReadConfig:
    @staticmethod
    def getAppURL():
        url = config.get('common data', 'baseURL')
        return url

    @staticmethod
    def getUsermail():
        usermail = config.get('common data', 'usermail')
        return usermail

    @staticmethod
    def getPassword():
        password = config.get('common data', 'password')
        return password

