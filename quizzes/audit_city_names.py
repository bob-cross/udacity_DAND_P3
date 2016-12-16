import xml.etree.cElementTree as ET
import pprint

#audit way tags for unexpected city names in Austin map

osmfile = "sample.osm"

expected = ("Austin", "Pflugerville", "Round Rock")

def is_city_name(elem):
    return (elem.attrib['k'] =="addr:city")

def audit_city(osmfile):
     city_file = open(osmfile, "r")
     for event, elem in ET.iterparse(city_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == 'addr:city':
                    city = tag.attrib['v'].strip()
                    if city not in expected: 
                        print city
                        
                         
     city_file.close()

audit_city("sample.osm")

#audit of sample file shows names which appear to be outside of what would be considered Austin (eg Buda > 60mi away)
#this would require edit specific entries; these can be ignore for analysis purposes in most cases with no material effect