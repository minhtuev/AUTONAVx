import numpy as np

def compute_means(lat,lon,alt):
    # TODO: implement mean computation
    mean_lat = np.mean(np.array(lat))
    mean_lon = np.mean(np.array(lon))
    mean_alt = np.mean(np.array(alt))
    return (mean_lat,mean_lon,mean_alt)

def compute_vars(lat,lon,alt):
    # TODO: implement variance computation
    N = len(lat)
    var_lat = np.var(np.array(lat))*N/(N-1)
    var_lon = np.var(np.array(lon))*N/(N-1)
    var_alt = np.var(np.array(alt))*N/(N-1)
    return (var_lat,var_lon,var_alt)

def compute_cov(lat,lon,alt):
    # TODO: implement covariance computation
    lat = np.array(lat)
    lon = np.array(lon)
    alt = np.array(alt)
    cov_lat_lon = np.cov(lat, lon)
    cov_lon_alt = np.cov(lon, alt)
    cov_lat_alt = np.cov(lat, alt)
    return (cov_lat_lon,cov_lon_alt,cov_lat_alt)