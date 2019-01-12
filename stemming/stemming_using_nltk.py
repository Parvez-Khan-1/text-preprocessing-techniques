from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

ps = PorterStemmer()

print(ps.stem('grows'))

print(ps.stem('leaves'))

print(ps.stem('fairly'))

print(ps.stem('communities'))

print("="*20)

ss = SnowballStemmer(language='english')

print(ss.stem('grows'))

print(ss.stem('leaves'))

print(ss.stem('fairly'))

print(ss.stem('communities'))