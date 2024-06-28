from aiogram import Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis


# Инициализируем Redis
redis = Redis(host='localhost')

# Инициализируем хранилище (создаем экземпляр класса MemoryStorage)
storage = RedisStorage(redis=redis)

# Создаем объекты бота и диспетчера
dp = Dispatcher(storage=storage)
