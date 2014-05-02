Insert Token
============

The purpose of this tool is to pre-process webmap JSON service references prior to sending the request to a print task. Within this context, the desire is to append tokens to services residing on a specified server. The documented solution to this scenario is outlined in the following Help Document provided by Esri. 

Printing maps that contain secured services 
http://resources.arcgis.com/en/help/main/10.1/index.html#//0154000005q3000000

However, due to a bug, specific layer references in the webmap JSON will not get a token.

*[#NIM094431 A custom print service with saved credentials created from the Export Web Map task fails to print individual feature layers from a secured map service. ]*

**Check to make sure the workflow provided by Esri will not work before proceeding**. This sample was designed as a workaround to the bug mentioned above.

Contents
----------------------

**addtoken.py** - The script that executes the WebMap JSON preprocessing. It is configured as a Script Tool and works with the Insert Token to Webmap JSON tool in the Toolbox.tbx object

**Insert Token to Webmap JSON (in Toolbox.tbx)** - A Python script tool that takes Webmap JSON as input, modifies it, and returns the modified JSON as output.

**Export Web Map (in Toolbox.tbx)** - A copy of the Export Web Map tool in the Server toolbox from ArcGIS Desktop. This tool takes webmap JSON as input and exports a map in a selected format. Can also export a map from Map Document templates.

**CustomPrint (in Toolbox.tbx)** - Model that combines Replace Service Paths and Export Web Map into a single process. After running, this can be published as a print service.

**Templates folder** - Folder containing the default Map Document templates included in the stock print service provided with ArcGIS Server.

Instructions
----------------------

1) Download and extract the package
2) In ArcCatalog, browse to WebmapWrappers > InsertToken.tbx
3) Right-click > edit CustomPrint.
4) Double-click on the Insert Token to Webmap JSON tool in the model.
5) Edit the Server, Username, and Password credentials to match the ArcGIS Server you wish to get a token from. Click OK.
6) Save the model and close ModelBuilder.
7) Double-click on the CustomPrint Model to open the dialogue.
8) Change the Input JSON as appropriate. Click OK.
9) If it runs successfully, this can be published as a Geoprocessing Service

*Notes*
- The Insert Token to Webmap script tool is only designed to get a token and append it service references from one server. The CustomPrint model can be customized to daisy-chain multiple iterations of the Insert Token tool for multiple servers if desired.

- The templates folder is included as a reference. You can of course use your own custom templates if desired.