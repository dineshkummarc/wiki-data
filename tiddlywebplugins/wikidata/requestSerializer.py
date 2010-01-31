
from tiddlyweb.serializations import SerializationInterface

from tiddlywebplugins.wikidata import templating


class Serialization(SerializationInterface):

    def tiddler_as(self, tiddler):
        template = templating.get_template(self.environ, 'request.html')
        try:
            query = self.environ['tiddlyweb.query']
            captcha = {}
            success = query['success'][0]
            if success == '1':
                captcha['success'] = True
            elif success == '0':
                captcha['failure'] = True
                try:
                   captcha['error'] = query['error'][0]
                except:
                   captcha['error'] = "Error not supplied"
        except:
            pass
        commonVars = templating.getCommonVars(self.environ)
        return template.render(tiddler=tiddler, captcha=captcha, commonVars=commonVars)
