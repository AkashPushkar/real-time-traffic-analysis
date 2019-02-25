# Real-time Traffic Analysis and Visualization
This is real-time traffic visualization project done for the city of Ann Arbor, Michigan

## Data Description ##
Data used is found [here](https://data.transportation.gov/Automobiles/Safety-Pilot-Model-Deployment-Data/a7qq-9vfe). Data despcription is as follows (https://data.transportation.gov/Automobiles/Safety-Pilot-Model-Deployment-Data/a7qq-9vfe/data?pane=manage)

| Field Name     | Type    | Units        | Description                                                                                                                            |
|----------------|---------|--------------|----------------------------------------------------------------------------------------------------------------------------------------|
| Device         | Integer | none         | A unique numeric ID assigned to each DAS. This ID also doubles as a vehicle’s ID                                                       |
| Trip           | Integer | none         | Count of ignition cycles—each ignition cycle commences when the ignition is in the on position and ends when it is in the off position |
| Time           | Integer | centiseconds | Time in centiseconds since DAS started, which (generally) starts when the ignition is in the on position                               |
| GpsValidWsu    | Integer | none         | Communicates whether a GPS data point is valid or not                                                                                  |
| GpsTimeWsu     | Integer | millisecond  | Epoch GPS time received from the remote vehicle that has been targeted by the host vehicle’s WSU                                       |
| LatitudeWsu    | Float   | deg          | Latitude from WSU receiver                                                                                                             |
| LongitudeWsu   | Float   | deg          | Longitude from WSU receiver                                                                                                            |
| AltitudeWsu    | Real    | m            | Altitude from WSU receiver                                                                                                             |
| GpsHeadingWsu  | Real    | deg          | Heading from WSU GPS receiver                                                                                                          |
| GpsSpeedWsu    | Real    | m/sec        | Speed from WSU GPS receiver                                                                                                            |
| HdopWsu        | Real    | none         | Horizontal dilution of precision                                                                                                       |
| PdopWsu        | Real    | none         | Position dilution of precision                                                                                                         |
| FixQualityWsu  | Integer | none         | GPS Fix Quality                                                                                                                        |
| GpsCoastingWsu | Integer | none         | GPS Coasted                                                                                                                            |
| ValidCanWsu    | Integer | none         | Valid Vehicle CAN Bus message to WSU                                                                                                   |
| YawRateWsu     | Real    | deg/sec      | Yaw rate from vehicle CAN Bus via WSU                                                                                                  |
| SpeedWsu       | Real    | kph          | Speed from vehicle CAN Bus via WSU                                                                                                     |
| TurnSngRWsu    | Integer | none         | Right turn signal from vehicle CAN Bus via WSU                                                                                         |
| TurnSngLWsu    | Integer | none         | Left turn signal from vehicle CAN Bus via WSU                                                                                          |
| BrakeAbsTcsWsu | Integer | none         | Brake, ABS, and traction control from vehicle CAN Bus via WSU                                                                          |
| AxWsu          | Real    | m/sec2       | Longitudinal acceleration from vehicle CAN Bus via WSU                                                                                 |
| PrndlWsu       | Integer | none         | Current transmission state (Park, Reverse, Neutral, Drive, Low) from vehicle CAN Bus via WSU                                           |
| VsaActiveWsu   | Integer | none         | Stability control active from vehicle CAN Bus via WSU                                                                                  |
| HeadlampWsu    | Integer | none         | Headlamp state from vehicle CAN Bus via WSU                                                                                            |
| WiperWsu       | Integer | none         | Wiper state from vehicle CAN Bus via WSU                                                                                               |
| ThrottleWsu    | Real    | none         | Throttle position from vehicle CAN Bus via WSU                                                                                         |
| SteerWsu       | Real    | deg          | Steering angle/position from vehicle CAN Bus via WSU                                                                                   |

### Data of the roads of Ann Arbor and WSU GPS data ###
![alt text](https://github.com/AkashPushkar/real-time-traffic-analysis/blob/master/doc/Screenshot%20from%202019-02-24%2023-58-35.png?raw=true)

## Dependencies ##
### Web Visualization ###
- [d3](https://github.com/d3/d3/wiki/Gallery) - 2D
- [Cesium](https://cesiumjs.org/) - 3D

### Trajectory Reconstruction ###
- 

### Big data Architecture - Real time analytics pipeline ###
