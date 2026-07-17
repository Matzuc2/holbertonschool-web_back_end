import { createClient } from "redis";
import redis from "redis"
import { promisify } from "util";
const client = createClient();

client.on("error", (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on("ready", () => console.log("Redis client connected to the server"));
const getAsync = promisify(client.get).bind(client)
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        redis.print((`Reply: ${reply}`));
    });
}

async function displaySchoolValue(schoolName) {
    const value = await getAsync(schoolName)
    console.log(value)
}

await displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');