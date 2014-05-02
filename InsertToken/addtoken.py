import arcpy, json, string, urllib2, urllib

inputJSON = arcpy.GetParameterAsText(0)

#Import JSON as an dictionary object in python
jsonObject = json.loads(inputJSON)

server = arcpy.GetParameterAsText(1)
userName = arcpy.GetParameterAsText(2)
userPassword = arcpy.GetParameterAsText(3)
# Class to capture cookie in http redirects
class MyHTTPRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        return urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)

    http_error_301 = http_error_303 = http_error_307 = http_error_302

# Get Token
token_URL = server + "/tokens/generateToken"
token_POSTdata = {'username':userName,'password':userPassword, 'f':'json'}
token_request = urllib2.Request(url=token_URL,data = urllib.urlencode(token_POSTdata))
token_response = urllib2.urlopen(token_request)
token_string = token_response.read()
token_obj = json.loads(token_string)
token = token_obj['token']

#Find and replace service URLs that currently reference a specific external path
for service in jsonObject['operationalLayers']:
    if 'url' in service:
        arcpy.AddMessage(service['url'])
        if server in service['url']:
            newURL = service['url'] + "?" + "token=" + token
            service['url'] = newURL

if 'baseMap' in jsonObject:
    for service in jsonObject['baseMap']['baseMapLayers']:
        if 'url' in service:
            arcpy.AddMessage(service['url'])
            if server in service['url']:
                newURL = service['url'] + "?" + "token=" + token
                service['url'] = newURL

#Encode updated dictionary back to JSON format
correctedJSON = str(json.JSONEncoder().encode(jsonObject))

arcpy.SetParameterAsText(4,correctedJSON)
