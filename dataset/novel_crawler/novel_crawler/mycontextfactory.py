# mycontextfactory.py
import ssl
from scrapy.core.downloader.contextfactory import ScrapyClientContextFactory

class MyContextFactory(ScrapyClientContextFactory):
    def getContext(self, hostname=None, port=None):
        ctx = super(MyContextFactory, self).getContext()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx
