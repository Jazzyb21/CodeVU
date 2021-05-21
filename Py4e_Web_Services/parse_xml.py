import xml.etree.ElementTree as ET

data = '''
<GeocodeResponse>
    <status>OK</status>
    <result>
        <type>locality</type>
        <type>political</type>
        <formatted_address>Columbia, MO, USA</formatted_address>
        <address_component>
            <long_name>Columbia</long_name>
            <short_name>Columbia</short_name>
            <type>locality</type>
            <type>political</type>
        </address_component>
        <address_component>
            <long_name>Boone County</long_name>
            <short_name>Boone County</short_name>
            <type>administrative_area_level_2</type>
            <type>political</type>
        </address_component>
        <address_component>
            <long_name>Missouri</long_name>
            <short_name>MO</short_name>
            <type>administrative_area_level_1</type>
            <type>political</type>
        </address_component>
        <address_component>
            <long_name>United States</long_name>
            <short_name>US</short_name>
            <type>country</type>
            <type>political</type>
        </address_component>
        <geometry>
            <location>
                <lat>38.9517053</lat>
                <lng>-92.3340724</lng>
            </location>
            <location_type>APPROXIMATE</location_type>
            <viewport>
                <southwest>
                    <lat>38.8635480</lat>
                    <lng>-92.4334839</lng>
                </southwest>
                <northeast>
                    <lat>39.0294400</lat>
                    <lng>-92.2281940</lng>
                </northeast>
            </viewport>
            <bounds>
                <southwest>
                    <lat>38.8635480</lat>
                    <lng>-92.4334839</lng>
                </southwest>
                <northeast>
                    <lat>39.0294400</lat>
                    <lng>-92.2281940</lng>
                </northeast>
            </bounds>
        </geometry>
        <place_id>ChIJyYKBu_Or3IcRIG-9ui1pEaA</place_id>
    </result>
</GeocodeResponse>'''

tree = ET.fromstring(data)

#important to include all parent level elements in the findall statement except for the the top level element
#  or you you wont find any desired nodes
list = tree.findall('result/address_component')
print(list)

for node in list:
    print("Long_Name ", node.find('long_name').text)
    print("Short_Name ", node.find('short_name').text)
    print("Type ", node.find('type').text)

    