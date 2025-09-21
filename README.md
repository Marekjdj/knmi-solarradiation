# KNMI Solar radiation
A Python script that can be used in Home Assistant to retrieve solar radiation information from the [KNMI EDR API](https://developer.dataplatform.knmi.nl/edr-api).

## Authentication
The KNMI API requires a token, which can be requested from the [KNMI website](https://developer.dataplatform.knmi.nl/apis). The script reads the token from the secrets.yaml file, where it must be stored as "knmi_token".

## Location
A location must be specified by their ID using the "location" variable within the script. The following locations are available as of September 2025:

|Location| ID |
|--|--|
| A12-CPP                   | 0-20000-0-06205 |
| Arcen                     | 0-20000-0-06391 |
| Assendelft                | 0-528-0-06233   |
| AWG-1                     | 0-20000-0-06208 |
| Berkhout                  | 0-20000-0-06249 |
| Bonaire Airport           | 0-20000-0-78990 |
| Borssele Alpha            | 0-528-0-06317   |
| Buitengaats BG-OHVS2      | 0-20000-0-06214 |
| Cabauw                    | 0-20000-0-06348 |
| Cadzand                   | 0-20000-0-06308 |
| D15-FA-1                  | 0-20000-0-06201 |
| De Bilt                   | 0-20000-0-06260 |
| De Kooy Airport           | 0-20000-0-06235 |
| Deelen Airport            | 0-20000-0-06275 |
| Eindhoven Airport         | 0-20000-0-06370 |
| Ell                       | 0-20000-0-06377 |
| Europlatform              | 0-20000-0-06321 |
| F16-A                     | 0-20000-0-06206 |
| F3-FB-1                   | 0-20000-0-06239 |
| Gilze-Rijen Airport       | 0-20000-0-06350 |
| Groningen Airport Eelde   | 0-20000-0-06280 |
| Hansweert                 | 0-20000-0-06315 |
| Heino                     | 0-20000-0-06278 |
| Herwijnen                 | 0-20000-0-06356 |
| Hoek van Holland          | 0-20000-0-06330 |
| Hollandse Kust Noord      | 0-528-0-06213   |
| Hollandse Kust West Alpha | 0-528-0-06218   |
| Hollandse Kust Zuid Alpha | 0-528-0-06216   |
| Hoofdplaat                | 0-20000-0-06311 |
| Hoogeveen                 | 0-20000-0-06279 |
| Hoorn Terschelling        | 0-20000-0-06251 |
| Hoorn-A                   | 0-20000-0-06212 |
| Horst                     | 0-528-0-06392   |
| Houtribdijk               | 0-20000-0-06258 |
| Huibertgat                | 0-20000-0-06285 |
| Hupsel                    | 0-20000-0-06283 |
| IJmond                    | 0-20000-0-06209 |
| IJmuiden                  | 0-20000-0-06225 |
| J6-A                      | 0-20000-0-06211 |
| K13-A                     | 0-20000-0-06252 |
| K14-FA-1C                 | 0-20000-0-06204 |
| L9-FF-1                   | 0-20000-0-06207 |
| Lauwersoog                | 0-20000-0-06277 |
| Leeuwarden Airport        | 0-20000-0-06270 |
| Lelystad Airport          | 0-20000-0-06269 |
| Lichteiland Goeree        | 0-20000-0-06320 |
| Maastricht Airport        | 0-20000-0-06380 |
| Marknesse                 | 0-20000-0-06273 |
| Muiden                    | 0-528-0-06236   |
| Nieuw Beerta              | 0-20000-0-06286 |
| Nieuwkoop                 | 0-528-0-06238   |
| Nieuw-Vennep              | 0-528-0-06237   |
| Oosterschelde             | 0-20000-0-06312 |
| P11-B                     | 0-20000-0-06203 |
| Rotterdam Airport         | 0-20000-0-06344 |
| Rotterdam Geulhaven       | 0-20000-0-06343 |
| Saba Airport              | 0-20000-0-78871 |
| Schaar                    | 0-20000-0-06316 |
| Schiphol Airport          | 0-20000-0-06240 |
| Sint Eustatius Airport    | 0-20000-0-78873 |
| SOESTERBERG               | 0-20000-0-06265 |
| Stavenisse                | 0-20000-0-06324 |
| Stavoren                  | 0-20000-0-06267 |
| Texelhors                 | 0-20000-0-06229 |
| Tholen                    | 0-20000-0-06331 |
| Twenthe Airport           | 0-20000-0-06290 |
| VALKENBURG VK             | 0-20000-0-06210 |
| Vlakte van de Raan        | 0-20000-0-06313 |
| Vlieland Vliehors         | 0-20000-0-06242 |
| Vlissingen                | 0-20000-0-06310 |
| Volkel Airport            | 0-20000-0-06375 |
| Voorschoten               | 0-20000-0-06215 |
| Westdorpe                 | 0-20000-0-06319 |
| Wijdenes                  | 0-20000-0-06248 |
| Wijk aan Zee              | 0-20000-0-06257 |
| Wilhelminadorp            | 0-20000-0-06323 |
| Woensdrecht Airport       | 0-20000-0-06340 |


## Running the script
Because the script uses imported packages like requests, it cannot be run directly from Home Assistant. Instead, a command line sensor must be used, for example:

	command_line:
	  - sensor:
	      name: KNMI Global (solar)radiation
	      unit_of_measurement: W/m²
	      scan_interval: 30
	      unique_id: ec278d13-91a4-4846-bb57-fe3d8d990b21
	      command: 'python3 ./python_scripts/knmi_radiation.py'
