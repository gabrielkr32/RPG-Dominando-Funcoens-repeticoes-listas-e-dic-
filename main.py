from random import randint

listas_npcs = []


player = {
    "nome": "Gabriel",
    "level": 1, 
    "exp": 0,
    "exp_max": 30,
    "hp": 100,
    "hp_max": 100,
    "dano": 25,
}


def criar_npc(level):
    #level = randint(0,50)

    novo_npc = {
        "nome": f"Monstro #{level}",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp": 7 * level,
    }

    return novo_npc 
    #listas_npcs.append(novo_npc)


def gerar_npcs(n_npcs):
    
    for x in range (n_npcs):
        #print(x)
        npc = criar_npc(x + 1)#encremento, faz a criação do npc começar no level 1, e nao 0.
        listas_npcs.append(npc)
  

def exibir_npcs():
    for npc in listas_npcs:
        print(f"Nome: {npc['nome']}// Level: {npc['level']}// Dano: {npc['dano']}//HP:{npc['hp']}// EXP: {npc['exp']}")
       


# atacar_npc(npc)>> npc:hp - player :dano
def inicar_batalha(npc):
    atacar_npc(npc)
    atacar_player(npc)
    exibir_info_batalha(npc)

def atacar_npc(npc):
     npc['hp'] -= player['dano']    

# atacar_player(npc)>> player:hp - npc:dano
def atacar_player(npc):
    player['hp'] -= npc['dano']


def exibir_info_batalha(npc):
    print(f"Player {player['hp']}/{player['hp_max']}")
    print(f"NPC:{npc['nome']}: {npc['hp']}/{npc['hp_max']}")

gerar_npcs(5)
#exibir_npcs()

npc_selecionado = listas_npcs[0]

#print("NPC selecionando:", npc_selecionado)
inicar_batalha(npc_selecionado)

#print("NPC atacado", npc_selecionado)
