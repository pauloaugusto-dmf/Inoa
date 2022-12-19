# Inoa

Project for tracking stocks on the stock exchange

<table>
    <tr>
        <td>Python</td>
        <td>3.11.1</td>
    </tr>
    <tr>
        <td>Django</td>
        <td>4.1.4</td>
    </tr>
    <tr>
        <td>Postgresql</td>
        <td>15.1</td>
    </tr>
    <tr>
        <td>Redis</td>
        <td>7.0.7</td>
    </tr>
    <tr>
        <td>RabbitMQ</td>
        <td>3.11.5</td>
    </tr>
    <tr>
        <td>Celery</td>
        <td>5.2.7</td>
    </tr>
</table>

# Settings to run the project

Note: To run this project it is necessary to have Docker and Docker-Compose installed. For more information visit [Docker Docs](https://docs.docker.com/)


```bash
# clone the repository
git clone https://github.com/pauloaugusto-dmf/Inoa.git

# access the project folder
cd Inoa

# start the container
make up
```
### Open the browser at the address `http://0.0.0.0:8000/`
<br>

# Other useful commands

Note: These commands need the container to be active
```bash
# run container with logs
make up-logs

# run the tests
make test

# show the logs
make logs

# run the rails console
make console

# finish the container
make down
```