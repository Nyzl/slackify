#built on the brilliant work by Adam J Calhourn from his post
#https://medium.com/@neuroecology/punctuation-in-novels-8f316d542ec4#.tz6i4h1ub

import app
import string
import json
from urllib.request import urlopen
import re


#set variables
title = "not"
wcount = "0"

def ithaca (urls):

   global wcount
   global title

# pixel border width
   trim = 100;
   font1size = 75;


#web scrape
   var = urls
   page = urlopen(var).read()

   soup = bs(page,'html.parser')
   title = soup.title.string
   title = title.strip()

   [s.extract() for s in soup('script')]

   try:
      txt = soup.find("div",{"class":re.compile(".*(article(.?body|content)|story-body).*", flags=re.IGNORECASE)})
      txt = txt.get_text()

   except AttributeError:
      try:
         txt = soup.find("div",{"itemprop":re.compile(".*(article(.?body|content)|story-body).*", flags=re.IGNORECASE)})
         txt = txt.get_text()

      except:
         txt = soup.find("body")
         txt = txt.get_text()

   include = set(string.punctuation)

   def getPunctuation(s):
      return ''.join(ch for ch in s if ch in include)

   punct = getPunctuation(txt);

# number of symbols to be output on each line
# and the number of lines

   size = int(math.floor(math.sqrt(len(punct))))

   symbolsPerLine = size
   linesOfText = size

   canvasHeight = size * 100
   canvasWidth = size * 100

   deltaW = (canvasWidth - trim*2)/symbolsPerLine
   deltaH = (canvasHeight - trim*2)/linesOfText

   bkgColor = (255,255,255)

   img = Image.new("RGB", [canvasWidth,canvasHeight], bkgColor)
   draw = ImageDraw.Draw(img)
# font from (SEE LICENSE!): http://www.fontsquirrel.com/fonts/glacial-indifference
   font1 = ImageFont.truetype(".fonts/GlacialIndifference-Bold.otf", font1size)



# in case you want to change by transition
   optionalFill = (0,0,0);


# getTextSize
   for ii in range(linesOfText):
      for jj in range(symbolsPerLine):
         symb = punct[jj + ii*symbolsPerLine]
         if (symb == '.'):
            draw.text((trim + jj*deltaW,trim + ii*deltaH - round(font1size/4)), symb,fill=optionalFill,font=font1)
         elif (symb == ','):
            draw.text((trim + jj*deltaW,trim + ii*deltaH - round(font1size/4)), symb,fill=optionalFill,font=font1)
         elif (symb == '!') or (symb == '?'):
            draw.text((trim + jj*deltaW,trim + ii*deltaH), symb,fill=optionalFill,font=font1)
         elif (symb == '"') or (symb == '\'') or (symb == '(') or (symb == ')') or (symb == '[') or (symb == ']'):
            draw.text((trim + jj*deltaW,trim + ii*deltaH), symb,fill=optionalFill,font=font1)
         elif (symb == ';') or (symb == '-') or (symb == ':'):
            draw.text((trim + jj*deltaW,trim + ii*deltaH), symb,fill=optionalFill,font=font1)
         else:
            draw.text((trim + jj*deltaW,trim + ii*deltaH), symb,fill=optionalFill,font=font1)

   img.save("static/" + title + '.png')

   wcount=(len(punct))

   return wcount
   return title


if __name__ == "__main__":
    ithaca.run()
