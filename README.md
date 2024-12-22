# Automated Azure Batch Processing Pipeline Project

## Tools used:

- Storage: Azure Data Lake Gen2
- Pipeline tool: Azure Databricks, Azure Data Factory
- Sink: Azure SQL Database
- Programming Language: Python

## Workflow:

### Data Generation and Collection:

Faker library used to generate fake customer data at interval of 30 minutes and uploaded to ADLS. 

### Data Transformation:

A Databricks Notebook is created to transform the source data. The source data contains First_name and Last_name which are concatenated together and a new column is created as fullName. The previous 2 columns are dropped. 


### Pipeline Description:

- When file arrives under the raw-data folder the pipeline is triggered and the Databricks Notebook runs.
- After transformation the file is copied to the to_process folder.
- A Get Metadata activity checks whether a file is present under the to_process folder. If file is present then it triggers the true block.
- Inside the true block, Copy Data activity loads the file from to_process folder to Azure SQL Database. It does an UPSERT into the database.
- Next Copy activity copies the file to the processed_data folder.
- After file is copied to the processed_data folder, the Delete activity deletes the file from to_process folder.


![Azure Pipeline Architecture](https://github.com/aritrasarkar99/azure-pipeline-project/blob/main/images/azure-pipeline-project.jpg)


![Azure pipeline screenshot](https://github.com/aritrasarkar99/azure-pipeline-project/blob/main/images/pipeline.jpg)













