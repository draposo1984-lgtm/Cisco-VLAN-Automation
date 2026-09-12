\# Plano de Automação da Configuração de VPN IPSec entre Fortigate e Palo Alto



\## 1. Objetivo



Este documento apresenta um plano de automação para implantação de uma VPN Site-to-Site IPSec entre um firewall Fortigate e um firewall Palo Alto.



O objetivo é padronizar o processo de configuração, reduzir erros operacionais e facilitar a implantação de túneis VPN em ambientes com equipamentos de fabricantes distintos.



\---



\## 2. Definição dos Parâmetros



\### Fortigate



| Parâmetro | Valor |

|------------|------------|

| IP WAN | 200.1.1.1 |

| Rede Local | 10.1.1.0/24 |

| IP do Túnel | 169.255.1.1/30 |



\### Palo Alto



| Parâmetro | Valor |

|------------|------------|

| IP WAN | 100.1.1.1 |

| Rede Local | 10.2.2.0/24 |

| IP do Túnel | 169.255.1.2/30 |



\### Configurações Phase 1 (IKE)



\- IKEv2

\- AES-256

\- SHA-256

\- Diffie-Hellman Group 14

\- Lifetime: 28800 segundos

\- Chave Pré-Compartilhada (PSK)



\### Configurações Phase 2 (IPSec)



\- AES-256

\- SHA-256

\- Perfect Forward Secrecy (PFS) Grupo 14

\- Lifetime: 3600 segundos



\---



\## 3. Ferramentas e APIs para Automação



\### Fortinet



As opções disponíveis para automação incluem:



\- REST API

\- SSH

\- FortiManager



\### Palo Alto



As opções disponíveis para automação incluem:



\- REST API

\- XML API

\- SSH

\- Panorama



\### Bibliotecas Python



As bibliotecas sugeridas para a implementação da automação são:



\- requests

\- netmiko

\- paramiko



\---



\## 4. Passos de Automação



O processo de automação pode seguir o fluxo abaixo:



\### Etapa 1 - Recebimento dos Parâmetros



Receber as informações necessárias para a VPN:



\- IP WAN do Fortigate;

\- IP WAN do Palo Alto;

\- Redes locais;

\- Configurações de Phase 1;

\- Configurações de Phase 2;

\- Chave pré-compartilhada.



\### Etapa 2 - Configuração do Fortigate



1\. Conectar ao equipamento utilizando API ou SSH.

2\. Criar objetos de rede.

3\. Configurar a Phase 1 (IKE).

4\. Configurar a Phase 2 (IPSec).

5\. Criar políticas de firewall.

6\. Criar rotas necessárias para o tráfego VPN.



\### Etapa 3 - Configuração do Palo Alto



1\. Conectar ao equipamento utilizando API ou SSH.

2\. Criar objetos de rede.

3\. Configurar a Phase 1 (IKE).

4\. Configurar a Phase 2 (IPSec).

5\. Criar políticas de segurança.

6\. Configurar as rotas necessárias.



\### Etapa 4 - Aplicação das Configurações



Após a criação dos objetos e políticas:



\- Aplicar as configurações.

\- Executar o processo de commit.

\- Confirmar sucesso da operação.



\### Etapa 5 - Validação



Executar validações em ambos os dispositivos para verificar o estabelecimento correto do túnel.



\---



\## 5. Considerações Específicas



A automação entre fabricantes diferentes apresenta alguns desafios importantes:



\### Diferenças de API



Fortinet e Palo Alto utilizam estruturas de API distintas, exigindo tratamento específico para cada plataforma.



\### Diferenças de Configuração



As nomenclaturas de objetos, políticas e interfaces podem variar significativamente entre os fabricantes.



\### Processo de Commit



O Palo Alto exige um processo explícito de commit para aplicação das configurações, enquanto o Fortigate normalmente aplica as alterações imediatamente.



\### Compatibilidade de Criptografia



Os parâmetros das fases IKE e IPSec devem ser exatamente compatíveis entre os dois equipamentos.



\### Tratamento de Erros



As mensagens e códigos de erro retornados pelas APIs podem variar entre os fabricantes, exigindo tratamento específico para cada cenário.



\---



\## 6. Validação da Configuração



Após a aplicação da VPN, recomenda-se executar validações em ambos os equipamentos.



\### Fortigate



Comandos sugeridos:



```text

get vpn ipsec tunnel summary

diagnose vpn tunnel list

```



\### Palo Alto



Comandos sugeridos:



```text

show vpn ike-sa

show vpn ipsec-sa

```



\### Verificações Adicionais



\- Confirmação do estado do túnel.

\- Verificação dos Security Associations (SA).

\- Verificação das rotas configuradas.

\- Teste de conectividade entre as redes remotas.



\### Testes de Conectividade



Executar:



```text

ping

traceroute

```



entre hosts localizados em cada extremidade da VPN.



\---



\## 7. Estratégia de Alertas



Em caso de falha durante a automação ou validação, o sistema deve:



\- Registrar o erro em log.

\- Informar o equipamento onde ocorreu a falha.

\- Informar a etapa da configuração que apresentou erro.

\- Informar o motivo detectado.

\- Interromper o processo quando necessário.



\### Exemplos de Alertas



```text

Falha na criação da Phase 1 no Fortigate.

```



```text

Parâmetros criptográficos incompatíveis entre os equipamentos.

```



```text

Túnel IPSec não estabelecido após a aplicação da configuração.

```



```text

Falha de autenticação na API do Palo Alto.

```



\---



\## 8. Conclusão



A utilização de ferramentas de automação permite reduzir o tempo de implantação e minimizar erros operacionais na configuração de VPNs IPSec entre equipamentos Fortinet e Palo Alto.



Devido às diferenças entre fabricantes, recomenda-se utilizar APIs oficiais sempre que possível e implementar mecanismos de validação e tratamento de erros para garantir a consistência das configurações em ambas as extremidades do túnel.

