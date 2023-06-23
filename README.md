# Learn FastAPI

##### Technical Details

> Actually, Query, Path and other's you'll see next create objects of subclasses
> of a common Param class, which is itself a subclass of Pydantic's FieldInfo class.

> And Pydantic's Field returns an instance of FieldInfo as well.

> Body also returns objects of a subclass of FieldInfo directly.

> Remember that when you import Query, Path, and others from fastapi, those are actually
> functions that return special classes.
