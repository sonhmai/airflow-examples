CREATE_TRIPS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS trips (
    trip_id INTEGER not null,
    start_time timestamp not null,
    end_time timestamp not null,
    bikeid integer not null,
    tripduration decimal(16,2) not null,
    from_station_id integer not null,
    from_station_name varchar(100) not null,
    to_station_id integer not null,
    to_station_name varchar(100) not null,
    usertype varchar(20),
    gender varchar(6),
    birthyear integer,
    primary key(trip_id)
)
DISTSTYLE ALL;
"""

LOCATION_TRAFFIC_SQL = """
BEGIN;
DROP TABLE IF EXISTS station_traffic;
CREATE TABLE station_traffic AS
SELECT
    DISTINCT(t.from_station_id) AS station_id,
    t.from_station_name AS station_name,
    num_departures,
    num_arrivals
FROM trips t
JOIN (
    SELECT
        from_station_id,
        COUNT(from_station_id) AS num_departures
    FROM trips
    GROUP BY from_station_id
) AS fs ON t.from_station_id = fs.from_station_id
JOIN (
    SELECT
        to_station_id,
        COUNT(to_station_id) AS num_arrivals
    FROM trips
    GROUP BY to_station_id
) AS ts ON t.from_station_id = ts.to_station_id
"""