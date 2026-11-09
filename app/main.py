from fastapi import FastAPI

from app.routers import items

app = FastAPI(
    title="FastAPI Demo",
    description="一个基础的 FastAPI CRUD 示例",
    version="0.1.0",
    swagger_ui_parameters={
        "swagger_js_url": "https://cdn.bootcdn.net/ajax/libs/swagger-ui/5.17.14/swagger-ui-bundle.min.js",
        "swagger_css_url": "https://cdn.bootcdn.net/ajax/libs/swagger-ui/5.17.14/swagger-ui.min.css",
    }
)

# 注册路由
app.include_router(items.router)

@app.get("/", tags=["root"])
def root():
    return {"message": "Hello FastAPI 👋", "docs": "/docs"}

@app.get("/health", tags=["root"])
def health():
    return {"status": "ok"}
