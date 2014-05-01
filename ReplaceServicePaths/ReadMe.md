REPLACE SERVICE PATHS

The purpose of this tool is to pre-process webmap JSON service references prior to sending the request to a print task. Within this context, the desire is to switch external path references with internal ones, though any scriptable JSON modification can be made here.

replaceservicePaths.py - The script that executes the WebMap JSON preprocessing. It is configured as a Script Tool and works with the Replace Service Paths tool in the Toolbox.tbx object

Replace Service Paths (in Toolbox.tbx) - A Python script tool that takes Webmap JSON as input, modifies it, and returns the modified JSON as output.

Export Web Map (in Toolbox.tbx) - A copy of the Export Web Map tool in the Server toolbox from ArcGIS Desktop. This tool takes webmap JSON as input and exports a map in a selected format. Can also export a map from Map Document templates.

CustomPrint (in Toolbox.tbx) - Model that combines Replace Service Paths and Export Web Map into a single process. After running, this can be published as a print service.

Templates folder - Folder containing the default Map Document templates included in the stock print service provided with ArcGIS Server.

