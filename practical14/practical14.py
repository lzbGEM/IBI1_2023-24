#######################DOM###########################################333
# Import necessary libraries
import datetime
import xml.dom.minidom
import matplotlib.pyplot as plt

# Initialize counters for each ontology category
biological_process = 0
molecular_function = 0
cellular_component = 0

# Record the start time for DOM parsing
start_time = datetime.datetime.now()

# Parse the XML file using DOM and create a DOM tree
DOM_tree = xml.dom.minidom.parse("go_obo.xml")

# Record the end time for DOM parsing
end_time = datetime.datetime.now()

# Calculate the real time taken for DOM parsing
realtime_DOM = end_time - start_time

# Get the document element (root) of the DOM tree
element = DOM_tree.documentElement

# Retrieve all 'term' elements within the document
dic = element.getElementsByTagName('term')

# Loop through each 'term' element
for term in dic:
    if term.getElementsByTagName('namespace')[0].firstChild.nodeValue == "biological_process":
        biological_process += 1
    elif term.getElementsByTagName('namespace')[0].firstChild.nodeValue == "molecular_function":
        molecular_function += 1
    elif term.getElementsByTagName('namespace')[0].firstChild.nodeValue == "cellular_component":
        cellular_component += 1

# Print the counts for each ontology category using DOM
print(f'DOM:term number of biological_process is {biological_process}')
print(f'DOM:term number of molecular_function is {molecular_function}')
print(f'DOM:term number of cellular_component is {cellular_component}')

# Print the time taken for DOM parsing
print(f'DOM time {realtime_DOM}')

# Plot the results using matplotlib
categories = ['biological_process', 'molecular_function', 'cellular_component']
counts = [biological_process, molecular_function, cellular_component]
plt.bar(categories, counts)
plt.show()
plt.clf()






################################SAX#############################################
# Import necessary libraries
import xml.sax

# Define the SAX API handler class
class SAX_API(xml.sax.ContentHandler):#study this method from https://blog.csdn.net/qq_33210042/article/details/117706970
    def __init__(self):
        # Initialize counters and current state variables
       self.biological_process = 0
       self.molecular_function = 0
       self.cellular_component = 0
       self.current_element = ''
       self.namespace = ''

    # Method to process the start of an element
    def startElement(self, a, attributes):
        self.current_element = a

    # Method to process the characters within an element
    def characters(self, content):
        if self.current_element == 'namespace':
            self.namespace += content

    # Method to process the end of an element
    def endElement(self, a):
        if self.current_element == 'namespace':
            if self.namespace == 'molecular_function':
                self.molecular_function += 1
            elif self.namespace == 'biological_process':
                self.biological_process += 1
            elif self.namespace == 'cellular_component':
                self.cellular_component += 1
            self.current_element = ''
            self.namespace = ''

# Create a SAX parser and set the feature to ignore namespaces
parser = xml.sax.make_parser()#come from https://blog.csdn.net/weixin_40970987/article/details/85690592
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# Instantiate the SAX handler
handler = SAX_API()
# Set the content handler to the SAX handler instance
parser.setContentHandler(handler)


start_time = datetime.datetime.now()
parser.parse("go_obo.xml")
end_time = datetime.datetime.now()
realtime_SAX = end_time - start_time

print(f'SAX:term number of biological_process is {handler.biological_process}')
print(f'SAX:term number of molecular_function is {handler.molecular_function}')
print(f'SAX:term number of cellular_component is {handler.cellular_component}')
print(f'SAX time {realtime_SAX}')

# Plot the results using matplotlib
categories = ['biological_process', 'molecular_function', 'cellular_component']
y_counts = [handler.biological_process,handler.molecular_function,handler.cellular_component]
plt.bar(categories, y_counts)
plt.show()
plt.clf()

# Conclusion statement
print("Conclusion: SAX is faster than DOM")


