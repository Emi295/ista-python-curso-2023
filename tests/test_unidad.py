from escuela_api.app import curso_existente

def test_validar_curso():
     curso1 = 'java'
     curso2 = 'go'

     valida_curso1 = curso_existente(curso1)
     valida_curso2 = curso_existente(curso2)

     assert valida_curso1 == True
     assert valida_curso2 == False

