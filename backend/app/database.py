import os
import asyncpg

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/cv_platform")

async def init_db():
    # 예시: 연결 풀 생성
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL)

async def close_db():
    await pool.close()
