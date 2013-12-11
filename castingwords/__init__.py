#    CastingWords API python client
#
#    Copyright (c) 2013 CastingWords LLC
#
# See the License file
# distributed with this work for additional information
# regarding copyright ownership.  The CastingWords licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
Access to the CastingWords API.  Order transcripts, and track thier progress
"""

__version__ = "0.1.0"
__author__ = "Nathan McFarland <nathan@castingwords.com>"


import requests

class API4(object):
    def __init__(self, api_key):        
        self.api_key = api_key
        self.base = 'https://castingwords.com/store/API4'
        self.response=None
        
    def path(self, *args):
        L = [self.base]
        L.extend(args)
        return '/'.join(L) 

    def audiofile_details(self, afid):   
        """
        Gets a dictionary of attribute for this audiofile. 
        The current transcription status is in 'statename'.
        """
        self.response = requests.get(self.path("audiofile/" + str(afid)), params={"api_key": self.api_key})
        return  self.response.json()


    def audiofile_transcript(self, afid, extension):   
        """
        Returns the transcript for a given audiofile_id - valid extensions are 
        txt
        doc
        rtf
        html
        """
        self.response = requests.get(self.path("audiofile/" , str(afid), "transcript.", ext ), params={"api_key": self.api_key})
        return  self.response.json()


    def runrate(self,sku):
        self.response = requests.get(self.path("runrate"), params={"api_key": self.api_key})
        return  self.response.json().get('cap').get(sku)
        

    def order_url(self, url, sku):   
        """
        Orders a transcript. Returns the order and audiofile ids.
        url -  Url(s) of audio/video to transcribe.  Preferably points to an mp3. ;
        sku -  one or more skus to order.
          TRANS14   =  Budget Transcription with a target of 14 days. 
          TRANS2    =  1 Day Transcription
          TRANS6    =  6 Day Transcription
          DIFFQ2    =  Difficult Audio
          TSTMP1    =  Timestamps
          VERBATIM1 =  Verbatim Transcription

        Return Example: {u'message': u"Order '0a0' Created", u'audiofiles': [0000001], u'order': u'0a0'}
        
        """
        self.response = requests.post(self.path("order_url"), params={"api_key": self.api_key, "url":url, "sku":sku})
        return  self.response.json()


    def order_media(self, mediaid, sku):   
        self.response = requests.post(self.path("order_media"), params={"api_key": self.api_key, "mediaid":mediaid, "sku":sku})
        return  self.response.json()
       

    def prepay_balance(self):   
        """
        Returns the remaining prepay balance for your account
        """
        self.response = requests.get(self.path("prepay_balance"), params={"api_key": self.api_key})
        return  self.response.json().get("balance")

    def set_webhook(self, callback_url):   
        self.response = requests.post(self.path("webhook"), params={"api_key": self.api_key,  "webhook":callback_url})
        return  self.response.json()

    def webhook(self):   
        self.response = requests.get(self.path("webhook"), params={"api_key": self.api_key})
        return  self.response.json()








