## An analysis of aircraft crashes from 1908 to 2009

Source: https://data.world/data-society/airplane-crashes

**Audit**

- There are 13 columns and 5268 records, plus two more columns containing coordinates from a different database.
- The dataset lists a large proportion of notable aircraft incidents (not just airplanes), which are mostly fatal crashes.
- It is unknown why this dataset was created or who paid for it. The original source is no longer available on the internet too.
- Column details:
  - date - The date the incident occurred. Formatted MM/DD/YYYY. Everything is sorted by date.
  - time - The approximate local time the incident occurred, in 24-hour format. Unknown times are left blank.
  - location - The approximate location the incident occurred. Needs processing as it is written in plain English with prepositions included.
  - operator - The carrier or organisation which operates the aircraft. Military aircraft are listed as such.
  - flight_number - The identification number assigned to the flight. Not all flights have a number.
  - route - The intended route of the aircraft. If travelling to a destination, both the start and end locations are included, separated by a dash.
  - type - The model/variant of aircraft.
  - registration - The registration number.
  - id - Basically a VIN but for airplanes. Not important for this data analysis.
  - aboard - Total number of people aboard.
  - fatalities - Total number of fatalities of those aboard.
  - ground_fatalities - Total number of fatalities of those outside of the aircraft.
  - latitude, longitude - coordinates collected from OpenStreetMap's _Nominatim_ Geocoding API, using data from the location field.
  - summary - A brief explanation of the incident in plain English. Mostly not usable for this data analysis.
