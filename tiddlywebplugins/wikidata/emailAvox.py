import logging
from tiddlywebplugins.wikidata import recordFields
from tiddlywebplugins.wikidata.sendEmail import send

def emailAvox(query):
    requestType = query['requestType'][0]
    name = query['name'][0]
    email = query['email'][0]
    country = query['country'][0]
    company = query['company'][0]
    if requestType == 'request':
        avid = query['avid'][0]
        legal_name = query['legal_name'][0]
        to = ['addadatarecord.wiki-data@avox.info', 'jnthnlstr@googlemail.com']
        subject = 'Request for more information'
        body = 'SPECIFIC REQUEST re: additional information request\n' \
            'for '+legal_name+' (AVID = '+avid+')\n' \
            'Name: '+name+'\n' \
            'Email address: '+email+'\n' \
            'Country: '+country+'\n' \
            'Company: '+company+'\n'
    elif requestType == 'challenge':
        avid = query['avid'][0]
        legal_name = query['legal_name'][0]
        source = query['source'][0]
        to = ['foundanerror.wiki-data@avox.info', 'jnthnlstr@googlemail.com']
        subject = 'Challenge record'
        body = 'SPECIFIC REQUEST re: correction\n' \
            'for '+legal_name+' (AVID = '+avid+')\n' \
            'Name: '+name+'\n' \
            'Email address: '+email+'\n' \
            'Country: '+country+'\n' \
            'Company: '+company+'\n' \
            'Source for challenge: '+source+'\n' \
            'Challenge details\n--------------\n'
        for field, _ in recordFields.recordFields:
            try:
                body += field+': '+query['challenge_'+field][0]+'\n'
            except KeyError:
                pass
    elif requestType == 'suggest_new':
        to = ['adam.edwards@avox.info', 'daniel.dunn@avox.info', 'paul.barlow@avox.info', 'kate.young@avox.info', 'brian.cole@avox.info', 'ken.price@avox.info', 'jnthnlstr@googlemail.com']
        subject = 'Wiki-data AVID record suggestion'
        body = """Submittor info
--------------
Name: %s
Email address: %s
Country: %s
Company: %s


Record info
--------------
""" % (name, email, country, company)
        for field, _ in recordFields.recordFields:
            try:
                body += field + ': ' + query[field][0] + '\n'
            except KeyError:
                pass
    else:
        to = 'jnthnlstr@googlemail.com'
        subject = 'Unknown contact type'
        body = 'Query: %s' % repr(query)
    logging.debug('to: %s , subject: %s body: %s', repr(to), subject, body)
    send(to, subject, body)