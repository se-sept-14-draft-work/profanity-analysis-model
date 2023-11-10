from pprint import pprint
from detoxify import Detoxify

results = Detoxify("original").predict("I like the way professor madhavan teaches this java course as he drills down on the fundamentals")
pprint(results)
