![example workflow](https://github.com/oscarasco/webhook-tester/actions/workflows/ci-test.yml/badge.svg)

# Self-Hosted Webhook Tester

Explore the flexibility of our self-hosted webhook tester powered by our containerized application. With no restrictions on the number of notifications an endpoint can receive and the ability to fully configure server responses including status codes and timeouts.


## Get webhook-tester:

#### Pull from official [registry](https://hub.docker.com/r/oscarasco/webhook-tester):

```shell
docker run -p 80:80 -p 8000:8000 -t oscarasco/webhook-tester
```

#### Build from source:

Begin by cloning the project along with its frontend submodule:
```shell
git clone --recurse-submodule git@github.com:oscarasco/webhook-tester.git
```

To build and launch the container, execute the following commands:

```shell
docker build -t webhook-tester .
docker run -p 80:80 -p 8000:8000 -t webhook-tester
```
#### Usage:


At this stage, the front-end is accessible via http://localhost, while the backend is reachable at http://localhost:8000. For instructions on sending your webhook to the webhook tester and customizing the receiver response, please refer to the backend documentation available at http://localhost:8000/docs.


Now you're ready to test your webhooks effortlessly!

## Development:

#### Testing:

```shell
bash ./scripts/run_tests.sh
```