from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/")
def main():
    return Response(content="Hello from FastAPI", media_type="text/plain")


if __name__ == "__main__":
    main()
