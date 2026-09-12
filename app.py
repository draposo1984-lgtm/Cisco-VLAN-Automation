from flask import Flask, render_template, request
from netmiko import ConnectHandler
from datetime import datetime
import os
import time

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    resultado = ""

    if request.method == "POST":

        try:
            ip = request.form["ip"]
            username = request.form["username"]
            password = request.form["password"]

            hostname = request.form["hostname"]

            vlan_id_1 = request.form["vlan_id_1"]
            vlan_nome_1 = request.form["vlan_nome_1"]

            vlan_id_2 = request.form["vlan_id_2"]
            vlan_nome_2 = request.form["vlan_nome_2"]

            vlan_id_3 = request.form["vlan_id_3"]
            vlan_nome_3 = request.form["vlan_nome_3"]

            switch = {
                "device_type": "cisco_ios",
                "host": ip,
                "username": username,
                "password": password
            }

            conn = ConnectHandler(**switch)

            # Altera o hostname
            conn.send_config_set([
                f"hostname {hostname}"
            ])

            # Atualiza o prompt do Netmiko
            time.sleep(1)
            conn.set_base_prompt()

            # Criação das VLANs
            comandos = [
                f"vlan {vlan_id_1}",
                f"name {vlan_nome_1}",

                f"vlan {vlan_id_2}",
                f"name {vlan_nome_2}",

                f"vlan {vlan_id_3}",
                f"name {vlan_nome_3}"
            ]

            conn.send_config_set(comandos)

            # Salva na NVRAM
            conn.save_config()

            # Backup
            os.makedirs("backup", exist_ok=True)

            backup = conn.send_command("show running-config")

            hostname_switch = conn.find_prompt().replace("#", "")

            data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")

            nome_arquivo = (
                f"backup/{hostname_switch}_{data_hora}.txt"
            )

            with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
                arquivo.write(backup)

            # ==========================
            # VALIDAÇÃO
            # ==========================

            validacao = []

            # Validação do hostname
            hostname_configurado = conn.find_prompt().replace("#", "")

            if hostname_configurado == hostname:
                validacao.append("✅ Hostname configurado corretamente")
            else:
                validacao.append(
                    f"⚠️ ALERTA: Hostname esperado '{hostname}' "
                    f"mas encontrado '{hostname_configurado}'"
                )

            # Validação das VLANs
            vlans = conn.send_command("show vlan brief")

            if vlan_nome_1 in vlans:
                validacao.append(
                    f"✅ VLAN {vlan_id_1} ({vlan_nome_1}) encontrada"
                )
            else:
                validacao.append(
                    f"⚠️ ALERTA: VLAN {vlan_id_1} não encontrada"
                )

            if vlan_nome_2 in vlans:
                validacao.append(
                    f"✅ VLAN {vlan_id_2} ({vlan_nome_2}) encontrada"
                )
            else:
                validacao.append(
                    f"⚠️ ALERTA: VLAN {vlan_id_2} não encontrada"
                )

            if vlan_nome_3 in vlans:
                validacao.append(
                    f"✅ VLAN {vlan_id_3} ({vlan_nome_3}) encontrada"
                )
            else:
                validacao.append(
                    f"⚠️ ALERTA: VLAN {vlan_id_3} não encontrada"
                )

            conn.disconnect()

            resultado = f"""
✅ Configuração aplicada com sucesso!

✅ Configuração salva na NVRAM!

✅ Backup realizado com sucesso!

Arquivo gerado:
{nome_arquivo}

Hostname:
{hostname}

VLAN {vlan_id_1}: {vlan_nome_1}
VLAN {vlan_id_2}: {vlan_nome_2}
VLAN {vlan_id_3}: {vlan_nome_3}

==========================
VALIDAÇÃO
==========================

{chr(10).join(validacao)}
"""

        except Exception as erro:

            resultado = f"""
❌ ERRO

{erro}
"""

    return render_template(
        "index.html",
        resultado=resultado
    )

if __name__ == "__main__":
    app.run(debug=True)