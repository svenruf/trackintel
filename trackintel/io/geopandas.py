import geopandas as gpd
import pandas as pd

def read_positionfixes_gpd(gdf, tracked_at='tracked_at', user_id='user_id', geom='geom', mapper={}):
    """
    warps the pd.rename function to simplify the import of GeoDataFrames

    Parameters
    ----------
    gdf : GeoDataFrame with valid point geometry, containing the positionfixes to import
    tracked_at : str, name of the column storing the timestamps. The default is 'tracked_at'.
    user_id : str, name of the column storing the user_id. The default is 'user_id'.
    geom : str, name of the column storing the geometry. The default is 'geom'.
    mapper : dict, further columns that should be renamed. 

    Returns
    -------
    gdf : a validated positionfixes GeoDataFrame

    """
  
    
    columns = {tracked_at:'tracked_at', 
               user_id:'user_id',
               geom:'geom'}
    columns.update(mapper)
    
    pfs = gdf.rename(columns=columns)
    
    assert pfs.as_positionfixes
    

    return pfs

def read_staypoints_gpd(gdf, started_at='started_at', finished_at='finished_at', user_id='user_id', geom='geom', mapper={}):
    """
    warps the pd.rename function to simplify the import of GeoDataFrames

    Parameters
    ----------
    gdf : GeoDataFrame with valid point geometry, containing the staypoints to import
    started_at : str, name of the column storing the starttime of the staypoints. The default is 'started_at'.
    finished_at : str, name of the column storing the endtime of the staypoints. The default is 'finished_at'.
    user_id : str, name of the column storing the user_id. The default is 'user_id'.
    geom : str, name of the column storing the geometry. The default is 'geom'.
    mapper : dict, further columns that should be renamed. 

    Returns
    -------
    gdf : a validated staypoints GeoDataFrame

    """
  
    
    columns = {started_at:'tracked_at',
               finished_at:'finished_at',
               user_id:'user_id',
               geom:'geom'}
    columns.update(mapper)
    
    stp = gdf.rename(columns=columns)
    
    assert stp.as_staypoints
    

    return stp

def read_triplegs_gpd(gdf, started_at='started_at', finished_at='finished_at', user_id='user_id', geom='geom', mapper={}):
    """
    warps the pd.rename function to simplify the import of GeoDataFrames

    Parameters
    ----------
    gdf : GeoDataFrame with valid line geometry, containing the triplegs to import
    started_at : str, name of the column storing the starttime of the triplegs. The default is 'started_at'.
    finished_at : str, name of the column storing the endtime of the triplegs. The default is 'finished_at'.
    user_id : str, name of the column storing the user_id. The default is 'user_id'.
    geom : str, name of the column storing the geometry. The default is 'geom'.
    mapper : dict, further columns that should be renamed. 

    Returns
    -------
    gdf : a validated triplegs GeoDataFrame

    """
  
    
    columns = {started_at:'tracked_at',
               finished_at:'finished_at',
               user_id:'user_id',
               geom:'geom'}
    columns.update(mapper)
    
    tpl = gdf.rename(columns=columns)
    
    assert tpl.as_triplegs
    

    return tpl

def read_trips_gpd(gdf, started_at='started_at', finished_at='finished_at', user_id='user_id', origin_staypoint_id='origin_staypoint_id', destination_staypoint_id='destination_staypoint_id', geom='geom', mapper={}):
    """
    warps the pd.rename function to simplify the import of GeoDataFrames

    Parameters
    ----------
    gdf : GeoDataFrame with valid geometry, containing the trips to import
    started_at : str, name of the column storing the starttime of the staypoints. The default is 'started_at'.
    finished_at : str, name of the column storing the endtime of the staypoints. The default is 'finished_at'.
    user_id : str, name of the column storing the user_id. The default is 'user_id'.
    origin_staypoint_id : str, name of the column storing the staypoint_id of the start of the tripleg
    destination_staypoint_id : str, name of the column storing the staypoint_id of the end of the tripleg
    geom : str, name of the column storing the geometry. The default is 'geom'.
    mapper : dict, further columns that should be renamed. 

    Returns
    -------
    gdf : a validated trips GeoDataFrame

    """
  
    
    columns = {started_at:'tracked_at',
               finished_at:'finished_at',
               user_id:'user_id',
               geom:'geom'}
    columns.update(mapper)
    
    tps = gdf.rename(columns=columns)
    
    assert tps.as_trips
    

    return tps

def read_locations_gpd(gdf, user_id='user_id', center='center', mapper={}):
    """
    warps the pd.rename function to simplify the import of GeoDataFrames

    Parameters
    ----------
    gdf : GeoDataFrame with valid point geometry, containing the locations to import
    user_id : str, name of the column storing the user_id. The default is 'user_id'.
    center : str, name of the column storing the geometry (Center of the location). The default is 'center'.
    mapper : dict, further columns that should be renamed. 

    Returns
    -------
    gdf : a validated locations GeoDataFrame

    """
  
    
    columns = {user_id:'user_id',
               center:'center'}
    columns.update(mapper)
    
    lcs = gdf.rename(columns=columns)
    
    assert lcs.as_locations
    

    return lcs

def read_tours_gpd(gdf, user_id='user_id',started_at='started_at', finished_at='finished_at', origin_destination_location_id='origin_destination_location_id', journey='journey', mapper={}):
    """
    warps the pd.rename function to simplify the import of GeoDataFrames

    Parameters
    ----------
    gdf : GeoDataFrame with valid point geometry, containing the locations to import
    user_id : str, name of the column storing the user_id. The default is 'user_id'.
    started_at : str, name of the column storing the starttime of the staypoints. The default is 'started_at'.
    finished_at : str, name of the column storing the endtime of the staypoints. The default is 'finished_at'.
    origin_destination_location_id : the name of the column storing the id of the location where the tour starts and ends. The default is 'origin_destination_location_id'.
    journey : str, name of the column storing the information (bool) if the tour is a journey. The default is 'journey'.
    mapper : dict, further columns that should be renamed. 

    Returns
    -------
    gdf : a validated locations GeoDataFrame

    """
  
    
    columns = {user_id:'user_id',
               started_at:'tracked_at',
               finished_at:'finished_at',
               origin_destination_location_id:'origin_destination_location_id',
               journey:'journey'}
    columns.update(mapper)
    
    trs = gdf.rename(columns=columns)
    
    assert trs.as_tours
    

    return trs