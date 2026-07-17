import { createClient, print } from 'redis';
 import redis from 'redis'
const client = createClient();
 
client.on('error', (err) => console.log('Redis client not connected to the server:', err.toString()));
client.on('ready', () => console.log('Redis client connected to server')) 
const hashKey = 'HolbertonSchools';
 
client.hset(hashKey, 'Portland', 50, redis.print);
client.hset(hashKey, 'Seattle', 80, redis.print);
client.hset(hashKey, 'New York', 20, redis.print);
client.hset(hashKey, 'Bogota', 20, redis.print);
client.hset(hashKey, 'Cali', 40, redis.print);
client.hset(hashKey, 'Paris', 2, redis.print);
 
client.hgetall(hashKey, (err, reply) => {
  console.log(reply);
});