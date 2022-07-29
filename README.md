# Deployment of Machine Learning Models

Accompanying repo for the online course Deployment of Machine Learning Models.

For the documentation, visit the [course on Udemy](https://www.udemy.com/deployment-of-machine-learning-models/?couponCode=TIDREPO).

```
docker build --build-arg PIP_EXTRA_INDEX_URL='https://gPzZpxSVxhFCPpwHHuKd:@pypi.fury.io/reboot87/' -t house-prices-api:latest .

docker run -p 8001:8001 -e PORT=8001 house-prices-api
```
