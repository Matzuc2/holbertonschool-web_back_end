import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
client.on('ready', () => {
  console.log('Redis client connected to the server');
});

const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

function getItemById(id) {
  return listProducts.find((item) => item.id === Number(id));
}

function reserveStockById(itemId, stock) {
  return setAsync(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? Number(reservedStock) : 0;
}

app.get('/list_products', (req, res) => {
  res.json(
    listProducts.map((item) => ({
      itemId: item.id,
      itemName: item.name,
      price: item.price,
      initialAvailableQuantity: item.stock,
    }))
  );
});

app.get('/list_products/:itemId', async (req, res) => {
  const item = getItemById(req.params.itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(item.id);

  return res.json({
    itemId: item.id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock,
    currentQuantity: item.stock - reservedStock,
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const item = getItemById(req.params.itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const reservedStock = await getCurrentReservedStockById(item.id);
  const currentQuantity = item.stock - reservedStock;

  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: item.id });
  }

  await reserveStockById(item.id, reservedStock + 1);
  return res.json({ status: 'Reservation confirmed', itemId: item.id });
});

app.listen(1245);