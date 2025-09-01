from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import date

app= FastAPI()

bodyweights=[]



class Weight_input(BaseModel):

    day: date
    kg: float = Field(..., gt=0)


class Weight_output(BaseModel):
    id: int
    day: date
    kg: float = Field(..., gt=0)



@app.get("/healthz")
def message():
    return {"msg": "ok"}



@app.post("/weightz", response_model=Weight_output, status_code=201) #responsemodel forteller hva slags respons man forventer
def my_weight(new_weight: Weight_input):
    new_id = len(bodyweights) + 1
    row = Weight_output(id=new_id, day=new_weight.day, kg=new_weight.kg)
    bodyweights.append(row)

    #return  ("msg": "You weighed " + str(new_weight.kg) + " kg on date " + str(new_weight.day))
    return row


@app.get("/weightz",  response_model=list[Weight_output])
def get_weight(limit: int=1000):
    return bodyweights[-limit:][::-1]

#TESTER gitupdate

