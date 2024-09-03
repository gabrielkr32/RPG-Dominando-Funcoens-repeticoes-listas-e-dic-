from random import randint

listas_npcs = []


player = {
    "nome": "Gabriel",
    "level": 1, 
    "exp": 0,
    "exp_max": 50,
    "ho": 100,
    "ho_max": 100,
    "dano": 25,
}


def criar_npc():
    level = randint(0,50)

    novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "exp": 7 * level,
    }

    return novo_npc 
    #listas_npcs.append(novo_npc)


def gerar_npcs(n_npcs):
    
    for x in range (n_npcs):
        #print(x)
        novo_npc = criar_npc(x + 1)#1+1 encremento
        listas_npcs.append(novo_npc)
  

def exibir_npcs():
    for npc in listas_npcs:
        print(f"Nome: {npc['nome']}// Level: {npc['level']}// Dano: {npc['dano']}//HP:{npc['hp']}")
       
# atacar_npc(npc)>> npc:hp - player :dano
def atacar_npc(npc):
    npc['hp'] =- player['dano']

# atacar_player(npc)>> player:hp - npc:dano




gerar_npcs(5)
exibir_npcs()

npc_selecionado = listas_npcs[0]

print("NPC selecionando:", npc_selecionado)
atacar_npc(npc_selecionado)

print("NPC atacado", npc_selecionado)