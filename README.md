# Cisco VLAN Automation

Projeto desenvolvido em Python e Flask para automatizar configurações de rede em equipamentos Cisco e documentar uma estratégia de automação para VPN Site-to-Site IPSec entre firewalls Fortinet e Palo Alto.

---

# Objetivos

O projeto foi dividido em duas etapas:

## Parte 1 – Automação de VLANs

Desenvolver uma aplicação web capaz de automatizar configurações em switches Cisco através de conexão SSH.

## Parte 2 – Planejamento de Automação VPN IPSec

Elaborar um plano detalhado de automação para implantação de VPN Site-to-Site IPSec entre firewalls de fabricantes distintos, identificando ferramentas, APIs, fluxo de automação, validação e desafios técnicos.

---

# Tecnologias Utilizadas

- Python 3
- Flask
- Netmiko
- HTML
- CSS
- Cisco IOS
- Git

---

# Funcionalidades

## Parte 1 – Automação de VLANs

A aplicação realiza:

- Conexão SSH com switches Cisco;
- Configuração automática do hostname do equipamento;
- Criação das VLANs solicitadas;
- Configuração de interfaces;
- Exibição do resultado da execução na interface web;
- Backup das configurações do switch.

### VLANs Implementadas

| VLAN | Nome |
|--------|--------|
| 10 | VLAN_DADOS |
| 20 | VLAN_VOZ |
| 50 | VLAN_SEGURANCA |

---

# Estrutura do Projeto

```text
Cisco-VLAN-Automation/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── backups/
│
└── docs/
    └── Automacao_VPN.md
```

---

# Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/Cisco-VLAN-Automation.git
```

Acesse o diretório do projeto:

```bash
cd Cisco-VLAN-Automation
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

# Execução

Execute a aplicação:

```bash
python app.py
```

Acesse:

```text
http://127.0.0.1:5000
```

---

# Parte 1 – Fluxo de Funcionamento

1. O usuário acessa a interface web.
2. São informados os dados do switch.
3. A aplicação estabelece conexão SSH.
4. O hostname é configurado.
5. As VLANs são criadas automaticamente.
6. As configurações são aplicadas.
7. Um backup da configuração é armazenado.
8. O resultado é exibido na interface.

---

# Parte 2 – Planejamento de Automação VPN IPSec

A segunda etapa consiste na elaboração de uma estratégia para automatização da configuração de uma VPN Site-to-Site IPSec entre firewalls Fortinet e Palo Alto.

O documento contempla:

- Conceitos de VPN IPSec;
- Ferramentas e APIs para automação;
- Utilização de SSH e APIs REST;
- Processo de criação de objetos de rede;
- Configuração das fases IKE e IPSec;
- Criação de políticas de firewall;
- Estabelecimento do túnel VPN;
- Desafios da automação entre fabricantes diferentes;
- Estratégias de validação da configuração;
- Estratégias de monitoramento e geração de alertas.

A documentação completa encontra-se no arquivo:

```text
docs/Automacao_VPN.md
```

---

# Ferramentas Avaliadas para Automação da VPN

## Fortinet

- REST API
- SSH
- FortiManager

## Palo Alto

- REST API
- XML API
- SSH
- Panorama

## Bibliotecas Python

- requests
- netmiko
- paramiko

---

# Controle de Versões

O projeto utiliza Git para rastrear todas as alterações realizadas durante o desenvolvimento.

Exemplos de commits:

```text
Projeto inicial Flask
Implementação da automação de VLANs
Configuração automática do hostname
Criação das VLANs 10, 20 e 50
Implementação do backup das configurações
Melhorias na interface web
Adição da documentação da automação VPN IPSec
Atualização final do README
```

Para visualizar o histórico:

```bash
git log --oneline
```

---

# Entregáveis

## Parte 1

- Código-fonte da aplicação;
- Interface web em Flask;
- Automação de VLANs;
- Configuração de hostname;
- Backup das configurações;
- README do projeto;
- Histórico de versões no Git.

## Parte 2

- Mesmo repositório Git da Parte 1;
- Documento de planejamento da automação VPN IPSec;
- Estratégia de validação e monitoramento;
- Documentação das ferramentas e APIs relevantes para Fortinet e Palo Alto.

---

# Autor

Daniel Faria
