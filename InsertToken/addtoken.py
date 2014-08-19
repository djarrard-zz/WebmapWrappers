import arcpy, json, string, urllib2, urllib

def defineEndpoints(agsURL):
    base = agsURL.split(r"/rest")[0]
    REST = base + "/rest/services"
    adminAPI = base + "/admin"
    info = base + "/rest/info" 
    endpoint_request = urllib2.Request(url=info + "?f=json")
    endpoint_response = urllib2.urlopen(endpoint_request)
    endpoint_string = endpoint_response.read()
    endpoint_obj = json.loads(endpoint_string)
    tokenURL = endpoint_obj["authInfo"]["tokenServicesUrl"]
    output = {"REST":REST,"TokenUrl":tokenURL,"Admin":adminAPI}
    return output

inputJSON = arcpy.GetParameterAsText(0)
server = arcpy.GetParameterAsText(1)
userName = arcpy.GetParameterAsText(2)
userPassword = arcpy.GetParameterAsText(3)

#Import JSON as an dictionary object in python
jsonObject = json.loads(inputJSON)

# Class to capture cookie in http redirects
class MyHTTPRedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        return urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)

    http_error_301 = http_error_303 = http_error_307 = http_error_302

# Get Token
endpoints = defineEndpoints(server)
token_URL = endpoints['TokenUrl']
token_POSTdata = {'username':userName,'password':userPassword, 'f':'json'}
token_request = urllib2.Request(url=token_URL,data = urllib.urlencode(token_POSTdata))
token_response = urllib2.urlopen(token_request)
token_string = token_response.read()
token_obj = json.loads(token_string)
token = token_obj['token']

#Find and replace service URLs that currently reference a specific external path
if "http:" in server:
            protocol = "http://"
elif "https:" in server:
            protocol = "https://"
serverBaseUrl = server.split(protocol)[1]

for service in jsonObject['operationalLayers']:
    if 'url' in service:
        if "http:" in service['url']:
            protocol = "http://"
        elif "https:" in service['url']:
            protocol = "https://"
        serviceBaseUrl = service['url'].split(protocol)[1]
        if serverBaseUrl in serviceBaseUrl:
            newURL = service['url'] + "?" + "token=" + token
            service['url'] = newURL

if 'baseMap' in jsonObject:
    for service in jsonObject['baseMap']['baseMapLayers']:
        if 'url' in service:
            if "http:" in service['url']:
                protocol = "http://"
            elif "https:" in service['url']:
                protocol = "https://"
            serviceBaseUrl = service['url'].split(protocol)[1]
            arcpy.AddMessage(service['url'])
            if serviceBaseUrl in serverBaseUrl:
                newURL = service['url'] + "?" + "token=" + token
                service['url'] = newURL

#Encode updated dictionary back to JSON format
correctedJSON = str(json.JSONEncoder().encode(jsonObject))

arcpy.SetParameterAsText(4,correctedJSON)
