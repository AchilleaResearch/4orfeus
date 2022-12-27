import pandas as pd
import numpy as np
from contproc.models import busCoordinates

def prepare_map(id:busCoordinates.pk):
    df1 = pd.read_csv(busCoordinates.objects.get(pk=id).file)
    varr = df1[df1['Vnom']>=69]['Vnom'].unique()
    data = []
    for v in varr:
        df1a = df1[df1['Vnom']==v]
        datav = {
            'name': '%g' %v,
            'type': 'scattermapbox',
            'lat': df1a['Lat'].to_list(),
            'lon': df1a['Lon'].to_list(),
            'marker': {
                'size': np.sqrt(df1a['Vnom'].to_numpy()).tolist(),
                # 'color': 'fuchsia',
            },
            'text': df1a['SubName'].to_list(),
        }
        data.append(datav)
    layout = {
        'dragmode': "zoom",
        'mapbox': {
		    'style': "white-bg",
		    'layers': [
			    {
				'sourcetype': "raster",
				'source': ["https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"],
				'below': "traces",
			    }
    		],
		    'center': { 'lat': df1['Lat'].mean(), 'lon': df1['Lon'].mean() },
		    'zoom': 5.5,
	    },
        'margin': { 'r': 0, 't': 30, 'b': 0, 'l': 0 },
        'height': 800,
	}
    config = {'responsive': True}

    return {'data': data, 'layout': layout, 'config':config}