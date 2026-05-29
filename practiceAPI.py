from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message": "welcome to my home page"}

# fake data
pages = {
    "home": "welcome to my home page",
    "about": "this is the about page",
    "contact": "this is the contact page"
}

## to get to all pages
@app.get("/pages")
def get_page():
    return pages

@app.get("/pages/{page_name}")
def get_page(page_name: str):
    if page_name in pages:
        return {
            "page": page_name,
            "content": pages[page_name]
        }
    return {"error": "Page not found"}

@app.get("/about")
def about():
    return {"message": "this is the about page"}