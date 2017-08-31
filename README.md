# Twitter-Sentiment-Analysis-using-NLP-Machine-Learning

Sentiment Analysis of Tweets using Natural Language Processing and Machine Learning Techniques.

**Requirements:**

1. **Python 3.5 or above** - Currently all code is written in Python 3.5.

2. **Tweepy** - To use Twitter API and fetch twitter data.

Use:

```
pip install tweepy
```

or

Download tweepy using:

```
git clone https://github.com/tweepy/tweepy.git
```

Go inside the tweepy folder and install it using:

```
python setup.py install
```

3.**Scikit-Learn** - For Machine Learning.

Install using:

```
pip install scikit-learn
```

4.**Matplotlib** - To plot data in real time

Install using:

```
pip install matplotlib
```

5.**Natural Language Processing Toolkit [NLTK]** - For natural language processing

Install using:

```
pip install nltk
```

To download data for additional testing use:

```
python 3
>> import nltk
>> nltk.download()
```

Choose whichever corporous you want to download.



*Note:* If any of the above installations give any errors, you can download the wheel file for "Windows only" from following link:

```
http://www.lfd.uci.edu/~gohlke/pythonlibs/
```

Install it using:

```
pip install name_of_whl_file
```


# Result

## Sample Classification

```
RT @kbari12: Obama and Lynch colluded to keep Hillary out of Prison. Stop insulting Americans Intelligence! #SundayMorning #ObamaWH #CNNSOT… neg 1.0
I want very much to know how everything fits together, Russia, Fisa, Obama, Lynch, and Hillary&amp; Bill Clinton Facts… https://t.co/0Rm2iE2gzO neg 1.0
Obama has a history of tapping &amp; hacking his friends and rivals https://t.co/irV8bTzXSy #NSA... by #LaLaRueFrench75… https://t.co/xxIGweXa4Q neg 1.0
RT @jonfavs: Barack Obama's master plan:
1) Wiretap the opposition 
2) Gather damaging info 
3) Say nothing
4) Let him win 
5) Ride off int… neg 1.0
RT @PadmaLakshmi: The Senate Is Voting on Monday to Destroy Obama’s Fair Pay and Safe Workplace Rules https://t.co/rWu27krDO1 via @aclu pos 1.0
RT @redsteeze: Oh god Trump's going to find out about this and tweet it out. https://t.co/k6fhmwcHB5 neg 1.0
RT @Craftmastah: Not only was Obama behind the  #ObamaWiretapLeaks you can bet that traitor was behind the IRS scandal as well. The man sho… neg 1.0
RT @PrisonPlanet: Why are libs demanding evidence that Obama spied on Trump?
Unnamed sources &amp; baseless claims were enough to satisfy thei… neg 1.0
RT @wikileaks: Obama has a history of tapping &amp; hacking his friends and rivals https://t.co/XbwyNSwTXg  #NSA #PRISM #Merkel…  neg 1.0
RT @PolticsNewz: Trump’s claim about Obama wiretapping him is indefensible. So his aides aren’t even defending it.…  neg 1.0
RT @DavidCornDC: If you have ever wondered how fascism starts.... https://t.co/7vSgRmkPQP neg 1.0
Obama Issue Unlawful “Recess-Appointments” Over a Long Weekend Source: United States Court of Appeals neg 1.0
RT @1bigbeer: Outrageous! President Obama ‘Put His Thumb on the Scale Using All Levers of Power’ https://t.co/9fZsyyUohK pos 1.0
@tedavis62 @ArthurCSchaper Obama funneled millions to this La Raza Terrorist hate group! neg 1.0
RT @jonfavs: Barack Obama's master plan:
1) Wiretap the opposition 
2) Gather damaging info 
3) Say nothing
4) Let him win 
5) Ride off int… neg 1.0
```

## False Prediction Examples

```
RT @RichardGrenell: CNN's "Chief National Security Reporter" was an Obama political appointee who now reports on possible wiretapping. CNN… pos 1.0
RT @brhodes: He's lying no matter what "3 people with direct knowledge" say. This isn't he said / he said. Obama did not order a…  pos 1.0
RT @ananavarro: The White House wants to make us believe Trump tweeting without any supporting evidence, qualify as "reports". Nope. https:… pos 1.0
```

## Geolocation Based LIVE Sentiments

![Output a1](figure_1.png?raw=true "Output a1") 
