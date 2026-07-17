import { createClient, print } from 'redis';
 import redis from 'redis'
const client = createClient();
 
client.on('error', (err) => console.log('Redis client not connected to the server:', err.toString()));
client.on('ready', () => console.log('Redis client connected to server')) 
client.subscribe("holberton school channel")
client.on('message', (channel, message) => {
    if (channel === "holberton school channel"){
        console.log(message)
    }
    else if(message === "KILL_SERVER"){
        client.unsubscribe("holberton school channel")
        client.quit()
    }
})
