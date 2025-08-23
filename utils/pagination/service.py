from sqlalchemy import select, func
from sqlalchemy.orm import Session
from math import ceil
from utils.pagination.paginator import PaginateByPage
from utils.pagination.schema import PaginatationSchema, T

def paginate(db: Session, stmt, paginator: PaginateByPage) -> PaginatationSchema[T]:
    # total count
    total_items = db.execute(
        select(func.count()).select_from(stmt.subquery())
    ).scalar_one()

    # apply offset/limit
    items = db.execute(
        stmt.offset(paginator.skip).limit(paginator.limit)
    ).scalars().all()

    # pages
    total_pages = ceil(total_items / paginator.page_size) if total_items > 0 else 1

    return {
        "page": paginator.page,
        "page_size": paginator.page_size,
        "total_items": total_items,
        "total_pages": total_pages,
        "items": items,
    }