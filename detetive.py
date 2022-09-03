#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

Telefonou para a vítima?
Esteve no local do crime?
Mora perto da vítima?
Devia para a vítima?
Já trabalhou com a vítima?

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente"."""


# In[ ]:


classif = []
nome = input('Boa noite! Sou o Inspetor Bugiganga. Qual o seu nome? ')
print(f'{nome}, preciso fazer algumas perguntas sobre o assassinato do Kuririn.')

while True:
    escolha = input('Você se importa? Responda [S] para Sim ou [N] para Não.')
    q = escolha.title()
    if q == 'N':
        print('Ok, então vamos ao que interessa. Responda [S] para Sim ou [N] para Não.')
        while True:
            q1 = input("Você telefonou para a vítima? " )
            q0 = q1.title()
            if q0 == 'S':
                classif.append(q0)
                break
            elif q0 == 'N':
                break
            else:
                print('Opção inválida. Responda [S] para Sim ou [N] para Não.')

        while True:
            q2 = input("Esteve no local do crime?" )
            q0 = q2.title()
            if q0 == 'S':
                classif.append(q0)
                break
            elif q0 == 'N':
                break
            else:
                print('Opção inválida. Responda [S] para Sim ou [N] para Não.')

        while True:        
            q3 = input("Mora perto da vítima?" )
            q0 = q3.title()
            if q0 == 'S':
                classif.append(q0)
                break
            elif q0 == 'N':
                break
            else:
                print('Opção inválida. Responda [S] para Sim ou [N] para Não.')

        while True:        
            q4 = input("Devia para a vítima?" )
            q0 = q4.title()
            if q0 == 'S':
                classif.append(q0)
                break
            elif q0 == 'N':
                break
            else:
                print('Opção inválida. Responda [S] para Sim ou [N] para Não.')

        while True:        
            q5 = input("Já trabalhou com a vítima?" )
            q0 = q5.title()
            if q0 == 'S':
                classif.append(q0)
                break
            elif q0 == 'N':
                break
            else:
                print('Opção inválida. Responda [S] para Sim ou [N] para Não.')
                
        if len(classif) == 5:
            print(f'{nome}, você está preso pelo assassinato do Kuririn!')
            break
        elif len(classif) >= 3:
            print(f'{nome}, me acompanhe, pois você é cúmplice no assassinato do Kuririn!')
            break
        elif len(classif) == 2:
            print(f'{nome}, não saia da cidade, precisamos conversar ainda!')
            break
        else:
            print(f'{nome}, pode ir agora! Obrigado por sua atenção')
            break
    elif q == 'S':
        print(f'Ok, nos vemos na delegacia. Até mais {nome}.')
        break
    else:
        print('Opção inválida.')
        continue

