def soma(a,b):
    return a + b
def subtracao(c,d):
    return c - d
def multiplique(c,d):
    return c * d
def divisao(c,d):
    return c / d


#resultadgo = soma (1,2)
#print ("Soma:" , resultado)

#soma
def test_soma():
    assert soma(4,4)==8
    
def test_soma():
    assert soma(3,2)==5
    
def test_soma():
    assert soma(10,5)==15
#subtracçao
    
def test_subtracao():
    assert subtracao(4,2)==2
    
def test_subtracao():
    assert (10,5)==5
    
def test_subtracao():
    assert subtracao(8,2)==6
    
#multipliçao
    
def test_multiplique():
    assert multiplique(2,2)==4
    
def test_multiplique():
    assert multiplique(3,2)==6
    
def test_multiplique():
    assert multiplique(5,2)==10
#divisao

def test_divisao():
    assert divisao(6,2)==3
    
def test_divisao():
    assert divisao(2,2)==1
    
def test_divisao():
    assert divisao(10,2)==5

    