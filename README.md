# onto_x
## Purpose
The purpose on this project is to build logical representation on Onto-x that preserves ancestor relationship (direct and indirect) and so construct the hierarchy on entity.

## Prequisite
You need to install last version of python and last version of pyBuilder tool.

## Build project
Go to directory "onto_x" and launch command "pyb" .

## Test command line
After building project, go to directory "target\dist\onto_x-1.0.dev0\onto".
To do query you should launch following command line:

onto_main.py [PATH_FILE_NAME] [QUERY_COMMAND] [PARAMETER]

The command line has 3 mandatory parameters:

- PATH_FILE_NAME: the path of csv file containing onto_x datas
- QUERY_COMMAND: the type of query we want to execute. There are 2 possibilities of queries: "searchOntoByName" and "searchOntoById" which respectively search data on file from onto label field and id field.
- PARAMETER: parameter of query (id or label)

## Example

- Query by label:
    
    onto_main.py C:\projets\onto_x\src\main\resources\onto_x.csv searchOntoByName "CERVIX DISORDER"

- Query by id:

    onto_main.py C:\projets\onto_x\src\main\resources\onto_x.csv searchOntoById "http://entity/CST/CERVIX%20DIS"

