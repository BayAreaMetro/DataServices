# specify desired folder for all 511 data pull outputs
OUTPUT_DIR = 'GTFS_outputs'

# specify desired files from each agency's GTFS feed
GTFS_FILES = ['agency.txt',
              'calendar.txt',
              'calendar_attributes.txt',
              'calendar_dates.txt',
              'directions.txt',
              'feed_info.txt',
              'routes.txt',
              # 'shapes.txt',  # not in feed for all agencies
              'stops.txt',
              'stop_times.txt',
              'trips.txt']

# specify desired operator IDs and names
OPERATOR_ID_MAP = {'3D': 'Tri Delta Transit',
                   'AC': 'AC Transit',
                   'AM': 'Capitol Corridor Joint Powers Authority',
                   'BA': 'Bay Area Rapid Transit',
                   'CC': 'County Connection',
                   'CE': 'Altamont Corridor Express',
                   'CM': 'Commute.org Shuttles',
                   'CT': 'Caltrain',
                   'DE': 'Dumbarton Express Consortium',
                   'EM': 'Emery Go-Round',
                   'FS': 'Fairfield and Suisun Transit',
                   'GF': 'Golden Gate Ferry',
                   'GG': 'Golden Gate Transit',
                   'MA': 'Marin Transit',
                   'MS': 'Stanford Marguerite Shuttle',
                   'PE': 'Petaluma Transit',
                   'RV': 'Rio Vista Delta Breeze',
                   'SA': 'Sonoma Marin Area Rail Transit',
                   'SB': 'San Francisco Bay Ferry',
                   'SC': 'VTA',
                   'SF': 'San Francisco Municipal Transportation Agency',
                   'SM': 'SamTrans',
                   'SO': 'Sonoma County Transit LastGenerated',
                   'SR': 'Santa Rosa CityBus LastGenerated',
                   'ST': 'SolTrans LastGenerated',
                   'TD': 'Tideline Marine Group Inc LastGenerated',
                   'UC': 'Union City Transit LastGenerated',
                   'VC': 'Vacaville City Coach LastGenerated',
                   'VN': 'Napa LastGenerated',
                   'WC': 'WestCat (Western Contra Costa) LastGenerated',
                   'WH': 'Livermore Amador Valley Transit Authority LastGenerated'
                   }