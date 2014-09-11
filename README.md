CastingWords Transcription API  
=================
Python Client
-------------


Install:

    $ python setup.py install

Example:

     $ python
     Python 2.7.5 (default, Aug 25 2013, 00:04:04)
     GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
     Type "help", "copyright", "credits" or "license" for more information.  
     >>> from castingwords import API4
     >>> cw = API4("123456789asdfghjkl0987654321")
     >>> cw.prepay_balance()
     u'1.00'
     >>> cw.order_url("http://example.com/media.mp3")
     {u'message': u"Order '0a0' Created", u'audiofiles': [0000001], u'order': u'0a0'}

See Also: 
* [CastingWords Transcription API Description](https://castingwords.com/support/transcription-api.html)
* [CastingWords API Docs](https://castingwords.com/docs/developer/SimpleAPI.html)







