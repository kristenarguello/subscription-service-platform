from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("", status_code=200)
@router.get("/", status_code=200, include_in_schema=False)
def health() -> dict[str, str]:
    return {"status": "ok"}
