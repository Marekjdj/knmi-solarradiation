# KNMI Solar radiation
A Python script that can be used in Home Assistant to retrieve solar radiation information from the [KNMI EDR API](https://developer.dataplatform.knmi.nl/edr-api).

## Authentication
The KNMI API requires a token, which can be requested from the [KNMI website](https://developer.dataplatform.knmi.nl/apis). The script reads the token from the secrets.yaml file, where it must be stored as "knmi_token".

## Location
A location must be specified by their ID using the "location" variable within the script. The following locations are available as of October 2024:

|Location| ID |
|--|--|
| A12-CPP                               | 06205 |
| AMSTERDAM/SCHIPHOL AP                 | 06240 |
| ARCEN AWS                             | 06391 |
| Assendelft BTP                        | 06233 |
| AWG-1                                 | 06208 |
| BERKHOUT AWS                          | 06249 |
| BG-OHVS2                              | 06214 |
| BORSSELE ALFA (BSA)                   | 06317 |
| CABAUW TOWER AWS                      | 06348 |
| CADZAND WP                            | 06308 |
| D15-FA-1                              | 06201 |
| DE BILT AWS                           | 06260 |
| DE KOOY VK                            | 06235 |
| DEELEN                                | 06275 |
| EINDHOVEN AP                          | 06370 |
| ELL AWS                               | 06377 |
| EURO PLATFORM                         | 06321 |
| F.D. ROOSEVELT AIRPORT, ST. EUSTATIUS | 78873 |
| F16-A                                 | 06206 |
| F3-FB-1                               | 06239 |
| FLAMINGO AIRPORT, BONAIRE             | 78990 |
| GILZE RIJEN                           | 06350 |
| GRONINGEN AP EELDE                    | 06280 |
| HANSWEERT                             | 06315 |
| HEINO AWS                             | 06278 |
| HERWIJNEN AWS                         | 06356 |
| HOEK VAN HOLLAND AWS                  | 06330 |
| Hollandse Kust Noord (HKN)            | 06213 |
| Hollandse Kust Zuid Alfa (HKZA)       | 06216 |
| HOOFDPLAAT WP                         | 06311 |
| HOOGEVEEN AWS                         | 06279 |
| HOORN-A                               | 06212 |
| HOUTRIBDIJK WP                        | 06258 |
| HUIBERTGAT WP                         | 06285 |
| HUPSEL AWS                            | 06283 |
| IJMOND WP                             | 06209 |
| IJMUIDEN WP                           | 06225 |
| J6-A                                  | 06211 |
| JUANCHO E. YRAUSQUIN AIRPORT, SABA    | 78871 |
| K13-A                                 | 06252 |
| K14-FA-1C                             | 06204 |
| L9-FF-1                               | 06207 |
| LAUWERSOOG AWS                        | 06277 |
| LEEUWARDEN                            | 06270 |
| LELYSTAD AP                           | 06269 |
| LICHTEILAND GOEREE                    | 06320 |
| MAASTRICHT AACHEN AP                  | 06380 |
| MARKNESSE AWS                         | 06273 |
| MAROLLEGAT                            | 06331 |
| Muiden BTP                            | 06236 |
| NIEUW BEERTA AWS                      | 06286 |
| Nieuw Vennep BTP                      | 06237 |
| Nieuwkoop BTP                         | 06238 |
| OOSTERSCHELDE 4                       | 06316 |
| OOSTERSCHELDE WP                      | 06312 |
| P11-B                                 | 06203 |
| ROTTERDAM GEULHAVEN                   | 06343 |
| ROTTERDAM THE HAGUE AP                | 06344 |
| SOESTERBERG                           | 06265 |
| STAVENISSE                            | 06324 |
| STAVOREN AWS                          | 06267 |
| TERSCHELLING HOORN AWS                | 06251 |
| TEXELHORS WP                          | 06229 |
| TWENTHE AWS                           | 06290 |
| VALKENBURG VK                         | 06210 |
| VLAKTE VAN DE RAAN                    | 06313 |
| VLIELAND                              | 06242 |
| VLISSINGEN AWS                        | 06310 |
| VOLKEL                                | 06375 |
| VOORSCHOTEN AWS                       | 06215 |
| WESTDORPE AWS                         | 06319 |
| WIJDENES WP                           | 06248 |
| WIJK AAN ZEE AWS                      | 06257 |
| WILHELMINADORP AWS                    | 06323 |
| WOENSDRECHT                           | 06340 |


## Running the script
Because the script uses imported packages like requests, it cannot be run directly from Home Assistant. Instead, a command line sensor must be used, for example:

    command_line:
	    - sensor:
		    name: KNMI Global (solar)radiation
	        unit_of_measurement: Watt/m2
	        scan_interval: 30
	        unique_id: ec278d13-91a4-4846-bb57-fe3d8d990b21
	        command: 'python3 ./python_scripts/knmi_radiation.py'
