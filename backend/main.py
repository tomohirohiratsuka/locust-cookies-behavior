import datetime

from typing import Optional

from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import Response
from starlette.requests import Request

app = FastAPI()


@app.get("/")
def read_root(
		response: Response
):
	response.set_cookie(
		key="access_token",
		value=f"your_access_token_{datetime.datetime.now().timestamp()}",
		domain="localhost",
		httponly=True
	)
	return {"Hello": "World"}


def get_token_from_cookie(
		request: Request
):
	token = request.cookies.get("access_token")
	return token


@app.get("/items")
def read_item(
		access_token: Optional[str] = Depends(get_token_from_cookie),
):
	if not access_token:
		raise HTTPException(status_code=401, detail="Access token not found")
	return {"access_token": access_token}
