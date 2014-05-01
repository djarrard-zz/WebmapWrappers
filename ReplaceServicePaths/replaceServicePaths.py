import arcpy, json, string

inputJSON = arcpy.GetParameterAsText(0)
findPath = arcpy.GetParameterAsText(1)
replacePath = arcpy.GetParameterAsText(2)

#Import JSON as an dictionary object in python
jsonObject = json.loads(inputJSON)

#Find and replace service URLs that currently reference a specific external path
for service in jsonObject['operationalLayers']:
    if 'url' in service:
        arcpy.AddMessage(service['url'])
        if findPath in service['url']:
            newURL = service['url'].replace(findPath,replacePath)
            service['url'] = newURL

if 'baseMap' in jsonObject:
    for service in jsonObject['baseMap']['baseMapLayers']:
        if 'url' in service:
            arcpy.AddMessage(service['url'])
            if findPath in service['url']:
                newURL = service['url'].replace(findPath,replacePath)
                service['url'] = newURL

#Encode updated dictionary back to JSON format
correctedJSON = str(json.JSONEncoder().encode(jsonObject))

arcpy.SetParameterAsText(3,correctedJSON)
