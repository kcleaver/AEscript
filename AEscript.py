import sys,re,os

locales = ["de", "es", "fr", "it", "ja", "pl", "zh"] 
  # array for all possible translations file you might need, can also add de_AT but file name will need to match example: de_AT.txt
  # the entries will need to match exactly with the file names
original_data = "data"
  # name (before prefix) of the original data file
original_translation = "en.txt"
  # Original set of English Strings to be translated, get by running <string>.* expression in sublime or any text editor, require back translations in lang.txt format.


def dowork(src, dest, orig, trans):
  f = open(src)
  g = open(orig)
  if os.path.exists(trans): #to make sure that the translations exist
    h = open(trans)
  else:
    print(trans + " This asset does not exist, mother-F-er")
    return # fall out and move on to the next array entry
  source = f.readlines() #read lines into an array
  before = g.readlines() #that can be accessed by doing NAME[#] (eg. source[123]) for a line
  after = h.readlines()
  f.close()
  g.close()
  h.close() #should get closed automagically, good to do this anywaay

  output = open(dest, 'w')  # open with the 'w' argument to make a new file if it doesn't exist
  for line in source:
    for index, entry in enumerate(before):
      #for every line in before[]: index is the line num and entry is the actual string
      line = line.replace(entry, after[index])
      # search every line for each possible string and if found replace it with the matching index
      # this means you'll only replace before[3] with after[3] etc.
    output.write(line) #output every line, whether a change has been made or not
  output.close()
  return

#actual body of work is done here for each potential translation, make a new result file
for geo in locales:
  dowork( original_data+".aepx", original_data+"_"+geo+".aepx", original_translation, geo+".txt")
  # eg will send something like ("data.aepx", "data_fr.aepx", "en.txt", "fr.txt")
  # RUN python AEscript.py data.aepx de.txt es.txt fr.txt it.txt and any other geos needed for translations
