# Pytest lessons

## Short preview

The project will be as cookbook to python automation and testing with pytest.

## Setup
To enjoy the automated tests, develop the framework or adapt it to your own purposes, just download the project or clone repository. You need to install packages using pip according to requirements.txt file. Run the command below in terminal:

pip install -r requirements.txt

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
