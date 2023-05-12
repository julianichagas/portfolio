# Google Analytics 4 Data Retrieval Code

This code provides a Python implementation to retrieve data from Google Analytics 4 (GA4) using the Google Analytics Data API. It allows you to easily connect to the GA4 API, run reports, and process the response for further analysis.

Prerequisites
Before using this code, make sure you have the following requirements:

- Python 3 installed

- Install the google-analytics-data library using the following command:

```
pip3 install --upgrade google-analytics-data
```
- Obtain your GA4 property ID and update the code by replacing "YOUR PROPERTY ID HERE" with your actual property ID.

- Set up your Google Cloud project and generate a JSON key file for authentication. Save the key file as ga4.json in the same directory as this code.

## Usage
- Import the required libraries:

```
import pandas as pd
import os
from typing import List, Tuple, Optional
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
    Filter,
    FilterExpression,
)
```

- Define the run_report() function, which takes the necessary parameters to execute a report:

```
def run_report(property_id:str, dimensions:List[str], metrics: List[str], date_ranges: List[Tuple[str, str]],
               dim_filters: Optional[List[Tuple[str, List[str]]]] = None):
   ...
```
- Replace "YOUR PROPERTY ID HERE" with your GA4 property ID in the code.

- Customize the dimension_list, metrics_list, date_ranges, and dim_filters variables according to your reporting needs.

- Call the run_report() function with your specified parameters:

```
response = run_report("YOUR PROPERTY ID HERE", dimension_list, metrics_list, date_ranges, dim_filters)
```

- The result will be stored in the response variable, containing the dimension and metric data.

- To visualize the result in a DataFrame, use the following code:

```
display(pd.DataFrame(response['rows'], columns=response['headers']))
```
