# Awesome Free Land Parcel Data [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of free land parcel data sources, tools, and resources for GIS professionals, researchers, and developers.

Land parcel data is fundamental for urban planning, real estate analysis, environmental studies, and many other applications. This list focuses on freely available parcel data.

## Contents

- [United States](#united-states)
  - [Statewide Coverage](#statewide-coverage)
  - [County-Level Coverage](#county-level-coverage)
  - [Federal](#federal)
- [Global Sources](#global-sources)
- [Canada](#canada)
- [Europe](#europe)
- [Australia & New Zealand](#australia--new-zealand)
- [Other Countries](#other-countries)

## United States


### Statewide Coverage

States with comprehensive, wall-to-wall parcel coverage:

#### California
- [California Statewide Parcel Map](https://geohub.lacity.org/documents/baaf8251bfb94d3984fb58cb5fd93258) - Comprehensive statewide wall-to-wall parcels in 1.6GB file geodatabase bulk download.
- **Coverage**: All 58 California counties with standardized parcel boundaries and attributes.
- **Data Format**: File geodatabase (.gdb) with rich attribute schema including APN, addresses, land use codes, tax information, and building details.
- **Attributes**: Assessor Parcel Numbers (APN), situs addresses, use codes, tax rate areas, building characteristics (year built, square footage, bedrooms/bathrooms), assessed values, and legal descriptions.
- **Coordinate System**: California State Plane coordinate systems (varies by county) with Web Mercator versions available.
- **Update Frequency**: Regular updates from county assessor offices, though frequency varies by county.
- **Access Methods**: Direct download, ArcGIS feature services, and web map viewers.

#### Florida
- [Florida Geographic Data Library](https://fgdl.org/zips/geospatial_data/) - Statewide parcels in file geodatabase format with historical archive back to 2007.

#### North Carolina
- [North Carolina OneMap Parcels](https://www.nconemap.gov/pages/parcels) - Statewide parcel data for North Carolina.

#### Washington
- [Washington State Geospatial Open Data Portal](https://geo.wa.gov/) - Statewide GIS data including parcels.

### County-Level Coverage

States with parcel data available by county only only:

#### New York
- [New York State GIS Data Portal](https://data.gis.ny.gov/search?categories=%252Fcategories%252Fparcels) - Standardized parcels for 36 of 62 counties.
- **Available Counties**: Albany, Cayuga, Chautauqua, Cortland, Erie, Genesee, Greene, Hamilton, Lewis, Livingston, Montgomery, NYC (all 5 boroughs), Oneida, Onondaga, Ontario, Orange, Oswego, Otsego, Putnam, Rensselaer, Rockland, Schuyler, St Lawrence, Steuben, Suffolk, Sullivan, Tioga, Tompkins, Ulster, Warren, Wayne, Westchester.
- **Note**: Remaining 26 counties require direct contact with county offices for parcel data access.

#### Oregon
- [Oregon Department of Forestry](https://gis.odf.oregon.gov/ags1/rest/services/WebMercator/TaxlotsDisplay/MapServer) - Tax lot data for all 36 counties via MapServer service.
- **Coverage**: All 36 Oregon counties included in single MapServer service layer.
- **Data Format**: ArcGIS MapServer service supporting multiple export formats (PNG, JPG, PDF, GeoJSON).
- **Coordinate System**: Oregon Lambert projection (original data) served in Web Mercator (EPSG:3857).
- **Access Methods**: ArcGIS web viewers, ArcMap, ArcGIS Pro, ArcGIS Online Map Viewer, ArcGIS Earth.
- **Limitations**: No bulk download option; data must be accessed through MapServer queries with 1000 record limit per request.
- **Note**: Data currency and completeness varies significantly by county; no standardized statewide dataset or update schedule.

#### Texas
- [Texas Natural Resources Information System](https://data.tnris.org/) - County-level parcel data available through modern DataHub with API access.
- **Data Portal**: Modern web-based DataHub interface with search, filter, and download capabilities.
- **API Access**: RESTful API for programmatic data access and integration.
- **Bulk Download Tool**: [TNRIS Bulk Downloader](https://github.com/TNRIS/go-bulk-downloader) - Go-based command-line tool for automated large dataset downloads.
- **Data Formats**: Multiple formats available including Shapefile, GeoJSON, and other standard GIS formats.
- **Coverage Variability**: Data availability, currency, and completeness varies significantly by county based on local data sharing agreements.
- **Note**: Texas does not provide statewide parcel coverage; each county maintains its own parcel data with varying levels of participation in state data sharing.

#### Utah
- [Utah Geospatial Resource Center](https://gis.utah.gov/products/sgid/cadastre/parcels/) - Parcel data for all 29 counties available through SGID database with both basic parcels and enhanced Land Information Records (LIR).
- **Data Types**: Basic parcels (boundaries, IDs, addresses) and LIR parcels (with tax roll attributes including market values, building details, construction year).
- **Update Schedule**: "Big 5" counties (Davis, Salt Lake, Utah, Washington, Weber) updated monthly; rural counties quarterly to annually.
- **Access Methods**: ArcGIS feature services, direct database queries, statewide feature service, vector tile service.
- **Legal Foundation**: Mandated by HB113 (2005) requiring state coordination with county recorders and surveyors.
- **Note**: While all counties are covered, each county must be downloaded separately; no single statewide bulk download available.

#### Virginia
- [Virginia Geographic Information Network (VGIN)](https://vgin.virginia.gov/) - State coordinating body for GIS data with links to local parcel data sources.
- **Coverage**: Decentralized model with 95 counties and 38 independent cities maintaining individual parcel datasets.
- **Data Coordination**: VGIN provides guidance and standards but no centralized statewide parcel dataset.
- **Access Methods**: Individual county/city GIS portals, open data portals, and direct data requests.
- **Notable Localities**: Fairfax County, Virginia Beach, Loudoun County, Henrico County, and Richmond City provide comprehensive open parcel data.
- **Data Formats**: Varies by locality - common formats include Shapefile, GeoJSON, File Geodatabase, and web services.
- **Update Frequency**: Varies significantly by locality, typically ranging from monthly to annually.
- **Limitations**: No standardized statewide schema; attribute completeness and data currency varies by jurisdiction.
- **Note**: Each locality must be contacted individually for data access requirements and availability.

#### Wyoming
- [Wyoming Property Division GIS Portal](https://wyo-prop-div.maps.arcgis.com/home/index.html) - ArcGIS Online portal providing access to Wyoming property and parcel data.

### Federal

- [BLM Land Records](https://www.blm.gov/services/land-records) - Bureau of Land Management's land records and survey data.
- [Census Bureau TIGER/Line](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html) - Topologically Integrated Geographic Encoding and Referencing system.
- [USDA Geospatial Data Gateway](https://datagateway.nrcs.usda.gov/) - Agricultural and natural resource data including land use.
- [USGS National Map](https://www.usgs.gov/programs/national-geospatial-program/national-map) - Comprehensive geospatial data including land boundaries.

## Global Sources

- [Global Administrative Areas (GADM)](https://gadm.org/) - Spatial database of administrative areas worldwide.
- [Natural Earth](https://www.naturalearthdata.com/) - Public domain map dataset with administrative boundaries.
- [OpenStreetMap](https://www.openstreetmap.org/) - Collaborative mapping project with land use and property boundary data.

## Canada

- [British Columbia Data Catalogue](https://catalogue.data.gov.bc.ca/) - Provincial open data including parcels.
- [Natural Resources Canada GEO.ca](https://geo.ca/) - Canada's definitive source for open geospatial information.
- [Ontario GeoHub](https://geohub.lio.gov.on.ca/) - Provincial geospatial data portal.
- [Statistics Canada Boundary Files](https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/bound-limit-eng.cfm) - Administrative boundary data.

## Europe

- [European Environment Agency](https://www.eea.europa.eu/data-and-maps) - Environmental and land use data across Europe.
- [France Cadastre](https://cadastre.data.gouv.fr/) - French national cadastral data.
- [Germany GovData](https://www.govdata.de/) - German federal geospatial data portal.
- [INSPIRE Geoportal](https://inspire-geoportal.ec.europa.eu/) - European spatial data infrastructure.
- [UK Land Registry Open Data](https://landregistry.data.gov.uk/) - Property ownership and transaction data.

## Australia & New Zealand

- [Australian Bureau of Statistics](https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs-edition-3/jul2021-jun2026/access-and-downloads/digital-boundary-files) - Statistical boundary files.
- [Geoscience Australia](https://www.ga.gov.au/data-pubs) - National geospatial datasets and data portal.
- [Land Information New Zealand (LINZ)](https://data.linz.govt.nz/) - Comprehensive land and property data.

## Other Countries

- [Brazil IBGE](https://www.ibge.gov.br/geociencias/downloads-geociencias.html) - Brazilian geographic and statistical data.
- [India Survey of India](https://www.surveyofindia.gov.in/) - National mapping agency data.
- [South Africa National Geo-spatial Information](https://ngi.dalrrd.gov.za/) - National spatial data infrastructure.



## Standards & Formats

- [GeoJSON](https://geojson.org/) - Format for encoding geographic data structures.
- [GeoPackage](https://www.geopackage.org/) - Open, standards-based, platform-independent format.
- [KML](https://developers.google.com/kml/) - Keyhole Markup Language for geographic data.
- [OGC Standards](https://www.ogc.org/standards/) - Open Geospatial Consortium standards.
- [Shapefile](https://en.wikipedia.org/wiki/Shapefile) - Geospatial vector data format.
- [WKT/WKB](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) - Well-Known Text/Binary geometry representations.

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work. 