# Test the classifiers for Sentiment Analysis
# using one positive statement and one negative statement

import sentimentDetectionModule as s

print(s.sentiment("This movie was awesome! The acting was great, plot was wonderful !!!"))
print(s.sentiment("This movie was utter junk. There were absolutely no plot. I don't see what the point was at all. Horrible movie !!!"))
