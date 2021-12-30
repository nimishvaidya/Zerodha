from nsetools import Nse
nse = Nse()
print(nse)

q = nse.get_quote('infy') # it's ok to use both upper or lower case for codes.
from pprint import pprint # just for neatness of display
#pprint(q)

nse.get_index_list()

print(nse.get_index_quote("nifty bank"))