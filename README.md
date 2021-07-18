## Bulding the application and hosting the containers
After cloning the project, make sure there is no application that is using the port `5000`, `8080` and `2104`.
1. Build and up the containers

    This command can be used to rebuild the application everytime the code is changed 
    ```bash
    docker-compose up --build -d
    ```

## Access the application
1. Access the flask application
    - Go to `localhost:5000`
    - Access an endpoint `localhost:5000/{your-route}`
        > e.g. `localhost:5000/getAccountInvoice`
2. To create API to access more Hasura endpoints
    - Add a view function in the `app.py`
    - Update the endpoint : `http://graphql-engine:8080/api/rest/{your-custom-endpoint}`
        > e.g. `http://graphql-engine:8080/api/rest/getAccountInvoice`

