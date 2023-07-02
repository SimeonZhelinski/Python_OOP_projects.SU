class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str):
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail: str):
        return mail in self.mails

    def __is_domain_valid(self, domain: str):
        return domain in self.domains

    def validate(self, email: str):
        first_split = email.split("@")
        name = first_split[0]
        second_split = first_split[1].split(".")
        mail = second_split[0]
        domain = second_split[1]
        return all([self.__is_name_valid(name), self.__is_mail_valid(mail), self.__is_domain_valid(domain)])
