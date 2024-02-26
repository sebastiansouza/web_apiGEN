import py_compile
from fastapi import FastAPI
from app.routes import user_routes, theme_routes, post_routes
from app.database import connect, disconnect, create_tables

# Cria uma instância do aplicativo FastAPI
app = FastAPI()

# Conectar ao banco de dados ao iniciar o aplicativo
@app.on_event("startup")
async def startup():
    create_tables()
    connect()

# Desconectar do banco de dados ao encerrar o aplicativo
@app.on_event("shutdown")
async def shutdown():
    disconnect()

# Adiciona os roteadores ao aplicativo
app.include_router(user_routes.router, prefix="/users", tags=["users"])
app.include_router(theme_routes.router, prefix="/themes", tags=["themes"])
app.include_router(post_routes.router, prefix="/posts", tags=["posts"])

# Executa o aplicativo
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
