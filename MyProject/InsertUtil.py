import random
import sys
from multiprocessing import Pool
from pip._vendor import requests
import time
import json

wines = [
  {
    "name": "CHATEAU DE SAINT COSME",
    "year": "2009",
    "grapes": "Grenache / Syrah",
    "country": "France",
    "region": "Southern Rhone",
    "description": "The aromas of fruit and spice giises.",
    "picture": "saint_cosme.jpg"
  },
  {
    "name": "LAN RIOJA CRIANZA",
    "year": "2006",
    "grapes": "Tempranillo",
    "country": "Spain",
    "region": "Rioja",
    "description": "A resurge not fail to tickle the taste buds.",
    "picture": "lan_rioja.jpg"
  },
  {
    "name": "MARGERUM SYBARITE",
    "year": "2010",
    "grapes": "Sauvignon Blanc",
    "country": "USA",
    "region": "California Central Cosat",
    "description": "The cache of a fie sure to transport you back in time.",
    "picture": "margerum.jpg"
  },
  {
    "name": "OWEN ROE \"EX UMBRIS\"",
    "year": "2009",
    "grapes": "Syrah",
    "country": "USA",
    "region": "Washington",
    "description": "A one-two puation.",
    "picture": "ex_umbris.jpg"
  },
  {
    "name": "REX HILL",
    "year": "2009",
    "grapes": "Pinot Noir",
    "country": "USA",
    "region": "Oregon",
    "description": "One cannot doubt tabout tomorrow.",
    "picture": "rex_hill.jpg"
  },
  {
    "name": "VITICCIO CLASSICO RISERVA",
    "year": "2007",
    "grapes": "Sangiovese Merlot",
    "country": "Italy",
    "region": "Tuscany",
    "description": "Though soft andhat leave the taste buds wholly satisfied.",
    "picture": "viticcio.jpg"
  },
  {
    "name": "CHATEAU LE DOYENNE",
    "year": "2005",
    "grapes": "Merlot",
    "country": "France",
    "region": "Bordeaux",
    "description": "Though dense and chewy, this wine does not overpower with its finely balanced depth and structure. It is a truly luxurious experience for the senses.",
    "picture": "le_doyenne.jpg"
  },
  {
    "name": "DOMAINE DU BOUSCAT",
    "year": "2009",
    "grapes": "Merlot",
    "country": "France",
    "region": "Bordeaux",
    "description": "The light golden color of this wine belies the bright flavor it holds. A true summer wine, it begs for a picnic lunch in a sun-soaked vineyard.",
    "picture": "bouscat.jpg"
  },
  {
    "name": "BLOCK NINE",
    "year": "2009",
    "grapes": "Pinot Noir",
    "country": "USA",
    "region": "California",
    "description": "With hints of ginger and spice, this wine makes an excellent complement to light appetizer and dessert fare for a holiday gathering.",
    "picture": "block_nine.jpg"
  },
  {
    "name": "DOMAINE SERENE",
    "year": "2007",
    "grapes": "Pinot Noir",
    "country": "USA",
    "region": "Oregon",
    "description": "Though subtle in its complexities, this wine is sure to please a wide range of enthusiasts. Notes of pomegranate will delight as the nutty finish completes the picture of a fine sipping experience.",
    "picture": "domaine_serene.jpg"
  },
  {
    "name": "BODEGA LURTON",
    "year": "2011",
    "grapes": "Pinot Gris",
    "country": "Argentina",
    "region": "Mendoza",
    "description": "Solid notes of black currant blended with a light citrus make this wine an easy pour for varied palates.",
    "picture": "bodega_lurton.jpg"
  },
  {
    "name": "LES MORIZOTTES",
    "year": "2009",
    "grapes": "Chardonnay",
    "country": "France",
    "region": "Burgundy",
    "description": "Breaking the mold of the classics, this offering will surprise and undoubtedly get tongues wagging with the hints of coffee and tobacco in perfect alignment with more traditional notes. Sure to please the late-night crowd with the slight jolt of adrenaline it brings.",
    "picture": "morizottes.jpg"
  },
  {
    "name": "ARGIANO NON CONFUNDITUR",
    "year": "2009",
    "grapes": "Cabernet Sauvignon",
    "country": "Italy",
    "region": "Tuscany",
    "description": "Like a symphony, this cabernet has a wide range of notes that will delight the taste buds and linger in the mind.",
    "picture": "argiano.jpg"
  },
  {
    "name": "DINASTIA VIVANCO ",
    "year": "2008",
    "grapes": "Tempranillo",
    "country": "Spain",
    "region": "Rioja",
    "description": "Whether enjoying a fine cigar or a nicotine patch, don't pass up a taste of this hearty Rioja, both smooth and robust.",
    "picture": "dinastia.jpg"
  },
  {
    "name": "PETALOS BIERZO",
    "year": "2009",
    "grapes": "Mencia",
    "country": "Spain",
    "region": "Castilla y Leon",
    "description": "For the first time, a blend of grapes from two different regions have been combined in an outrageous explosion of flavor that cannot be missed.",
    "picture": "petalos.jpg"
  },
  {
    "name": "SHAFER RED SHOULDER RANCH",
    "year": "2009",
    "grapes": "Chardonnay",
    "country": "USA",
    "region": "California",
    "description": "Keep an eye out for this winery in coming years, as their chardonnays have reached the peak of perfection.",
    "picture": "shafer.jpg"
  },
  {
    "name": "PONZI",
    "year": "2010",
    "grapes": "Pinot Gris",
    "country": "USA",
    "region": "Oregon",
    "description": "For those who appreciate the simpler pleasures in life, this light pinot grigio will blend perfectly with a light meal or as an after dinner drink.",
    "picture": "ponzi.jpg"
  },
  {
    "name": "HUGEL",
    "year": "2010",
    "grapes": "Pinot Gris",
    "country": "France",
    "region": "Alsace",
    "description": "Fresh as new buds on a spring vine, this dewy offering is the finest of the new generation of pinot grigios.  Enjoy it with a friend and a crown of flowers for the ultimate wine tasting experience.",
    "picture": "hugel.jpg"
  },
  {
    "name": "FOUR VINES MAVERICK",
    "year": "2011",
    "grapes": "Zinfandel",
    "country": "USA",
    "region": "California",
    "description": "o yourself a favor and have a bottle (or two) of this fine zinfandel on hand for your next romantic outing.  The only thing that can make this fine choice better is the company you share it with.",
    "picture": "fourvines.jpg"
  },
  {
    "name": "QUIVIRA DRY CREEK VALLEY",
    "year": "2009",
    "grapes": "Zinfandel",
    "country": "USA",
    "region": "California",
    "description": "Rarely do you find a zinfandel this oakey from the Sonoma region. The vintners have gone to extremes to duplicate the classic flavors that brought high praise in the early '90s.",
    "picture": "quivira.jpg"
  },
  {
    "name": "CALERA 35TH ANNIVERSARY",
    "year": "2010",
    "grapes": "Pinot Noir",
    "country": "USA",
    "region": "California",
    "description": "Fruity and bouncy, with a hint of spice, this pinot noir is an excellent candidate for best newcomer from Napa this year.",
    "picture": "calera.jpg"
  },
  {
    "name": "CHATEAU CARONNE STE GEMME",
    "year": "2010",
    "grapes": "Cabernet Sauvignon",
    "country": "France",
    "region": "Bordeaux",
    "description": "Find a sommelier with a taste for chocolate and he's guaranteed to have this cabernet on his must-have list.",
    "picture": "caronne.jpg"
  },
  {
    "name": "MOMO MARLBOROUGH",
    "year": "2010",
    "grapes": "Sauvignon Blanc",
    "country": "New Zealand",
    "region": "South Island",
    "description": "Best served chilled with melon or a nice salty prosciutto, this sauvignon blanc is a staple in every Italian kitchen, if not on their wine list.  Request the best, and you just may get it.",
    "picture": "momo.jpg"
  },
  {
    "name": "WATERBROOK",
    "year": "2009",
    "grapes": "Merlot",
    "country": "USA",
    "region": "Washington",
    "description": "Legend has it the gods didn't share their ambrosia with mere mortals.  This merlot may be the closest we've ever come to a taste of heaven.",
    "picture": "waterbrook.jpg"
  }
]
def insertQuery(wine):
    r = requests.post("http://193.106.55.134:3004/wines", data=wine)
    print("insert return: ",r.status_code, r.reason)
# #RUN
print("Start")
for i in range (0,23):
  insertQuery(wines[i])
print("Finish")
# insertQuery(wines[0])
