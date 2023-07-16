from abc import ABC, abstractmethod


class IEmail(ABC):

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class IContent(ABC):
    def __init__(self, content):
        self.content = content

    @abstractmethod
    def format(self):
        pass


class MyContent(IContent):

    def format(self):
        return '\n'.join(['<myML>', self.content, '</myML>'])


class IProtocol(ABC):
    def __init__(self, protocol):
        self.protocol = protocol

    @abstractmethod
    def format_sender(self, sender):
        pass

    @abstractmethod
    def format_receiver(self, receiver):
        pass


class MyProtocol(IProtocol):

    def format_sender(self, sender):
        return ''.join(["I'm ", sender])

    def format_receiver(self, receiver):
        return ''.join(["I'm ", receiver])


class Email(IEmail):

    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, content):
        self.__content = content.format()

    def __repr__(self):

        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = MyContent('Hello, there!')
email.set_content(content)
print(email)
