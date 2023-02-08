# Pytest lessons

## Short preview

The project will be as cookbook to python automation and testing with pytest.

## Write api automation tests eazy

Check the automation framework PyCamel based on pytest and pydantic that will save a lot of your code and nerves

## Run project tests:
pytest -s -v test/ --alluredir=allure_results

## Run allure reports:
allure serve allure_results

## Build image with test:
docker build --build-arg run_env=development -t automation-tests .

## Run container:
docker run automation-tests

## Copy folder with Allure report from docker container:
docker cp $(docker ps -a -q | head -1):/usr/lessons/allureResults .

## Run allure reports copied from docker container:
allure serve allureResults