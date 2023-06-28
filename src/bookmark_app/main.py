import duckdb
from fastapi import FastAPI

app = FastAPI()

# TODO: rewrite using other DB or search engine DB.
con = duckdb.connect(database="database.duckdb", read_only=False)
con.execute(
    "CREATE TABLE IF NOT EXISTS tbl_url ( url VARCHAR NOT NULL UNIQUE, tags VARCHAR )"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


# TODO: Should be POST method?
@app.get("/items/")
def store_url(url, tags):
    # TODO: update tag only if tags params updated from stored tags.
    print(f"url: {url}, tags: {tags}")
    con.execute(
        "INSERT INTO tbl_url VALUES ($url, $tags) ON CONFLICT (url) DO UPDATE SET tags=$tags",
        {"url": url, "tags": tags},
    )
    con.execute("SELECT * FROM tbl_url")
    print(con.fetchall())
