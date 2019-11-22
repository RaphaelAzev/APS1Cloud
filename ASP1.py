from fastapi import FastAPI
import json
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder


dictTarefas = {}
auto_id = 1
	
app = FastAPI()

#id_incremented = len(dictTarefas) + 1

#class Tarefa:
#  def __init__(self, name, content):
#	self.name = name
#	self.content = content

class Tarefa(BaseModel):
	name: str = None
	content: str = None


#Tarefa
@app.get("/Tarefas")
def list_tarefas():
	try:
		return dictTarefas 
	except Exception as e:
		return {"status": "failed", "except" : e}

@app.post("/Tarefas")
def post_tarefa(tarefa: Tarefa):
	try:
        global auto_id
        dictTarefas[auto_id] = {"Name": tarefa.name, "Content": tarefa.content}
        auto_id += 1
        return {"status": "success", "status_code": 200} 
    except Exception as e:
        return {"status": "failed", "except" : e} 

@app.get("/Tarefas/{tarefa_id}")
def list_tarefa(tarefa_id: int):
	try:
		return dictTarefas[tarefa_id]
	except Exception as e:
		return {"status": "failed", "except" : e}

@app.delete("/Tarefas/{tarefa_id}")
def delete_tarefa(tarefa_id: int):
	try:
		del dictTarefas[tarefa_id]
		return {"status": "success", "status_code": 200} 
	except Exception as e:
		return {"status": "failed", "except" : e} 

@app.put("/Tarefas/{tarefa_id}")
def edit_tarefas(tarefa_id: int, tarefa: Tarefa):
	try:
		dictTarefas[tarefa_id]['Name'] = tarefa.name
		dictTarefas[tarefa_id]['Content'] = tarefa.content

		return {"status": "success", "status_code": 200} 
	except Exception as e:
		return {"status": "failed", "except" : e} 

@app.get("/healthcheck")
def check_health():
	try:
		return {"status": "success", "status_code": 200} 
	except Exception as e:
		return {"status": "failed", "except" : e} 

