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
terms = element.getElementsByTagName('term')

# Loop through each 'term' element
for term in terms:
    # Find the 'namespace' child element and get its value
    name = term.getElementsByTagName('namespace')[0].firstChild.nodeValue
    
    # Increment the appropriate counter based on the namespace value
    if name == "biological_process":
        biological_process += 1
    elif name == "molecular_function":
        molecular_function += 1
    elif name == "cellular_component":
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
        self.count = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
        self.current_element = ''
        self.namespace = ''

    # Method to process the start of an element
    def startElement(self, name, attributes):
        self.current_element = name

    # Method to process the characters within an element
    def characters(self, content):
        if self.current_element == 'namespace':
            self.namespace += content

    # Method to process the end of an element
    def endElement(self, name):
        if self.current_element == 'namespace':
            # Increment the appropriate counter based on the namespace value
            if self.namespace in self.count:
                self.count[self.namespace] += 1
            # Reset the current_element and namespace
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

print(f'SAX:term number of biological_process is {handler.count["biological_process"]}')
print(f'SAX:term number of molecular_function is {handler.count["molecular_function"]}')
print(f'SAX:term number of cellular_component is {handler.count["cellular_component"]}')
print(f'SAX time {realtime_SAX}')

# Plot the results using matplotlib
categories = ['biological_process', 'molecular_function', 'cellular_component']
y_counts = [handler.count[category] for category in categories]
plt.bar(categories, y_counts)
plt.show()
plt.clf()

# Conclusion statement
print("Conclusion: SAX is faster than DOM")


