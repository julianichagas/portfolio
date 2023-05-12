#pip3 install --upgrade google-analytics-data

# Libraries
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

# Using a default constructor instructs the client to use the credentials
# specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ga4.json'

# Define function
def run_report(property_id:str, dimensions:List[str], metrics: List[str], date_ranges: List[Tuple[str, str]],
               dim_filters: Optional[List[Tuple[str, List[str]]]] = None):

    
    
    client = BetaAnalyticsDataClient()
    
    # if there is a filter to be filtered
    if dim_filters != None:
        # Create the filter expression
        filter_expression_list=FilterExpression(
            filter=Filter(
                    field_name=dim_filters[0],
                    in_list_filter=Filter.InListFilter(
                                       values=dim_filters[1]
                    )
                )
            )
    
        request = RunReportRequest(
            property=f"properties/{property_id}",
            dimensions=[Dimension(name=dim) for dim in dimensions],
            metrics=[Metric(name=metric) for metric in metrics],
            date_ranges=[DateRange(start_date=date_range[0], end_date=date_range[1]) for date_range in date_ranges],
            dimension_filter=filter_expression_list,
        )
        
    # else, case no filter were inserted in the function
    else:
        request = RunReportRequest(
            property=f"properties/{property_id}",
            dimensions=[Dimension(name=dim) for dim in dimensions],
            metrics=[Metric(name=metric) for metric in metrics],
            date_ranges=[DateRange(start_date=date_range[0], end_date=date_range[1]) for date_range in date_ranges],
        )
        
    response = client.run_report(request)

    output = {}
    if 'property_quota' in response:
        output['quota'] = response.property_quota
    
    # construct the dataset
    headers = [header.name for header in response.dimension_headers] + [header.name for header in response.metric_headers]
    rows = []
    for row in response.rows:
        rows.append(
            [dimension_value.value for dimension_value in row.dimension_values] + \
            [metric_value.value for metric_value in row.metric_values])            
    output['headers'] = headers
    output['rows'] = rows
    
    return output

# Dimensions, metrics and filters to be searched on GA4
dimension_list = ["transactionId", "source", "medium", "campaignId", "campaignName"]
metrics_list   = ["sessions"]
date_ranges    = [("90daysAgo","yesterday")]
orders_list    = ["1329240994844",
                  "1329250994872",
                  "1329260994880"]
dim_filters    = ("transactionId",orders_list) #optional variable

# Call function
response = run_report("YOUR PROPERTY ID HERE", dimension_list, metrics_list, date_ranges, dim_filters)

# Show return in DataFrame
display(pd.DataFrame(response['rows'],columns=response['headers']))