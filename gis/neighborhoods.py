import shapefile
from shapely import Polygon

SHP_PATH = "neighborhoods_wgs84.shp"
neighborhoods = {}

with shapefile.Reader(SHP_PATH) as sf:
    for shape_rec in sf.shapeRecords():
        # shape_rec.shape.points - list of WKT points, used to construct
        #                             a shapely.Polygon
        # We are assuming Polygon here! If this file had points/lines/etc.
        # changes would be needed.
        polygon = Polygon(shape_rec.shape.points)
        # shape_rec.record contains the attributes as a list or dictionary
        # in this file record[0] contains the neighborhood name
        name = shape_rec.record[0]
        # associate polygon with name
        neighborhoods[name] = polygon


from shapely import Point

museums = [
    ("Field Museum", Point(-87.6169, 41.8663)),
    ("Art Institute of Chicago", Point(-87.6237, 41.8796)),
    ("Museum of Science and Industry", Point(-87.5830, 41.7906)),
    ("The Metropolitan Museum of Art", Point(-73.9632, 40.7794)),
]

for museum, museum_point in museums:
    for neighborhood, poly in neighborhoods.items():
        if poly.contains(museum_point):
            print(museum, "is in", neighborhood)
            break
    else:
        # for-else only executes if no break did
        print(museum, "is not in Chicago!")
