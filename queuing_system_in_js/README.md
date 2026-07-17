# Queuing System in JavaScript

This project covers asynchronous job handling and Redis-backed data storage in Node.js. It is a set of small exercises that build up from basic Redis operations to job queues and a simple inventory API.

## What this project covers

- Redis client setup and basic key/value operations
- Promisified Redis access with `util.promisify`
- Kue job creation and processing
- A small Express server that exposes product and reservation endpoints

## Project structure

- `0-redis_client.js` - create a Redis client and connect to the server
- `1-redis_op.js` - set a key in Redis
- `2-redis_op_async.js` - read a key asynchronously from Redis
- `4-redis_advanced_op.js` - store and read multiple Redis values
- `5-publisher.js` / `5-subscriber.js` - basic pub/sub example
- `6-job_creator.js` / `6-job_processor.js` - create and process a job queue
- `7-job_creator.js` / `7-job_processor.js` - queue jobs with better structure
- `8-job.js` / `8-job.test.js` - push notification job creator and tests
- `9-stock.js` - Express + Redis stock reservation API

## Requirements

- Node.js
- Redis server
- npm dependencies installed from `package.json`

## Running the stock server

Start the server with:

```bash
npm run dev 9-stock.js
```

The server listens on port `1245` and exposes:

- `GET /list_products`
- `GET /list_products/:itemId`
- `GET /reserve_product/:itemId`

## Example usage

```bash
curl localhost:1245/list_products
curl localhost:1245/list_products/1
curl localhost:1245/reserve_product/1
```

## Notes

- The stock API stores reserved quantity in Redis.
- Responses are returned as JSON.
- The job queue tests use Kue test mode to inspect queued jobs without processing them.