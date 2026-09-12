# Cisco VLAN Automation

Projeto desenvolvido em Python e Flask para automatizar configurações de rede em switches Cisco e documentar uma estratégia de automação para VPN Site-to-Site IPSec entre firewalls Fortinet e Palo Alto.

---

# Objetivos

O projeto foi dividido em duas etapas:

## Parte 1 – Automação de VLANs

Desenvolver uma aplicação web capaz de automatizar configurações em switches Cisco através de conexão SSH.

## Parte 2 – Planejamento de Automação VPN IPSec

Elaborar um plano detalhado de automação para implantação de uma VPN Site-to-Site IPSec entre firewalls de fabricantes distintos, identificando ferramentas, APIs, fluxo de automação, validação e desafios técnicos.

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
- Salvamento da configuração na NVRAM;
- Backup das configurações do switch;
- Validação automática da configuração aplicada;
- Exibição do resultado da execução na interface web.

### VLANs Implementadas

| VLAN | Nome |
| ------ | ------ |
| 10 | VLAN_DADOS |
| 20 | VLAN_VOZ |
| 50 | VLAN_SEGURANCA |

---

# Estrutura do Projeto

```text
Cisco-VLAN-Automation/
│
├── README.md
├── app.py
│
├── backup/
│   └── SWITCH_AUTOMATIZADO_20260912_123412.txt
│
├── templates/
│   └── index.html
│
├── docs/
│   └── Automacao_VPN.md
│
└── evidencias/
    ├── backup_gerado.png
    ├── front.end.png
    ├── hostname_alterado.png
    ├── sh run inicial.txt
    ├── validacao_sucesso.png
    └── vlans_configuradas.png
```

---

# Instalação

Clone o repositório:

```bash
git clone https://github.com/draposo1984-lgtm/Cisco-VLAN-Automation.git
```

Acesse o diretório do projeto:

```bash
cd Cisco-VLAN-Automation
```

Instale as dependências necessárias:

```bash
pip install flask netmiko
```

---

# Execução

Execute a aplicação:

```bash
python app.py
```

Acesse pelo navegador:

```text
http://127.0.0.1:5000
```

---

# Utilização do Frontend

1. Execute a aplicação Flask.
2. Acesse a interface web.
3. Informe os dados de conexão do switch Cisco:
   - Endereço IP;
   - Usuário;
   - Senha.
4. Informe o hostname desejado.
5. Confirme as VLANs a serem configuradas.
6. Execute a automação.
7. Acompanhe o resultado apresentado na tela.

---

# Fluxo de Funcionamento

1. O usuário acessa a interface web.
2. Informa os dados do switch.
3. A aplicação estabelece conexão SSH.
4. O hostname é configurado.
5. As VLANs são criadas automaticamente.
6. A configuração é salva na NVRAM.
7. Um backup da configuração é gerado.
8. A validação da configuração é executada.
9. O resultado é exibido ao usuário.

---

# Backup da Configuração

Após a aplicação das configurações, a solução realiza automaticamente um backup da configuração atual do switch.

Os arquivos são armazenados na pasta:

```text
backup/
```

Exemplo:

```text
backup/SWITCH_AUTOMATIZADO_20260912_123412.txt
```

---

# Validação e Alertas

Após a aplicação das configurações, o sistema executa uma validação automática para verificar:

- Hostname configurado;
- VLAN 10 (VLAN_DADOS);
- VLAN 20 (VLAN_VOZ);
- VLAN 50 (VLAN_SEGURANCA).

Caso alguma divergência seja identificada, uma mensagem de alerta é exibida ao usuário.

Em caso de sucesso, a aplicação apresenta a confirmação da configuração aplicada e da validação realizada.

---

# Evidências

As evidências do funcionamento da solução encontram-se na pasta:

```text
evidencias/
```

Arquivos incluídos:

- front.end.png (frontend da aplicação)
- sh run inicial.txt (configuração inicial do switch)
- vlans_configuradas.png (VLANs criadas no switch)
- hostname_alterado.png (hostname configurado)
- validacao_sucesso.png (resultado da validação)
- backup_gerado.png (evidência do backup gerado)

---

# Parte 2 – Planejamento de Automação VPN IPSec

A segunda etapa consiste na elaboração de uma estratégia para automatização da configuração de uma VPN Site-to-Site IPSec entre firewalls Fortinet e Palo Alto.

O documento contempla:

- Conceitos de VPN IPSec;
- Definição dos parâmetros da VPN;
- Ferramentas e APIs para automação;
- Utilização de SSH e APIs REST;
- Processo de criação de objetos de rede;
- Configuração das fases IKE e IPSec;
- Criação de políticas de firewall;
- Estabelecimento do túnel VPN;
- Desafios da automação entre fabricantes distintos;
- Estratégias de validação da configuração;
- Estratégias de monitoramento e geração de alertas.

A documentação completa encontra-se em:

```text
docs/Automacao_VPN.md
```

---

# Controle de Versões

O projeto utiliza Git para rastrear as alterações realizadas durante o desenvolvimento.

Histórico de commits:

```text
Adicionado README do projeto
Implementada automacao de switch Cisco
Adicionada documentacao da automacao VPN IPSec
Implementada validacao, tratamento de alertas e ajustes no app.py
Finalizada entrega da Parte 1 do projeto
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
- Salvamento da configuração na NVRAM;
- Backup das configurações;
- Validação automática da configuração;
- Evidências de funcionamento;
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

Analista de Redes