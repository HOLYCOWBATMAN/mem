# -*- coding: utf-8 -*-
import urllib2, re

def go():
    urls = ['http://memprotec.com/css/master_main-fr.css?4034467386',
        'http://memprotec.com/css/site_global.css?201922450',
        'http://memprotec.com/css/index.css?3868613213',
        'http://memprotec.com/css/compagnie.css?4214478465',
        'http://memprotec.com/css/technologie.css?505215458',
        'http://memprotec.com/css/nos-produits.css?3881783879',
        'http://memprotec.com/css/contact.css?3846667535',
        'http://memprotec.com/css/nos-services.css?357155200']
    
    for url in urls:
        print url
        
        css = urllib2.urlopen(url).read()
        
        err = re.compile("\s*width:\s(?P<value>\d*)(?=px)")
        left = re.compile("\s*left:\s(?P<value>\d*)(?=px)")
        anypx = re.compile("\s*([a-z]*):\s(?P<value>\d*)(?=px)")
        i = -1
        for l in css.splitlines():
            i += 1
            #print type(l)
            #~ if err.match(l) is not None:
                #~ w = err.match(l).group('value')
                #~ if int(w) > 1200:
                    #~ print 'line %s: width %s' % (i, w)
                    #~ 
            #~ if left.match(l) is not None:
                #~ w = left.match(l).group('value')
                #~ if int(w) > 1200:
                    #~ print 'line %s: left %s' % (i, w)
                    
            if anypx.match(l) is not None:
                w = anypx.match(l).group('value')
                
                if int(w) > 1200:
                    print 'line %s: %s %s' % (i, anypx.match(l).group(1), w)
