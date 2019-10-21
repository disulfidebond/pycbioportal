# pycbioportal: pythonic implementation of the cbioportal API

**Comments**:
This repo us under active development, and will change frequently

Current version: 1.0-beta

**Dependencies**
numpy
pandas
requests

**Usage**
Currently, the output from cbioportal will be returned as either a string or a pandas dataframe.

To return data as a string:

v = CbioportalStr("https://www.cbioportal.org")
v.specifyQuery("/webservice.do?cmd=getCaseLists&cancer_study_id=brca_mskcc_2019")
v.getCaseList()
print(v.getOutputStr)

To return data as a pandas dataframe:

v = CbioportalDF("https://www.cbioportal.org")
v.specifyQuery("/webservice.do?cmd=getCaseLists&cancer_study_id=brca_mskcc_2019")
v.getCaseList()
print(v.getOutputDF)

