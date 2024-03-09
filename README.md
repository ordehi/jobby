# Jobby

Scrape for jobs.

## Schema

In data/sites.json you can store an array of sites to scrape. Each site is an object with a url and the schema to scrape from that url.

Below is the schema definition:

```
[
  {
    "url": "<URL of the page to scrape>",
    "schema": {
      "container": "<CSS selector for the main container that encapsulates items to be scraped>",
      "details": {
        "<DetailName>": {
          "selector": "<CSS selector to extract the detail>",
          "extract": "<'text' or 'attribute'> - specifies whether to extract the text of the selected element or one of its attributes",
          "single": "<'true' or 'false'> - specifies whether to extract only the first matching element (true) or all matching elements (false)"
          "attribute_name": "<name of the attribute to extract if 'extract' is set to 'attribute'> - optional, required only if 'extract' is 'attribute'"
        },
        "<AnotherDetailName>": {
          // Same structure as above for another detail within the same container
        },
        "Positions": { // Example of a nested detail collection
          "container": "<CSS selector for the sub-container>",
          "details": {
            "<SubDetailName>": {
              "selector": "<CSS selector to extract the sub-detail>",
              "extract": "<'text' or 'attribute'>",
              "single": "<'true' or 'false'>"
              "attribute_name": "<name of the attribute to extract if 'extract' is 'attribute'>"
            }
          },
          "extract": "<'multiple'> - indicates that multiple items will be extracted within this sub-container"
        }
      },
      "extract": "<'multiple'> - indicates that multiple items will be extracted within the main container"
    }
  }
]
```
