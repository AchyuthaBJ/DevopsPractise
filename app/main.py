from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class NotesBase():
    def __init__(self,title:str,content:str,category:str,is_fav:bool):
        self.title = title
        self.content = content
        self.category = category
        self.is_fav = is_fav
        
class Notes(NotesBase):
    def __init__(self, title, content, category, is_fav,id):
        super().__init__(title, content, category, is_fav)
        self.id = id


NOTES = [
    Notes(
        id=1,
        title="Learning FastAPI",
        content="Understanding basics",
        category="Learning",
        is_fav=False
    ),
    Notes(
        id=2,
        title="Prepare Q3 Report",
        content="Gather quarterly metrics, conversion rates, and revenue figures.",
        category="Work",
        is_fav=True,
    ),
    Notes(
        id=3,
        title="Weekly Shopping List",
        content="Almond milk, whole grain bread, Greek yogurt, and avocados.",
        category="Personal",
        is_fav=False,
    ),
    Notes(
        id=4,
        title="FastAPI Best Practices",
        content="Study dependency injection, Pydantic field validations, and async routes.",
        category="Study",
        is_fav=True,
    ),
    Notes(
        id=5,
        title="Marathon Training Schedule",
        content="Run 5km on Tuesday, 8km on Thursday, and a long 15km run on Sunday.",
        category="Fitness",
        is_fav=False,
    ),
    Notes(
        id=6,
        title="Home Renovation Ideas",
        content="Repaint living room wall sage green and replace balcony light fixtures.",
        category="Ideas",
        is_fav=True,
    )
]


@app.get("/")
def root():
    return {"root":"The app is launched"}

@app.get("/notes")
def all_notes():
    if not NOTES:
        return {"notes": "No notes are present"}
    return {
        "notes": NOTES
    }

@app.get("/notes/{id}")
def notesId(id:int):
    if not NOTES:
        return {"notes": "No notes are present"}
    for note in NOTES:
        if note.id == id:
            return note


