#!/usr/bin/env python
import sys
import pprint
from castingwords import API4
# usage: ./ex/order_url.py $CASTINGWORDS_API_KEY $MP3_URL
# ex: ./ex/order_mediaid.py 123456789087653789jlhkgytux  http://example.com/media.mp3
api_key =  sys.argv[1]
mediaid =  sys.argv[2]
pp = pprint.PrettyPrinter(indent=4)
api4 = API4(api_key)


try:
    pp.pprint(api4.order_url(url, "TRANS6"))
except:
    pp.pprint(api4.response.text) 






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
